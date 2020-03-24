from binascii import unhexlify, b2a_hex
import base64

string1 = unhexlify("1c0111001f010100061a024b53535009181c")
string2 = unhexlify("686974207468652062756c6c277320657965")
#converted both strings from hex to ascii
string3 = ""
for i in range(0, len(string1)):
    string3 += chr(ord(string1[i])^ord(string2[i]))
# ord() returns the unicode value of characters   
print(string3)