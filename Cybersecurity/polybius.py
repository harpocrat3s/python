#!/usr/bin/env python3

"""
Polybius Square (also known as the Polybius Checkerboard) is a simple
substitution cypher first described by the ancient Greek historian Polybius.
It's a way to encode letters into numbers and was used historically for telegraphy.

In its classical form, it's a 5x5 square filled with the letters of the alphabet
(usually excluding J, or merging I and J into the same cell), and then the position
of each letter is used as its code, represented by a pair of single-digit numbers,
the row and the column in which the letter is located.
"""

import sys

POLYBIUS_SQUARE = {
    'A': '11',   'N': '33',
    'B': '12',   'O': '34',
    'C': '13',   'P': '35',
    'D': '14',   'Q': '41',
    'E': '15',   'R': '42',
    'F': '21',   'S': '43',
    'G': '22',   'T': '44',
    'H': '23',   'U': '45',
    'I': '24',   'V': '51',
    ' ': ' ',    'W': '52',
    'K': '25',   'X': '53',
    'L': '31',   'Y': '54',
    'M': '32',   'Z': '55'
}

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

def get_message(mode):
    # Prompt the user to enter the message to encrypt or decrypt.
    # Please note that it will ignore accented letters, numbers and punctuation

    print(f'Enter the message to {mode}')
    return input('> ').upper()

def encrypt_decrypt_message(message, mode):
    """
    Encrypt or decrypt the given message using the polybius square cypher algorithm.

    Args:
        message (str): The message to encrypt or decrypt.
        mode (str): The chosen mode ('encrypt', 'decrypt').

    Returns:
        str: The encrypted or decrypted message.
    """
    translated = ''

    if mode == 'encrypt':
        for symbol in message:
            for key, value in POLYBIUS_SQUARE.items():
                if symbol == key:
                    translated += value + ' '

    if mode == 'decrypt':
    # This splits the message in words first, to keep track of the spaces
    # in the original message
        words = message.split('   ')
        for i, word in enumerate(words):
            letters = word.split()
            for letter in letters:
                for key, value in POLYBIUS_SQUARE.items():
                    if letter == value:
                        translated += key
            if i != len(words) - 1:
                translated += ' '

    return translated


def polybius():
    # The user is prompted to choose between encryption, decryption, or quitting.
    # Then, the user is asked for the message to encrypt or decrypt.
    # Finally, the script performs the encryption or decryption and displays the result.

    mode = get_user_choice()
    message = get_message(mode)
    translated = encrypt_decrypt_message(message, mode)

    print(translated)


if __name__ == '__main__':
    polybius()

