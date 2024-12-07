import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

# Create the FastAPI app instance
app = FastAPI()

# Middleware
app.add_middleware(SessionMiddleware, secret_key="add_any_string_here")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Define routes or other application logic here (add existing routes from app/main.py if needed)

if __name__ == "__main__":
    # Get the port from the environment variable or use 8000 as default
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        app,  # Pass the app instance directly
        host="0.0.0.0",
        port=port,
        reload=True  # Optional: Disable in production for better performance
    )

# --- PRESERVED CODE (PREVIOUSLY REMOVED) ---
# The following code snippets were removed during the consolidation process,
# but are preserved here for your reference and potential reuse.

# Example: OAuth configuration
# from authlib.integrations.starlette_client import OAuth, OAuthError
# from .config import CLIENT_ID, CLIENT_SECRET
# 
# oauth = OAuth()
# oauth.register(
#     name="google",
#     client_id=CLIENT_ID,
#     client_secret=CLIENT_SECRET,
#     access_token_url="https://accounts.google.com/o/oauth2/token",
#     authorize_url="https://accounts.google.com/o/oauth2/auth",
#     api_base_url="https://www.googleapis.com/oauth2/v1/",
#     client_kwargs={"scope": "openid email profile"},
# )

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
