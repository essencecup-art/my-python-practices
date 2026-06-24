# PROJECT BLUEPRINT: FOOD ORDERING MVP
# - Frontend: HTML / Asynchronous JavaScript Fetch API (Dynamic states/Animations)
# - Backend: Python Flask
# - Core Focus: Checkout loop connecting to VietQR/PayOS API
# - Status: Core logic done, moving to checkout integration
import os
import requests
from flask import Flask, redirect, render_template, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
server.secret_key = 'super_secret_key_ahh'
base_dir = os.path.abspath(os.path.dirname(__file__))
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'instance', 'menu.db')
db = SQLAlchemy(server)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dish_name = db.Column(db.String(75), nullable = False, unique = True)
    pricing = db.Column(db.Integer, nullable = False)
    category = db.Column(db.String(30), nullable = False)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def __repr__(self):
        return f'dish number {self.id}'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    items_summary = db.Column(db.String(500), nullable=False)
    total = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default="Pending")

    def __repr__(self):
        return f' order {self.id}'
    
    
@server.route('/checkout')
def loading():
    return render_template('checkout.html')

@server.route('/create_payment', methods = ['POST'])
def create():
    data = request.form
    fullname = data.get('fullname')
    phone = data.get('phone')
    address = data.get('address')
    payment = data.get('payment_method')

    api_url = "https://api.vietqr.io/v2/generate"

    payload = {
        "accountNo": "1133224455",       
        "accountName": "FOOD MVP STORE",  
        "acqId": "970415",                
        "amount": 50000,                  
        "addInfo": f"Order from {phone}", 
        "template": "qr_only"
    }

    response = requests.post(api_url, json= payload)
    api_data = response.json()

    qr_code_url = api_data.get('data', {}).get('qrDataURL')

    return jsonify({
        "status":"success",
        'method':'vietqr',
        'qr_url': qr_code_url
    })
        



@server.route('/menu')
def menu():
    available_dishes = Menu.query.filter(Menu.available == True).all()
    return render_template('menu.html', menu = available_dishes)

@server.route('/menu/add/<int:id>', methods = ['POST'])
def add_to_cart(id):
    cart = session.get('cart',{})
    dish_id = str(id)

    if dish_id in cart:
       cart[dish_id] += 1
    else:
        cart[dish_id] = 1

    session['cart'] = cart
    # cart = session.get('cart',[])
    # cart.append(id)
    # session['cart']= cart
    return jsonify({"status": "success", "total_items": sum(cart.values())})

@server.route('/cart')
def view_cart():
    cart = session.get('cart',{})
    display = []
    total_price = 0

    for dish_id, quantity in cart.items():
        dish_name = Menu.query.get(int(dish_id))
        if dish_name:
            item_total = dish_name.pricing * quantity
            total_price += item_total

        display.append({
            'dish':dish_name,
            'quantity': quantity
        })
    # for dish in cart:
    #     dish_name = Menu.query.get(dish)
    #     display.append(dish_name)
    #     total_price += dish_name.pricing

    return render_template('cart.html', cart =display, price =total_price)

@server.route('/menu/remove/<int:id>', methods = ['POST'])
def remove_from_cart(id):
    cart = session.get('cart',{})
    dish_id = str(id)
    if dish_id in cart:
        del cart[dish_id]

    session['cart'] = cart
    return redirect('/cart')

@server.route('/menu/decrease/<int:id>', methods = ['POST'])
def decrease(id):
    cart = session.get('cart',{}) 
    dish_id =str(id)
    if dish_id in cart:
        if cart[dish_id] > 1:
            cart[dish_id] -= 1
        else:
            del cart[dish_id]

    session['cart'] = cart
    return redirect('/cart')

@server.route('/checkout', methods = ['POST'])
def check_out():
    cart = session.get('cart', {})
    if not cart:
        return redirect('/cart')
    display =[]
    total_price = 0

    for dish_id, quantity in cart.items():
        dish_row = Menu.query.get(int(dish_id))
        total_price += dish_row.pricing * quantity
        display.append(f'{dish_row.dish_name} x {quantity}')

    summary =', '.join(display)

    check_out = Order(items_summary = summary, total = total_price)

    db.session.add(check_out)
    db.session.commit()
    session['cart'] = {}

    return redirect('/admin')


@server.route('/admin')
def show_checkout():
    all_order = Order.query.all()

    return render_template('admin.html', orders = all_order)

if __name__ == '__main__':
    
    # with server.app_context():
    #     db.create_all()

        # dummy_menu = [
        #         {"dish_name": "Truffle Fries", "pricing": 850, "category": "Appetizer", "available": True},
        #         {"dish_name": "Crispy Calamari", "pricing": 1300, "category": "Appetizer", "available": True},
        #         {"dish_name": "Smash Burger", "pricing": 1599, "category": "Main", "available": True},
        #         {"dish_name": "Ribeye Steak", "pricing": 3450, "category": "Main", "available": False},
        #         {"dish_name": "New York Cheesecake", "pricing": 750, "category": "Dessert", "available": True},
        #         {"dish_name": "Iced Matcha Latte", "pricing": 550, "category": "Drink", "available": True}
        #     ]
        # for dish in dummy_menu:
        #     new_dish = Menu(dish_name = dish['dish_name'],
        #                     pricing = dish['pricing'],
        #                     category = dish['category'],
        #                     available = dish['available'])
        #     db.session.add(new_dish)
    
    # db.session.commit()

    server.run(debug=True)
                        

    