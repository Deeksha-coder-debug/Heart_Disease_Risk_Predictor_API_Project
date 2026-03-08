#!/bin/bash

echo "Starting FastAPI server..."
uvicorn app:app --host 0.0.0.0 --port 8000 &

echo "Starting Streamlit app..."
streamlit run frontend.py --server.address=0.0.0.0 --server.port=8501