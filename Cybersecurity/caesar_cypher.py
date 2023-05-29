#!/usr/bin/env python3

# A Caesar cypher is a simple encryption technique named after Julius Caesar.
# It works by shifting each letter in the plaintext a fixed number of positions
# up or down the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B'
# becomes 'E', and so on. The shift wraps around the alphabet, so 'Z' becomes 'C'.
# The same shift value is used for both encryption and decryption.

# While the Caesar cypher is easy to understand and implement, it is considered
# extremely weak from a security perspective. It can be easily broken by trying
# all possible shift values or using frequency analysis.

# I wrote this script to dip my toe back into the cryptography field. Although I 
# have some past experience with cryptography, it's been a while, and I want to 
# refresh and strengthen my foundational knowledge.
# Additionally, I'm a massive fan of Escape Rooms, and a particular brand I played
# often used the Caesar cipher. I like the idea of using Python to solve even 
# mundane problems.
# Finally, this is one of the most commonly used ciphers in CTF challenges in Cybersecurity.


import sys

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_user_choice():
    # Prompt the user to choose between encryption, decryption, or quitting.

    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        print('Or press (q) to quit.')
        user_input = input('> ').lower()
        if user_input.startswith('e'):
            return 'encrypt'
        elif user_input.startswith('d'):
            return 'decrypt'
        elif user_input.startswith('q'):
            print('Quitting, bye.')
            sys.exit()
        print('Please enter the letter e, d, or q.')

def get_shift_key():
    #Prompt the user to enter the shift key for encryption or decryption.

    max_key = len(SYMBOLS) - 1
    while True:
        print(f'Please enter the key (0 to {max_key}) to use.')
        user_input = input('> ').upper()
        if user_input.isdecimal() and 0 <= int(user_input) < len(SYMBOLS):
            return int(user_input)

def get_message(mode):
    # Prompt the user to enter the message to encrypt or decrypt.

    print(f'Enter the message to {mode}')
    return input('> ').upper()

def encrypt_decrypt_message(message, key, mode):
    """
    Encrypt or decrypt the given message using the Caesar cypher algorithm.

    Args:
        message (str): The message to encrypt or decrypt.
        key (int): The shift key for encryption or decryption.
        mode (str): The chosen mode ('encrypt', 'decrypt').

    Returns:
        str: The encrypted or decrypted message.
    """
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # Get the index of the symbol
            if mode == 'encrypt':
                num = (num + key) % len(SYMBOLS)
            elif mode == 'decrypt':
                num = (num - key) % len(SYMBOLS)
            translated += SYMBOLS[num]
        else:
            translated += symbol
    return translated

def caesar_cypher():
    # The user is prompted to choose between encryption, decryption, or quitting.
    # Then, the user is asked for the shift key and the message to encrypt or decrypt.
    # Finally, the script performs the encryption or decryption and displays the result.

    print()
    print('The Caesar Cipher is a substitution cypher that')
    print('encrypts letters by shifting them up or down the')
    print('alphabet by a key number of positions.')
    print()

    mode = get_user_choice()
    key = get_shift_key()
    message = get_message(mode)
    translated = encrypt_decrypt_message(message, key, mode)

    print(translated)

if __name__ == '__main__':
    caesar_cypher()
