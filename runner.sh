#!/bin/sh
MY_SQL_PASSWORD="test"
sudo docker pull mysql/mysql-server:latest && \
            sudo docker run -p 3306:3306 --name pumpkin-mysql -e MYSQL_ROOT_PASSWORD=${MY_SQL_PASSWORD} -d mysql&& \
DOCKER_IP="$(sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pumpkin-mysql)"
echo "Waitting for MySQL container to set up it will take about 4 minutes"
sleep 4m
export EGOR_PUMPKIN_DB_IP=${DOCKER_IP}
export EGOR_PUMPKIN_DB_PASSWORD=${MY_SQL_PASSWORD}
python insert_random_pets.py
npx serverless offline start