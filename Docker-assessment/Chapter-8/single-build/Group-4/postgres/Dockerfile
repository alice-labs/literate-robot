FROM debian:sid-slim

RUN apt-get update && apt-get install -y postgresql postgresql-contrib

COPY Docker-assessment/Chapter-8/single-build/Group-4/postgres/postgresql_entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/postgresql_entrypoint.sh

ENTRYPOINT ["postgresql_entrypoint.sh"]
