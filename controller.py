
import requests

main_server="http://localhost:5000"

nodes=requests.get(main_server+"/nodes").json().get('nodes')

print("Nodes in network : "+str(nodes))
while True:
    sender=int(input("Sender (index from above list):"))
    rec=int(input("Recipient (Public Key) :"))
    amt=int(input("Amount:"))
    rec=requests.get("http://"+nodes[rec]+"/pk").json().get('pk')
    requests.post("http://"+nodes[sender]+"/pay",json={'recipient':rec,'amount':amt})
    
    
    
