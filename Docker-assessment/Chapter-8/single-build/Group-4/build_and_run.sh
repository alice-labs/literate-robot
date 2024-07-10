# build and run postgres
echo "Building Postgres"
docker build -t single_postgres -f Docker-assessment/Chapter-8/single-build/Group-4/postgres/Dockerfile .
docker run -d --name=single_postgres_container -p 5432:5432 single_postgres

# build and run mysql
echo "Building MySql"
docker build -t single_mysql -f Docker-assessment/Chapter-8/single-build/Group-4/Mysql/Dockerfile .
docker run -d --name=single_mysql_container -p 3306:3306 single_mysql

# build and run redis
echo "Building Redis"
docker build -t single_redis -f Docker-assessment/Chapter-8/single-build/Group-4/Redis/Dockerfile .
docker run -d --name=single_redis_container -p 6379:6379 single_redis

# build and run rabbitMQ
echo "Building RabbitMQ"
docker build -t single_rabbitmq -f Docker-assessment/Chapter-8/single-build/Group-4/RabbitMQ/Dockerfile .
docker run -d --name=single_rabbitmq_container -p 5672:5672 single_rabbitmq

# build and run fastapi
echo "Building FastAPI"
docker build -t single_fastapi -f Docker-assessment/Chapter-8/single-build/Group-4/fastapi/Dockerfile .
docker run -d --name=single_fastapi_container -p 8000:8000 single_fastapi
