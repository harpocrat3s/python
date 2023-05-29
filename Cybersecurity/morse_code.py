#!/usr/bin/env python3

import sys

MORSE_CODE = {
    'A': '.-',     'N': '-.',     '0': '-----',
    'B': '-...',   'O': '---',    '1': '.----',
    'C': '-.-.',   'P': '.--.',   '2': '..---',
    'D': '-..',    'Q': '--.-',   '3': '...--',
    'E': '.',      'R': '.-.',    '4': '....-',
    'F': '..-.',   'S': '...',    '5': '.....',
    'G': '--.',    'T': '-',      '6': '-....',
    'H': '....',   'U': '..-',    '7': '--...',
    'I': '..',     'V': '...-',   '8': '---..',
    'J': '.---',   'W': '.--',    '9': '----.',
    'K': '-.-',    'X': '-..-',   ' ': ' ',
    'L': '.-..',   'Y': '-.--',
    'M': '--',     'Z': '--..'
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
    # Please note that it will ignore accented letters and punctuation

    print(f'Enter the message to {mode}')
    return input('> ').upper()

def encrypt_decrypt_message(message, mode):
    """
    Encrypt or decrypt the given message using the Morse code cypher algorithm.

    Args:
        message (str): The message to encrypt or decrypt.
        mode (str): The chosen mode ('encrypt', 'decrypt').

    Returns:
        str: The encrypted or decrypted message.
    """
    translated = ''

    if mode == 'encrypt':
        for symbol in message:
            for key, value in MORSE_CODE.items():
                if symbol == key:
                    translated += value + ' '

    if mode == 'decrypt':
    # This splits the message in morse code words first, to keep track of the spaces
    # in the original message
        words = message.split('   ')
        for i, word in enumerate(words):
            letters = word.split()
            for letter in letters:
                for key, value in MORSE_CODE.items():
                    if letter == value:
                        translated += key
            if i != len(words) - 1:
                translated += ' '

    return translated


def morse_code():
    # The user is prompted to choose between encryption, decryption, or quitting.
    # Then, the user is asked for the message to encrypt or decrypt.
    # Finally, the script performs the encryption or decryption and displays the result.

    mode = get_user_choice()
    message = get_message(mode)
    translated = encrypt_decrypt_message(message, mode)

    print(translated)


if __name__ == '__main__':
    morse_code()

