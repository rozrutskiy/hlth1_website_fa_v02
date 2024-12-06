import uvicorn
import os

if __name__ == "__main__":
    # Get the port from the environment variable, default to 8000 if not set
    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        app="app.main:app",  # Points to the app instance inside 'app.main'
        host="0.0.0.0",      # Use '0.0.0.0' to allow external access
        port=port,           # Use the dynamic port from the environment variable
        reload=True          # Enable auto-reload during development (can be removed in production)
    )
