from binascii import unhexlify
import base64
byte_seq = unhexlify("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
print(byte_seq)
print(base64.b64encode(byte_seq))
