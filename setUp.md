befor rannig container do this command

1) run this commande en terminal

sysctl -w vm.max_map_count=262144

if you work on a server i don't know if is necessary

2)run en terminal

docker-compose build

3) run en terminal

docker-compose up -d

docker ps

docker inspect id_of_mongo_image

copy the IPAddress and set it in replicaset.sh and run replicaset.sh

./replicaset.sh

on terminal you shoulf see => replica set created

docker-compose down

4)run en terminal

docker-compose up

finally .......
