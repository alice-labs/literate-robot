FROM debian:sid-slim

RUN apt-get update && apt-get install -y redis-server

COPY Docker-assessment/Chapter-8/single-build/Group-4/Redis/redis_entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/redis_entrypoint.sh

ENTRYPOINT ["redis_entrypoint.sh"]
