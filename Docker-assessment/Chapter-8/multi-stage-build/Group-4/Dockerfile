FROM debian:sid-slim as debian_base

# ENV DEBIAN_FRONTEND=noninteractive

# Install common dependencies
RUN apt-get update && apt-get install -y \
    postgresql postgresql-contrib \
    mysql-server \
    redis-server \
    rabbitmq-server

# Install Python and dependencies
RUN apt-get update && apt install -y python3 python3-pip python3-venv

# Install FastAPI dependencies
FROM debian_base as fastapi
WORKDIR /app

# Create a virtual environment and install dependencies
RUN python3 -m venv /app/venv
COPY Docker-assessment/Chapter-8/multi-stage-build/Group-4/fastapi /app/
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy entrypoint scripts
COPY Docker-assessment/Chapter-8/multi-stage-build/Group-4/postgresql_entrypoint.sh /usr/local/bin/
COPY Docker-assessment/Chapter-8/multi-stage-build/Group-4/mysql_entrypoint.sh /usr/local/bin/
COPY Docker-assessment/Chapter-8/multi-stage-build/Group-4/redis_entrypoint.sh /usr/local/bin/
COPY Docker-assessment/Chapter-8/multi-stage-build/Group-4/rabbitmq_entrypoint.sh /usr/local/bin/
COPY Docker-assessment/Chapter-8/multi-stage-build/Group-4/build_entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/postgresql_entrypoint.sh
RUN chmod +x /usr/local/bin/mysql_entrypoint.sh
RUN chmod +x /usr/local/bin/redis_entrypoint.sh
RUN chmod +x /usr/local/bin/rabbitmq_entrypoint.sh
RUN chmod +x /usr/local/bin/build_entrypoint.sh

ENTRYPOINT ["build_entrypoint.sh"]
