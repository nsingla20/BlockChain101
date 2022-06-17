import requests
from nacl.public import PrivateKey, SealedBox, PublicKey
from nacl.signing import SigningKey, VerifyKey
from nacl.encoding import HexEncoder

skbob = SigningKey.generate()
pkbob = skbob.verify_key


signk=skbob.to_curve25519_private_key()
vk=signk.public_key

en1=str(vk.encode(encoder=HexEncoder).decode('utf-8'))
en2=str(pkbob.to_curve25519_public_key().encode(encoder=HexEncoder).decode('utf-8'))



# print(str(pkbob))
# print(vk.encode(encoder=HexEncoder))
# print(pkbob==vk)

print(en1)
print(en2)