from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from redis import Redis
from redis_om import get_redis_connection, HashModel, Field
from starlette.requests import Request
import requests, time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3001'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

redis_backend = get_redis_connection(
    host="redis-11160.c8.us-east-1-4.ec2.redns.redis-cloud.com",
    port=11160,
    password="jk8tyl5E1p3hDpsLL6o3z7ba9B4dwaxk",
    decode_responses=True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str

    class Meta:
        database = redis

@app.get("/orders/{pk}")
def get(pk: str):
    return Order.get(pk)

@app.post("/orders")
async def create(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()

    req = requests.get('http://localhost:8000/products/%s' % body['id'])
    product = req.json()

    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2 * product['price'],
        quantity=body['quantity'],
        total=1.2 * product['price'],
        status='pending'
    )
    order.save()

    background_tasks.add_task(order_completed, order)

    return order

def order_completed(order: Order):
    time.sleep(5)
    redis_backend.xadd('order_completed', order.dict(), '*')
    order.status = 'completed'
    order.save()