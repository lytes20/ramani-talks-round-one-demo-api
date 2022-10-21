from flask import Flask, request

app = Flask(__name__)

orders = [{"product_name": "Ukwaju", "quantity": 10},
          {"product_name": "Tanga Fresh Maziwa", "quantity": 10}]

saved_password = "HakunaMatata"


@app.route("/")
def hello_world():
    return "Hakuna Matata"


@app.get("/api/login")
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if saved_password == password:
        return {"message" : "Login successful"}, 200
    return {"message" : "Invalid Credentials"}, 401

@app.get("/api/orders")
def get_orders():
    return {"orders" : orders}
