from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding
import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.serialization import PublicFormat,PrivateFormat
private_key = Ed25519PrivateKey.generate()
print(private_key.private_bytes(Encoding.PEM,PrivateFormat.PKCS8,serialization.NoEncryption()))
signature = private_key.sign(b"my authenticated message")
public_key = private_key.public_key()
public_key.verify(signature, b"my authenticated message")