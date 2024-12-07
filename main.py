import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
import uvicorn

# Create the FastAPI app instance
app = FastAPI()

# Middleware
app.add_middleware(SessionMiddleware, secret_key="add_any_string_here")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define the root route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

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
        "redirect_uri": "http://localhost:8000/auth"
    }
)

if __name__ == "__main__":
    # Get the port from the environment variable or use 8000 as default
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

# The following code snippets were removed during the consolidation process,
# but are preserved here for your reference and potential reuse.

# Example: Route for OAuth login
# @app.get("/login")
# async def login(request: Request):
#     redirect_uri = request.url_for("auth")
#     return await oauth.google.authorize_redirect(request, redirect_uri)

# Example: Route for OAuth callback
# @app.get("/auth")
# async def auth(request: Request):
#     try:
#         token = await oauth.google.authorize_access_token(request)
#         user = await oauth.google.parse_id_token(request, token)
#         request.session["user"] = dict(user)
#     except OAuthError:
#         return RedirectResponse(url="/")
#     return RedirectResponse(url="/welcome")

# Example: Welcome route
# @app.get("/welcome")
# async def welcome(request: Request):
#     user = request.session.get("user")
#     if not user:
#         return RedirectResponse(url="/")
#     return templates.TemplateResponse("welcome.html", {"request": request, "user": user})

# --- END OF PRESERVED CODE ---
