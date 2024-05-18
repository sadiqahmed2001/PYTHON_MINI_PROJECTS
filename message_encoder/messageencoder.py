# Example usage of the Secret Message Encoder/Decoder program

# User inputs their message
message = input("Enter your secret message: ")

# User selects encryption technique
encryption_method = input("Choose encryption method (Caesar/Vigenère/Substitution): ")

# Depending on the encryption method chosen, perform encoding or decoding
if encryption_method.lower() == 'caesar':
    shift = int(input("Enter the shift value for Caesar cipher: "))
    # Encode message using Caesar cipher
    encoded_message = caesar_cipher_encode(message, shift)
    print("Encoded Message:", encoded_message)
elif encryption_method.lower() == 'vigenère':
    keyword = input("Enter the keyword for Vigenère cipher: ")
    # Encode message using Vigenère cipher
    encoded_message = vigenere_cipher_encode(message, keyword)
    print("Encoded Message:", encoded_message)
elif encryption_method.lower() == 'substitution':
    # Encode message using Substitution cipher
    encoded_message = substitution_cipher_encode(message)
    print("Encoded Message:", encoded_message)
else:
    print("Invalid encryption method. Please choose from Caesar, Vigenère, or Substitution.")
