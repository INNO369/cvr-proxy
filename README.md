# CVR Proxy Server

Proxy für die dänische CVR-API (virk.dk) — löst CORS-Probleme im Browser.

## Deploy auf Render.com

1. Dieses Repo auf GitHub hochladen
2. render.com → "New Web Service" → GitHub Repo verbinden
3. Settings:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Deploy klicken → fertig!

## Endpunkt

`POST https://DEINE-URL.onrender.com/cvr`

Header: `X-CVR-Auth: <base64(user:password)>`
