# Dockerizing a Python Script for Web Scraping and consume the scraped data using FastApi

This repository aims to show you how to dockerize a Python script for web scraping, store the scraped data in a sqlite database and consume the scraped data using a FastApi app, everything in the same container, you can modify this repository and repeatthe same example but using different docker containers for each app.

## Docker environment
![image](https://user-images.githubusercontent.com/8701464/144087110-fc3589bd-f4f2-461d-9e7a-90f6ad9d3a23.png)

## Details
El proyecto consta de dos procesos:

1. Un script de Python que se executa cuando se crea la imagen de docker, este script sera responsable de extraer la informacion del sitio web: www.metroscubicos.com y almacenar los datos extraidos en una base de datos sqlite, el script esta en el archivo **publicaciones.py** y recibe como parametros los siguientes argumentos:

**python publicaciones.py -t 50  -s 48**, **-t** indica la cantidad elementos totales que se quieren extraer del sitio, y el parametro *-s* indiga la cantidad de elementos por pagina que contiene el sitio, este ultimo parametrp no es necesario usarlo, por defecto esta usando el numero 48, si la estructura del sitio cambia se puede cambiar a conveniencia.

el archivo docker file se encarga de corer el comando **RUN python -u ./app/publicaciones.py -t 50 -s 48** cuando se construye la imagen de docker.

![image](https://user-images.githubusercontent.com/8701464/144090544-768621be-5b97-4e5f-970a-acd7b0d9dcff.png)


2. Una vez que la imagen docker se construyó, se inicializa la app de FastApi, el archivo dockerfile se encarga de correr el comando: **CMD ["python", "./app/main.py"]**, api expone un servicio, puedes intentar llamarlo por localhost de la siguiente manera:  **http://127.0.0.1:8000/items/2**, este ejemplo retorna dos registros almacenados en la base de datos **metroscubicos.sqlite** en la tabla **ESTATE**.

![image](https://user-images.githubusercontent.com/8701464/144091524-98a49806-c35a-4bfb-b1c5-4546ba555de5.png)

## How to run
