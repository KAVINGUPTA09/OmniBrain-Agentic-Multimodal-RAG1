import os
import uvicorn
from backend.app import app

if __name__ == "__main__":
    # Force port 8000 regardless of Render's PORT environment variable
    uvicorn.run(app, host="127.0.0.1", port=8000)