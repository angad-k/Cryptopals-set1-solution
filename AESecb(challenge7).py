from Crypto.Cipher import AES
import base64
# This is pretty self explanatory.
cipher = base64.b64decode(open('aesECBencoded.txt').read())
obj = AES.new(b'YELLOW SUBMARINE', AES.MODE_ECB)
print(obj.decrypt(cipher))