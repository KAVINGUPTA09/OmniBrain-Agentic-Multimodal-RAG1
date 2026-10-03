#!/bin/bash
export PYTHONPATH=.

# Render ka $PORT ek naye variable me save karo Streamlit ke liye
STREAMLIT_PORT=${PORT:-10000}

# Uvicorn ko force karo ki wo Render ka PORT na le, balki 8000 par chale
PORT=8000 python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 &

# 4 second wait taaki backend cleanly listen kare
sleep 4

# Streamlit ko Render ke public port par start karo
streamlit run frontend/app.py \
  --server.port $STREAMLIT_PORT \
  --server.address 0.0.0.0 \
  --server.headless true \
  --server.enableCORS false \
  --server.enableXsrfProtection false \
  --browser.gatherUsageStats false