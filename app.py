import blockchain
from flask import Flask, request
import requests
import simplejson as json

app = Flask(__name__)
blockchain = blockchain.Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

@app.route('/pay', methods=['post'])
def pay():
    index = blockchain.add_new_transaction(request.get_json())
    return json.dumps({"index": index })

@app.route('/mine', methods=['post'])
def mine():
    index = blockchain.mine()
    return json.dumps({"index": index })

app.run(debug=True, port=5000)