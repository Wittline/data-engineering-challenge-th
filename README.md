# Dockerizing a Python Script for Web Scraping and consume the scraped data using FastApi

This repository aims to show you how to dockerize a Python script for web scraping, store the scraped data in a sqlite database and consume the scraped data using a FastApi app, everything in the same container, you can modify this repository and repeatthe same example but using different docker containers for each app.

## Docker environment
![image](https://user-images.githubusercontent.com/8701464/144087110-fc3589bd-f4f2-461d-9e7a-90f6ad9d3a23.png)


## Dockerfile

![carbon (27)](https://user-images.githubusercontent.com/8701464/144100115-e3e89bb2-a7e8-47a7-a2d3-d53acc17b796.png)

## Details
The project consists of two processes:

1. A Python script that is executed when the docker image is created, this script will be responsible for scraped the data from the website: www.metrocubicos.com and will store the data in a sqlite database, the script is in the file **publications.py** and receives the following arguments as parameters: **python publicaciones.py -t 50  -s 48**, **-t** indicates the number of total elements to be scraped from the web site, and the parameter **-s** indicates the number of elements per page that the web site contains, this last parameter is not needed, by default it is using the number 48, if site´s structure changes in the future so this parameter can be changed at your convenience. the dockerfile file will be in charge of running the command: **RUN python -u ./app/publicaciones.py -t 50 -s 48** when Docker Image is built.

![image](https://user-images.githubusercontent.com/8701464/144090544-768621be-5b97-4e5f-970a-acd7b0d9dcff.png)


2. Once the Docker image was built, the FastApi app will be initialized, the dockerfile file is in charge of running the command: **CMD ["python", "./app/main.py"]**, this exposes a service, you can try to call it by localhost as follows:  **http://127.0.0.1:8000/items/2**, this example returns two records stored in the database **metroscubicos.sqlite** in the **ESTATE** table.

![image](https://user-images.githubusercontent.com/8701464/144091524-98a49806-c35a-4bfb-b1c5-4546ba555de5.png)

## How to run

In order to make this example work correctly please follow the next steps:

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

- Ready!. Web scraping process was executed and the fastApi App exposed, lets try looking into this url:: **http://127.0.0.1:8000/items/2**

- If you want stop everything, go and open another gitbash windows and use the below command:

``` 
ramse@DESKTOP-K6K6E5A MINGW64 ~/documents/github/data-engineering-challenge-th
docker container ls 
```
- Now use the below command using the **CONTAINER ID** shown in the last step, this will stop everything:
``` 
ramse@DESKTOP-K6K6E5A MINGW64 ~/documents/github/data-engineering-challenge-th
docker stop 7f2181fe515d
```
- If you want to release your resources, then you can use the below command, this will delete everything:

``` 
ramse@DESKTOP-K6K6E5A MINGW64 ~/documents/github/data-engineering-challenge-th
docker system prune -a
```


