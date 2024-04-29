import pika
import redis
from minio import Minio

def connect_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq-svc", port=5672, virtual_host="/", credentials=pika.PlainCredentials("admin","admin")))
    channel = connection.channel()
    return channel

def connect_redis():
    return redis.Redis(host='redis-svc', port=6379, db=0)

def connect_minio():
    return Minio(
        endpoint="minio-svc:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False)