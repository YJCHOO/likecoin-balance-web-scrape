from flask import Flask 
from flask import request
from webscrape import *

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/wallet', methods=['GET'])
def getBalance():
    cosmosWalletAddress = request.args.get('address')
    balance = scrapeBalance(cosmosWalletAddress)
    return {
        "balance" : balance
    }

app.run(host='0.0.0.0', port=5000)