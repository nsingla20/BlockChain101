from crypt import methods
from flask import Flask, jsonify, request
from urllib.parse import urlparse

import requests
app = Flask(__name__)
nodes=set()
@app.route('/ping',methods=['POST'])
def add_node():
    values=request.get_json()
    
    port=values.get('port')
    for node in nodes:
        requests.post(f"http://{node}/nodes/register",json={'nodes':[request.remote_addr+":"+port]})
    
    
    nodes.add(request.remote_addr+":"+port)
    
    
    
    return "Host "+request.remote_addr+":"+port+" added to network",200

@app.route("/nodes",methods=['GET'])
def get_nodes():
    res={'nodes':list(nodes)}
    return res,200

@app.route('/transaction',methods=['POST'])
def transsac():
    values=request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    
    data={
        'sender':values['sender'],
        'recipient':values['recipient'],
        'amount':values['amount'],
    }
    
    for node in nodes:
        requests.post(f"http://{node}/transactions/new",json=data)
    
    return "Transaction Broadcasted",200

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
    
