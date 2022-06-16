import ed25519,time

st=time.time()
privKey, pubKey = ed25519.create_keypair()
end=time.time()
print("\nTime Taken for Generation : ",end-st)
print("Private key (32 bytes):", privKey.to_ascii(encoding='hex'))
print("Public key (32 bytes): ", pubKey.to_ascii(encoding='hex'),'\n')

msg = b'Message for Ed25519 signing'

st=time.time()
signature = privKey.sign(msg, encoding='hex')
end=time.time()
print("Time Taken to generate signature:",end-st)
print("Signature (64 bytes):", signature,'\n')

st=time.time()
try:
    pubKey.verify(signature, msg, encoding='hex')
    print("The signature is valid.")
except:
    print("Invalid signature!")
end=time.time()
print("Time Taken to verify:",end-st)