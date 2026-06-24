from flask import Flask, render_template, redirect, request, jsonify
import requests

server = Flask(__name__)

@server.route('/')
def main():
    return render_template('checkout.html')

@server.route('/submit', methods = ['POST'])
def send():
    user_name = request.form['user_input']
    return jsonify(status ='good',
                   user = user_name 
                   )

@server.route('/create_payment', methods = ['POST'])
def payment():
    data = request.form
    username = data.get('username')
    phone = data.get('phone')
    address = data.get('address')
    payment_method = data.get('payment_method')

    if payment_method == 'cod':
        return jsonify(
            status = 'success',
            method = 'cod',
            message = f'''thank you {username}({phone}) for buying our product
            {address}'''
        )

    payload = {
            "accountNo": "11223344",
            "accountName": "FOOD MVP STORE",
            "acqId": "970415",
            "amount": 50000,
            "addInfo": f"Order from {phone}",
            "template": "qr_only"
    }

    respons = requests.post("https://api.vietqr.io/v2/generate", json= payload)
    api_data = respons.json()
    qr_code_url = api_data.get('data', {}).get('qrDataURL')

    return jsonify(status = 'chill',
                   method = 'viettqr',
                   code_url = qr_code_url), redirect('/')

if __name__ == '__main__':
    server.run(debug=True)