FROM python:3.11.9-alpine3.19

WORKDIR /app

COPY t-producer.py transaction.json requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5050

ENTRYPOINT [ "/usr/local/bin/python3" ]