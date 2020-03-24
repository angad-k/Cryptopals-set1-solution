from binascii import unhexlify, b2a_hex
import base64
import array as arr

def main():
    Stanza = open('ShakespeareKaBaap.txt').read().splitlines()
    k = 1
    #k is used to iterate over ICE. 
    for line in Stanza:
        string3 = ""
        for i in range(0, len(line)):
            if(k == 1):
                string3 += chr(ord(line[i])^ord("I"))
                k = 2
            elif(k == 2):
                string3 += chr(ord(line[i])^ord("C"))
                k = 3
            elif(k == 3):
                string3 += chr(ord(line[i])^ord("E"))
                k = 1
        print(b2a_hex(string3))

if __name__== "__main__":
  main()
       


