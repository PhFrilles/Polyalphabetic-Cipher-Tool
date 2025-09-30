import os

def encrypt(message, keyword):
    character_set = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t",
                     "u", "v", "w", "x",
                     "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                     "S", "T", "U", "V",
                     "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", '"', "£", "$", "%", "^",
                     "&", "*", "(", ")",
                     "`", "¬", "-", "_", "=", "+", "[", "{", "]", "}", "#", "~", ";", ":", "'", "@", ",", "<", ".", ">",
                     "/", "?"]

    og_numbers = []
    code_letters = []
    count = -1

    # Turns message into numbers
    for character in message:
        character = character_set.index(character)
        og_numbers.append(character)

    for num in og_numbers:
        count += 1
        current_letter = keyword[count]
        #  Sets count back to zero once over keyword length
        if count >= len(keyword) - 1:
            count = -1

        key = character_set.index(current_letter)

        if num == 0:
            num = -1

        new_num = num + key

        if new_num > 94:
            new_num = new_num - 94
            letter = character_set[new_num]
            code_letters.append(letter)
        else:
            letter = character_set[new_num]
            code_letters.append(letter)

    codeword = "".join(code_letters)
    print("Encrypted text is: ", codeword)
    print("Keyword :",keyword)


def decrypt(message, keyword):
    character_set = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t",
                     "u", "v", "w", "x",
                     "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                     "S", "T", "U", "V",
                     "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", '"', "£", "$", "%", "^",
                     "&", "*", "(", ")",
                     "`", "¬", "-", "_", "=", "+", "[", "{", "]", "}", "#", "~", ";", ":", "'", "@", ",", "<", ".", ">",
                     "/", "?"]

    count = -1
    plaintext_letters = []

    ## Turns message into numbers
    for character in message:

        count += 1
        current_letter = keyword[count]

        #  Sets count back to zero once over keyword length
        if count >= len(keyword) - 1:
            count = -1

        #  Turns current letter of keyword into a number
        key = character_set.index(current_letter)

        letter_num = character_set.index(character)

        ## Subtracts letter from key. If its minus, makes it positive.
        plain_num = letter_num - key

        if plain_num == -1:
            plain_num = 0
            plain_letter = character_set[plain_num]
            plaintext_letters.append(plain_letter)

        elif plain_num < -1 or plain_num == 0:
            plain_num = key - letter_num
            excess_num = letter_num + 94
            plain_num = excess_num - key

            plain_letter = character_set[plain_num]
            plaintext_letters.append(plain_letter)

        else:
            plain_letter = character_set[plain_num]
            plaintext_letters.append(plain_letter)

    plaintext = "".join(plaintext_letters)
    print("Decrypted text is: ", plaintext)


def start():
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄ ")
    print("▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌")
    print("▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌      ▀▀▀▀▀▀▀▀▀█░▌")
    print("▐░▌          ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌               ▐░▌")
    print("▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌               ▐░▌")
    print("▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌      ▄▄▄▄▄▄▄▄▄█░▌")
    print("▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌          ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀      ▐░░░░░░░░░░░▌")
    print("▐░▌          ▐░▌    ▐░▌▐░▌▐░▌          ▐░▌     ▐░▌       ▐░▌     ▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░█▀▀▀▀▀▀▀▀▀ ")
    print("▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌      ▐░▌     ▐░▌               ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌      ▐░█▄▄▄▄▄▄▄▄▄ ")
    print("▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░░░░░░░░░░░▌")
    print(" ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀                 ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀▀▀▀▀▀▀▀▀▀▀ ")
    menu()

def menu():
    print("\n- Decrypt\n- Encrypt\n")
    choice = input("Please type an option: ").capitalize()

    if choice == "Decrypt":
        message = input("Please input the message you would like to decrypt: ")
        key = input("Please enter the keyword: ")
        print("")

        decrypt(message,key)

        input("\nPress enter to return to menu: ")
        os.system('cls')
        start()

    if choice == "Encrypt":
        message = input("Please input the message you would like to encrypt: ")
        key = input("Please enter the keyword you would like to use: ")
        print("")

        encrypt(message, key)

        input("\nPress enter to return to menu: ")
        os.system('cls')
        start()

    if choice != "Decrypt" or choice != "Encrypt":
        print("\nThat is not an option. Please retry...")
        os.system('cls')
        start()

start()
