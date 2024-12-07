import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "app.main:app",  # Reference to the app instance in app/main.py
        host="0.0.0.0",
        port=port,
        reload=True  # Optional: Disable in production for better performance
    )
