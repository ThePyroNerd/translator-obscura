# Translator Obscura is a simple translator app for not-so-common languages. Created for fun by Cameron Hill
# This version of Translator Obscura is written in Python and was last updated on 02/25/2021

# Al Bhed
def al_bhed(phrase):
    result = ''
    dict_a = {'A': 'Y', 'B': 'P', 'C': 'L', 'D': 'T', 'E': 'A', 'F': 'V', 'G': 'K', 'H': 'R', 'I': 'E', 'J': 'Z',
              'K': 'G', 'L': 'M', 'M': 'S', 'N': 'H', 'O': 'U', 'P': 'B', 'Q': 'X', 'R': 'N', 'S': 'C', 'T': 'D',
              'U': 'I', 'V': 'J', 'W': 'F', 'X': 'Q', 'Y': 'O', 'Z': 'W', 'a': 'y', 'b': 'p', 'c': 'l', 'd': 't',
              'e': 'a', 'f': 'v', 'g': 'k', 'h': 'r', 'i': 'e', 'j': 'z', 'k': 'g', 'l': 'm', 'm': 's', 'n': 'h',
              'o': 'u', 'p': 'b', 'q': 'x', 'r': 'n', 's': 'c', 't': 'd', 'u': 'i', 'v': 'j', 'w': 'f', 'x': 'q',
              'y': 'o', 'z': 'w', ' ': ' ', '.': '.', ',': ',', '-': '-', '?': '?', '!': '!'}
    for letter in phrase:
        result = result + dict_a.get(letter)
    return result


# Pig Latin
def pig_latin(phrase):
    result = ''
    words = phrase.strip(".?!-").split()
    for word in words:
        result = result + word[1:] + word[0].lower() + "ay "
    if phrase[-1] == '.' or '?' or '!':
        return result.capitalize().strip() + phrase[-1]
    else:
        return result.strip()


# Prompt user to select language for translation
select = input("Enter a number to select a language:\n"
               "1 : Al Bhed\n"
               "2 : Pig Latin\n"
               "Your selection: ")
if int(select) == 1:
    print(al_bhed(input('Enter a word or sentence: ')))
elif int(select) == 2:
    print(pig_latin(input('Enter a word or sentence: ')))
else:
    print('Invalid selection.')
