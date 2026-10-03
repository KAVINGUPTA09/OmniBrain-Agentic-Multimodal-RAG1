#!/bin/bash
export PYTHONPATH=.

# 1. FastAPI backend ko strictly 127.0.0.1:8000 par start karo
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 &

# 2. 5 second wait karo taaki FastAPI listen mode me aa jaye
sleep 5

# 3. Streamlit ko Render ke public $PORT par headless mode me chalao
streamlit run frontend/app.py \
  --server.port $PORT \
  --server.address 0.0.0.0 \
  --server.headless true \
  --server.enableCORS false \
  --server.enableXsrfProtection false \
  --browser.gatherUsageStats false