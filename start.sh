#!/bin/bash

# Navigate to server and start FastAPI
echo "Starting backend..."
cd server
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..

# Navigate to frontend and start React/Next.js app
echo "Starting frontend..."
cd client
npm run dev &
FRONTEND_PID=$!
cd ..

# Wait for both to finish
trap "kill $BACKEND_PID $FRONTEND_PID" SIGINT
wait $BACKEND_PID $FRONTEND_PID