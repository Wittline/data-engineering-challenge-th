FROM python:3.7.9

WORKDIR /TH-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

RUN python -u ./app/publicaciones.py -t 50 -s 48

CMD ["python", "./app/main.py"]

#docker build -t python-th . --progress=plain
#docker run -p 8000:8000 python-th