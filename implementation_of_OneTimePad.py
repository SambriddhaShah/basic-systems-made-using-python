   

message=15;
key=19;

def encryption(message,key):
    encrypt=message ^  key
    return encrypt
print(encryption(message,key));
 
def decryption(encrypt=encryption(message,key), key=key):
    decrypt=encrypt^ key
    return decrypt
print(decryption());


 