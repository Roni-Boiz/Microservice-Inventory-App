from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host="redis-16197.c264.ap-south-1-1.ec2.redns.redis-cloud.com",
    port=16197,
    password="36SxrwBNrWzliQ8ml7Rv9Gj1BDgQ0v0z",
    decode_responses=True
)

redis_payment = Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get("/products")
def all():
    return [format(pk) for pk in Product.all_pks()]

def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }

@app.post("/products")
def create(product: Product):
    return product.save()

@app.get("/products/{pk}")
def get(pk: str):
    return Product.get(pk)

@app.delete("/products/{pk}")
def delete(pk: str):
    product = Product.get(pk)
    return Product.delete(pk)