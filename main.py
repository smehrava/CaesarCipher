from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")



def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in original_text:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter)
            new_position = (shifted_position - shift_amount) % len(alphabet)
            cipher_text += alphabet[new_position]
    print(f"Here is the decoded result: {cipher_text}")



def caesar(choice):
    if choice == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif choice == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Wrong choice")

continue_caesar = True
while continue_caesar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(choice=direction)

    yes_or_no = input("Do you want to continue?").lower()
    if yes_or_no == "yes":
        continue_caesar = True
    else:
        continue_caesar = False
