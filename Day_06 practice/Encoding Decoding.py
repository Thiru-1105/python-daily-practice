
import text2art

import art
from art import *
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    decrypt_text=""
    for letter in original_text:
        if letter not in alphabet:
            decrypt_text += letter
            continue
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decrypt_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {decrypt_text}")

def caesar(direction, original_text, shift_amount):

    if direction == "encode":
        encrypt(original_text, shift_amount)

    elif direction == "decode":
        decrypt(original_text, shift_amount)



repeat=True
while repeat:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, direction=direction)
    repeat_inp=input("Do you want to repeat?(y/n)\n").lower()
    if repeat_inp == "n":
        repeat=False
        print("Done!!!!!")




