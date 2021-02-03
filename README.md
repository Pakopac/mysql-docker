# MYSQL Docker

## Le Dockerfile

```Dockerfile
# On récupère la dernière version de l'image mysql
FROM mysql:latest

# On met la bdd dans le entry point qui l'initialise
COPY ./bdd.sql /docker-entrypoint-initdb.d

# On crée une variable environnement avec le nom de la base
ENV MYSQL_DATABASE classmodels

# On l'expose sur le port 3306
EXPOSE 3306 
```

## Build de l'image
```
docker build -t mysql-test:01 .
```

## Run du container
```
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root --name=mysql-test mysql-test:01
```

## Exec (pour aller sur le container)
```
sudo docker exec -it mysql-test mysql -uroot -p
```

## Tester la base (sur le container)
```
SHOW DATABASES;
USE classicmodels;
SHOW TABLES;
```

## Créer un user avec les privilèges
```
CREATE USER 'lilian'@'%' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'lilian'@'%' WITH GRANT OPTION;
```
pour se connecter avec le nouveau user:
```
sudo docker exec -it mysql-test mysql -u lilian -p
```

## Delete un user
```
DROP USER 'lilian'@'%';
```