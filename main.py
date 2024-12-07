import os

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse
import uvicorn

# Create the FastAPI app instance
app = FastAPI()

# Removed custom static file serving route

# Middleware
app.add_middleware(SessionMiddleware, secret_key="add_any_string_here")

# Static files
# Mount the static files directory
app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "static")), name="static")

# Jinja2 templates
jinja2_templates = Jinja2Templates(directory="templates")

# Define the root route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return jinja2_templates.TemplateResponse("home.html", {"request": request})
async def read_root(request: Request):
    """
    Handle the root route and render the home page.

    Args:
        request (Request): The request object.

    Returns:
        TemplateResponse: The rendered home page.
    """
    return templates.TemplateResponse("home.html", {"request": request})

# Get the port from the environment variable or use 8000 as the default port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
# The following code snippets were removed during the consolidation process,
# but are preserved here for your reference and potential reuse.

# Example: OAuth configuration
from authlib.integrations.starlette_client import OAuth, OAuthError
from .config import CLIENT_ID, CLIENT_SECRET

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
    # access_token_url="https://accounts.google.com/o/oauth2/token",
    # authorize_url="https://accounts.google.com/o/oauth2/auth",
    # api_base_url="https://www.googleapis.com/oauth2/v1/",
)

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
