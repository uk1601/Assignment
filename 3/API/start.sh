#!/bin/bash
redis-server --daemonize yes #running the redis-server in background
python3 /app/app.py #running the flask api endpoints file
