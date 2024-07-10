#!/bin/bash
# Start all services in the background
/usr/local/bin/postgresql_entrypoint.sh &
/usr/local/bin/mysql_entrypoint.sh &
/usr/local/bin/redis_entrypoint.sh &
/usr/local/bin/rabbitmq_entrypoint.sh &

# Start FastAPI
/app/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
