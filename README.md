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

##### Frontend
![app-1](https://github.com/user-attachments/assets/b078d66b-64b2-47c5-bcad-0edf9ed3822c)

![app-2](https://github.com/user-attachments/assets/d4523842-8ac0-465d-936f-4ec907f6a984)

![app-3](https://github.com/user-attachments/assets/e3ae96dd-2aa1-4ef4-a613-5aaeb84a57eb)

![app-4](https://github.com/user-attachments/assets/b03f7070-d872-46d9-a727-89eafe409374)

![app-5](https://github.com/user-attachments/assets/a2442605-2c2d-4330-b518-b8e2f74ab8a3)

![app-6](https://github.com/user-attachments/assets/88bd1d79-bb77-4c50-902c-fc7aa2f90983)

##### APIs

###### Products
1. Get
![products-get](https://github.com/user-attachments/assets/a9ef8f3d-2368-4315-a320-7d036e4bae23)

2. Get All
![products-getall](https://github.com/user-attachments/assets/593befa3-b46b-4bf2-9756-b408ce09d611)

3. Post
![products-post](https://github.com/user-attachments/assets/6cc1af10-fcde-4f83-a70f-d8c76762f622)

4. Delete
![products-delete](https://github.com/user-attachments/assets/eadb0d44-97d6-4480-be24-d97e86ac1f20)

###### Orders
1. Get
![orders-get](https://github.com/user-attachments/assets/0a7dfc26-0146-46ef-b29b-8b379863b4ba)

2. Post
![orders-post](https://github.com/user-attachments/assets/68cea2a0-bdf6-41c1-b2a2-2d6d84fb2e6b)

###### Consumers
1. Inventory
![inventory-consumer](https://github.com/user-attachments/assets/22df8087-0936-4e4f-bcd9-d4d3542e73f4)

2. Payment
![payment-consumer](https://github.com/user-attachments/assets/5dc73c31-429e-4aa2-a5f3-a9dcf4d3d763)
