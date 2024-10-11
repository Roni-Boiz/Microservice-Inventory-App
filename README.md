# Microservice Inventory Application
Python microservice application with 2 frontends, 2 redis databases, and 4 microservices.

### Pre-requisite

1. Redis Account: Create an account in [Redis](https://redis.io/)
2. Install Python3 and Docker


#### Setup Development Environment
```bash
# backend-inventory
$ cd inventory
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# backend-payment
$ cd payment
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# frontend-inventory
$ cd frontend/inventory
$ npm install

# frontend-inventory
$ cd frontend/purchase
$ npm install
```

#### Create databases

##### 1. Redis_1: redis-inventory-db
Create new database in your redis account then update the host, port and password in `inventory/main.py` and `payment/main.py`

##### 1. Redis_2: redis-payment-db
Create new database in docker
```bash
$ docker run -d --name redis-payment-db -p 6379:6379  redis/redis-stack-server:latest
```


#### Run the Application
```bash
# backend-inventory
$ cd inventory
$ uvicorn main:app --reload --port 8000
$ python3 consumer.py

# backend-payment
$ cd payment
$ uvicorn main:app --reload --port 8000
$ python3 consumer.py

# frontend-inventory
$ cd frontend/inventory
$ npm start

# frontend-inventory
$ cd frontend/purchase
$ npm start
```

#### Application Endpoints


