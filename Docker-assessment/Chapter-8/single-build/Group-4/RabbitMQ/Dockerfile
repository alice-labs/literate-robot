FROM debian:sid-slim

RUN apt-get update && apt-get install -y rabbitmq-server

COPY Docker-assessment/Chapter-8/single-build/Group-4/RabbitMQ/rabbitmq_entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/rabbitmq_entrypoint.sh

ENTRYPOINT ["rabbitmq_entrypoint.sh"]
