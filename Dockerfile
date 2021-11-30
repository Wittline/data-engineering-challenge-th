FROM python:3.7.9

WORKDIR /TH-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD python publicaciones.py -t 50 -s 48 ; python main.py