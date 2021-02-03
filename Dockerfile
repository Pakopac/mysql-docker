FROM mysql:latest

COPY ./bdd.sql /docker-entrypoint-initdb.d

ENV MYSQL_DATABASE classmodels

EXPOSE 3306