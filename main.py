import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
from config import STATIC_DIR, CLIENT_ID, CLIENT_SECRET
from fastapi.staticfiles import StaticFiles
import uvicorn

# Create the FastAPI app instance
app = FastAPI()

# Middleware
app.add_middleware(SessionMiddleware, secret_key="add_any_string_here")

# Static files
# Use environment variable to configure the static directory
static_dir = os.environ.get("STATIC_DIR", "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define the root route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        name="home.html",
        context={"request": request}
        )
@app.get("/login")
async def login(request: Request):
    url = request.url_for("auth")
    return await oauth.google.authorize_redirect(request, url)

# OAuth configuration
from authlib.integrations.starlette_client import OAuth, OAuthError
from config import CLIENT_ID, CLIENT_SECRET  # Changed to absolute import
oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs={
        "scope": "openid email profile",
        "redirect_uri": os.environ.get("REDIRECT_URI", "http://localhost:8000/auth")
    }
)

for route in app.routes:
    print(route.path, route.name)

if __name__ == "__main__":
    # Get the port from the environment variable or use 8000 as default
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
