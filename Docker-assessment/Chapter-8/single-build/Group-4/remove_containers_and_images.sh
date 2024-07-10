# stop and remove postgres container and image
docker stop single_postgres_container
docker rm single_postgres_container
docker rmi single_postgres

# stop and remove MySQL container and image
docker stop single_mysql_container
docker rm single_mysql_container
docker rmi single_mysql

# stop and remove redis container and image
docker stop single_redis_container
docker rm single_redis_container
docker rmi single_redis

# stop and remove rabbitmq container and image
docker stop single_rabbitmq_container
docker rm single_rabbitmq_container
docker rmi single_rabbitmq

# stop and remove fastapi container and image
docker stop single_fastapi_container
docker rm single_fastapi_container
docker rmi single_fastapi

