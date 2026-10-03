#!/bin/bash
export PYTHONPATH=.

# 1. FastAPI backend ko internal port 8000 par start karo
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 &

# 2. 5 second wait karo taaki backend puri tarah load ho jaye
sleep 5

# 3. Streamlit frontend ko Render ke $PORT (10000) par launch karo
streamlit run frontend/app.py --server.port $PORT --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false