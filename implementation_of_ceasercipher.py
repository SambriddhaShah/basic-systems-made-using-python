
#           # Encryption
def encrypt(message='CRYPTOCURRENCY',key=3):
    cipher_text=''
    for char in message:
        if char==' ':
            char=char
            cipher_text=cipher_text + char

        elif char.isupper():    
            s=ord(char)
            char= ((s+key-65)%26+65)
            char=chr(char)
            cipher_text=cipher_text + char
    
        else:    
            s=ord(char)
            char= ((s+key-97)%26+97)
            char=chr(char)
            cipher_text=cipher_text + char
    return cipher_text    
print(f'The cipher text of given message after encryption process  is {encrypt()}')




            # Decryption
def decrypt(message=encrypt(),key=3):
        plain_text=''
        for char in message:
            if char==' ':
                char=char
                plain_text=plain_text + char

            elif char.isupper():    
                s=ord(char)
                char= ((s-key-65)%26+65)
                char=chr(char)
                plain_text=plain_text + char
                
            else:    
                s=ord(char)
                char= ((s-key-97)%26+97)
                char=chr(char)
                plain_text=plain_text + char
        
        print(f'The plain text after decryption process is {plain_text}')    
decrypt()
