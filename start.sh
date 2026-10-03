#!/bin/bash

# 1. Background mein FastAPI backend start karo (internal port 8000 par)
uvicorn backend.app:app --host 0.0.0.0 --port 8000 &

# 2. Render ke assigned $PORT par Streamlit frontend launch karo
streamlit run frontend/app.py --server.port $PORT --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false