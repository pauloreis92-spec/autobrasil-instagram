# Auto Brasil – publicação automática no Instagram

- `fila/AAAA-MM-DD.json`: o que publicar em cada dia (tipo `story` ou `feed`, horário, imagem, legenda).
- `artes/AAAA-MM-DD/`: as imagens JPG.
- A cada 15 minutos o GitHub roda `publicar.py`, publica no @auto_brasil2 o que chegou a hora e marca `publicado`.
- A chave da Meta fica em *Settings > Secrets and variables > Actions* com o nome `IG_TOKEN` (nunca no código).
