alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','e','s','t',
          'u','v','x','y','z']

def encryption(plain_text, shift_key) : 
    cipher_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_key
        cipher_text +=alphabet[new_position]
    print(f"Here's is the text after encryption {cipher_text}")   

what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
text = input("Type your message:\n")
key = int(input("Enter shif key:\n"))
if what_to_do == "encrypt" :
    encryption(plain_text=text, shift_key = shift)
elif what_to_do == "decrypt" :
    decryption(text,shift)