# Translator Obscura is a simple translator app for not-so-common languages. Created by Cameron Hill
# This version of Translator Obscura is written in Python and was last updated on 03/22/2021

# Al Bhed
def al_bhed(phrase):
    result = ''
    dict_a = {'A': 'Y', 'B': 'P', 'C': 'L', 'D': 'T', 'E': 'A', 'F': 'V', 'G': 'K', 'H': 'R', 'I': 'E', 'J': 'Z',
              'K': 'G', 'L': 'M', 'M': 'S', 'N': 'H', 'O': 'U', 'P': 'B', 'Q': 'X', 'R': 'N', 'S': 'C', 'T': 'D',
              'U': 'I', 'V': 'J', 'W': 'F', 'X': 'Q', 'Y': 'O', 'Z': 'W', 'a': 'y', 'b': 'p', 'c': 'l', 'd': 't',
              'e': 'a', 'f': 'v', 'g': 'k', 'h': 'r', 'i': 'e', 'j': 'z', 'k': 'g', 'l': 'm', 'm': 's', 'n': 'h',
              'o': 'u', 'p': 'b', 'q': 'x', 'r': 'n', 's': 'c', 't': 'd', 'u': 'i', 'v': 'j', 'w': 'f', 'x': 'q',
              'y': 'o', 'z': 'w'}
    for letter in phrase:
        if letter.isalpha():
            result += dict_a.get(letter)
        else:
            result += letter
    return result


# Caesar Cipher
def caesar_cipher(phrase):
    key = int(input('Enter a number to use a a key: '))
    result = ''
    for letter in phrase:
        if letter.isalpha():
            # Subtract the ASCII value of capital A, modulus 26, add ASCII value back
            if letter.isupper():
                result += chr((((ord(letter) - 65) + key) % 26) + 65)
            # Subtract the ASCII value of lower a, modulus 26, add ASCII value back
            elif letter.islower():
                result += chr((((ord(letter) - 97) + key) % 26) + 97)
        else:
            result += letter
    return result


# Pig Latin
def pig_latin(phrase):
    result = ''
    words = phrase.strip(".?!-").split()
    for word in words:
        result += word[1:] + word[0].lower() + "ay "
    if phrase[-1] == '.' or '?' or '!':
        return result.capitalize().strip() + phrase[-1]
    else:
        return result.strip()


while True:
    # Prompt user to select language for translation and route to functions
    select = input('\nEnter a number to select a language:\n'
                   "1 : Al Bhed\n"
                   "2 : Caesar Cipher\n"
                   "3 : Pig Latin\n"
                   "4 : Exit\n"
                   "Your selection: ")
    if int(select) == 1:
        print(al_bhed(input('\nEnter a word or sentence: ')))
    elif int(select) == 2:
        print(caesar_cipher(input('\nEnter a word or sentence: ')))
    elif int(select) == 3:
        print(pig_latin(input('\nEnter a word or sentence: ')))
    elif int(select) == 4:
        break
    else:
        input('\nInvalid selection. Press Enter to continue.')
