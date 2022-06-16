
import requests

main_server="http://localhost:5000"

nodes=requests.get(main_server+"/nodes").json().get('nodes')

print("Nodes in network : "+str(nodes))
while True:
    sender=int(input("Sender:"))
    rec=int(input("Recipient:"))
    amt=int(input("Amount:"))
    requests.post("http://"+nodes[sender]+"/pay",json={'recipient':nodes[rec],'amount':amt})
    
