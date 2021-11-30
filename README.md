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


2. Una vez que la imagen docker se construyó o el proceso build terminó, se inicializará la app de FastApi, el archivo dockerfile se encarga de correr el comando: **CMD ["python", "./app/main.py"]**,esto expone un servicio, puedes intentar llamarlo por localhost de la siguiente manera:  **http://127.0.0.1:8000/items/2**, este ejemplo retorna dos registros almacenados en la base de datos **metroscubicos.sqlite** en la tabla **ESTATE**.

![image](https://user-images.githubusercontent.com/8701464/144091524-98a49806-c35a-4bfb-b1c5-4546ba555de5.png)

## How to run

Para hacer funcionar el ejemplo sigue los siguientes pasos:

- Install <a href="https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/">git-bash for windows</a>, once installed , open **git bash** and download this repository, this will download the **app** folder and the **Dockerfile** file, and other files needed.

``` 
ramse@DESKTOP-K6K6E5A MINGW64 /c/documents/github
$ git clone https://github.com/Wittline/data-engineering-challenge-th.git
```

- Install <a href="https://docs.docker.com/docker-for-windows/install/">Docker Desktop on Windows</a>, it will install **docker compose** as well, docker compose will alow you to run multiple containers applications.

- Once all the files needed were downloaded from the repository , Let's run everything we will use the git bash tool again, go to the folder **data-engineering-challenge-th** we will run the Dockerfile using the command:

``` 
ramse@DESKTOP-K6K6E5A MINGW64 ~/documents/github/data-engineering-challenge-th
docker build -t python-th . --progress=plain
```
![image](https://user-images.githubusercontent.com/8701464/144094340-2ddea8ce-8095-4e27-a9ba-6f67402c9f49.png)

- Once the above command was executed and finished, proceed with the container creation using the image: **python-th** and then start the container, using the below command:

``` 
ramse@DESKTOP-K6K6E5A MINGW64 ~/documents/github/data-engineering-challenge-th
docker run -p 8000:8000 python-th
```

![image](https://user-images.githubusercontent.com/8701464/144096285-a0eda402-8a63-4483-a9c7-7f2e7b47dffe.png)

- READY, the web scrapping process ws executed and the api exposed, lets try looking into this url: **http://127.0.0.1:8000/items/2**

