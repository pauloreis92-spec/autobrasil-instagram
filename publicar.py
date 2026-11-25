"""Publica no Instagram da Auto Brasil o que estiver na fila e já tiver chegado a hora.
Roda no GitHub Actions a cada 15 minutos. Usa a API oficial da Meta (Content Publishing)."""
import json, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timedelta, timezone

IG_ID = "17841403091421343"           # @auto_brasil2
API = "https://graph.facebook.com/v23.0"
REPO = os.environ.get("GITHUB_REPOSITORY", "pauloreis92-spec/autobrasil-instagram")
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
TOKEN = os.environ["IG_TOKEN"]
BRT = timezone(timedelta(hours=-3))
JANELA_MAX = timedelta(hours=3)        # não publica se passou mais de 3h do horário (evita story atrasado)

def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    url = f"{API}/{path}"
    req = urllib.request.Request(url + ("" if method == "POST" else "?" + data.decode()),
                                 data=data if method == "POST" else None, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(e.read().decode()[:500])

def publicar(item):
    if item["tipo"] == "reel":
        p = {"video_url": RAW + urllib.parse.quote(item["video"]), "media_type": "REELS",
             "caption": item.get("legenda", ""), "share_to_feed": "true"}
        if item.get("capa"): p["cover_url"] = RAW + urllib.parse.quote(item["capa"])
    else:
        p = {"image_url": RAW + urllib.parse.quote(item["imagem"])}
        if item["tipo"] == "story":
            p["media_type"] = "STORIES"
        else:
            p["caption"] = item.get("legenda", "")
    cont = call("POST", f"{IG_ID}/media", **p)["id"]
    for _ in range(60 if item["tipo"] == "reel" else 20):
        st = call("GET", cont, fields="status_code").get("status_code")
        if st == "FINISHED": break
        if st == "ERROR": raise RuntimeError("container com erro")
        time.sleep(5)
    return call("POST", f"{IG_ID}/media_publish", creation_id=cont)["id"]

def validar():
    """Cria o container de um story de teste SEM publicar: confere chave, permissões e acesso à imagem."""
    res = {}
    try:
        res["conta"] = call("GET", IG_ID, fields="username")
        cont = call("POST", f"{IG_ID}/media", image_url=RAW + "artes/teste/teste.jpg", media_type="STORIES")["id"]
        for _ in range(12):
            st = call("GET", cont, fields="status_code").get("status_code")
            if st in ("FINISHED", "ERROR"): break
            time.sleep(5)
        res["container"] = st
    except Exception as e:
        res["erro"] = str(e)[:400]
    json.dump(res, open("validacao.json", "w"), ensure_ascii=False, indent=1)
    print(res)

def main():
    if "--validar" in sys.argv:
        return validar()
    teste = "--teste" in sys.argv
    agora = datetime.now(BRT)
    mudou = False
    for arq in sorted(os.listdir("fila")):
        if not arq.endswith(".json"): continue
        caminho = os.path.join("fila", arq)
        fila = json.load(open(caminho, encoding="utf-8"))
        for item in fila:
            if item.get("status") in ("publicado", "perdido"): continue
            quando = datetime.fromisoformat(item["quando"])
            if quando > agora and not teste: continue
            if agora - quando > JANELA_MAX and not teste:
                item["status"] = "perdido"; item["obs"] = f"passou da hora ({agora:%d/%m %H:%M})"; mudou = True
                print("PERDIDO", item.get("imagem") or item.get("video")); continue
            try:
                item["media_id"] = publicar(item)
                item["status"] = "publicado"; item["publicado_em"] = agora.isoformat(timespec="minutes")
                print("OK", item["tipo"], item.get("imagem") or item.get("video"), item["media_id"])
            except Exception as e:
                item["tentativas"] = item.get("tentativas", 0) + 1
                item["erro"] = str(e)[:300]
                if item["tentativas"] >= 3: item["status"] = "perdido"
                print("ERRO", item.get("imagem") or item.get("video"), e)
            mudou = True
            if teste: break
        if mudou:
            json.dump(fila, open(caminho, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        if teste and mudou: break
    print("nada para publicar agora" if not mudou else "fila atualizada")

if __name__ == "__main__":
    main()
