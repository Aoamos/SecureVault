from flask import Flask, render_template, request, redirect
from models import Wallet
from security import encrypt_data, generate_2fa_code

app = Flask(__name__)

# Fake user for now
my_wallet = Wallet(user="test_user")

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # This gets live crypto price (free API)
    return render_template('dashboard.html', naira=my_wallet.naira_balance, usdt=my_wallet.usdt_balance)

@app.route('/send', methods=['POST'])
def send_money():
    amount = request.form.get('amount')
    code_2fa = request.form.get('code')
    # here we check 2FA before sending - This is our secuirty feature
    if code_2fa == '12345': # We will replace with real Google Auth later 
        my_wallet.send(amount)
        return "Money sent securely!"
    else:
        return "2FA FAILED - Transaction Blocked"

if __name__ == '__main__':
    app.run(debug=True)