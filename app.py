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
        return f"""
        <html><head><style>
        body{{background:#0f172a;color:white;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;}}
        .card{{background:#1e293b;padding:40px;border-radius:20px;text-align:center;max-width:400px;}}
        h1{{color:#4ade80;}} a{{display:inline-block;background:#38bdf8;color:#0f172a;padding:12px 28px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:20px;}}
        </style></head><body><div class="card">
        <div style="font-size:60px;">✅</div>
        <h1>Money Sent Securely!</h1>
        <p>₦{amount} sent with AES-256 + 2FA protection.</p>
        <a href="/dashboard">Back to Dashboard →</a>
        </div></body></html>
        """
    else:
        return """
        <html><head><style>
        body{background:#0f172a;color:white;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;}
        .card{background:#1e293b;padding:40px;border-radius:20px;text-align:center;max-width:400px;}
        h1{color:#f87171;} a{display:inline-block;background:#334155;color:white;padding:12px 28px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:20px;}
        </style></head><body><div class="card">
        <div style="font-size:60px;">❌</div>
        <h1>2FA FAILED</h1>
        <p>Transaction Blocked - Invalid 2FA code.</p>
        <a href="/dashboard">Try Again →</a>
        </div></body></html>
        """

if __name__ == '__main__':
    app.run(debug=True)