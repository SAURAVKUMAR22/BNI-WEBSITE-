# Putting the site online (a link anyone can open)

The app needs a place that runs Python and keeps files (it stores answers in `data/asks.db` and uploads in `data/media/`).
Pick ONE option.

## Option A - PythonAnywhere (free plan keeps files; link looks like https://YOURNAME.pythonanywhere.com)
1. Make a free account at pythonanywhere.com.
2. **Files** tab: upload `bni-ask-editor.zip`, then in a **Bash console**: `unzip bni-ask-editor.zip`
3. In that console: `cd bni-ask-editor && pip install --user -r requirements.txt`
4. **Web** tab > *Add a new web app* > *Manual configuration* > latest Python.
5. Open the **WSGI configuration file** link, delete what's in it, paste `wsgi_pythonanywhere.py`, set your username and your two keys, Save.
6. Click **Reload**. Your live link is on that Web tab. Share it.
   (Free plan: the site must be re-"extended" with one button click about every 3 months. Very large videos may hit the plan's upload limits - paste a video link instead if so.)

## Option B - Render (paid disk, auto https)
Push the project to a GitHub repo, then Render > New > Blueprint > choose the repo (uses `render.yaml`).
Keys are generated for you under the service's *Environment* tab.

## Option C - your own server / VPS
    pip install -r requirements.txt
    BNI_ADMIN_KEY=... BNI_VIEWER_KEY=... BNI_DATA_DIR=/srv/bni-data gunicorn -w 2 --threads 4 -b 0.0.0.0:8000 app:app
Put it behind HTTPS (Caddy or nginx).

## Before sharing the link
* Set your own long **admin** and **viewer** keys (never leave defaults). Anyone with the link can open the "I'm a viewer" deck.
* Use https. Presenter personal links are the presenters' passwords.
* Back up the whole `data/` folder.
