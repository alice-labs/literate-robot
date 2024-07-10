FROM debian:sid-slim

RUN apt-get update && apt-get install -y mysql-server

COPY Docker-assessment/Chapter-8/single-build/Group-4/Mysql/mysql_entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/mysql_entrypoint.sh

ENTRYPOINT ["mysql_entrypoint.sh"]
