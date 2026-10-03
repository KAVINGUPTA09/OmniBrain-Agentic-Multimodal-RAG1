#!/bin/bash
export PYTHONPATH=.

# 1. FastAPI backend ko dedicated runner se port 8000 par launch karo
python run_backend.py &

# 2. Wait 5 seconds taaki backend successfully start ho sake
sleep 5

# 3. Streamlit frontend ko Render ke public port par chalao
streamlit run frontend/app.py \
  --server.port $PORT \
  --server.address 0.0.0.0 \
  --server.headless true \
  --server.enableCORS false \
  --server.enableXsrfProtection false \
  --browser.gatherUsageStats false