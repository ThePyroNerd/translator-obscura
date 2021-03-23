# Translator Obscura is a translator bot for not-so-common languages. Created by Cameron Hill.
# This version of Translator Obscura is written in Python and was last updated on 03/23/2021
import discord
import os
from keep_alive import keep_alive

client = discord.Client()

# To Al Bhed
def to_al_bhed(phrase):
  phrase = phrase.replace('to.albhed ', '')
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


  # From Al Bhed
def from_al_bhed(phrase):
  phrase = phrase.replace('albhed.to ', '')
  result = ''
  dict_a = {'Y': 'A', 'P': 'B', 'L': 'C', 'T': 'D', 'A': 'E', 'V': 'F', 'K': 'G', 'R': 'H', 'E': 'I', 'Z': 'J',
            'G': 'K', 'M': 'L', 'S': 'M', 'H': 'N', 'U': 'O', 'B': 'P', 'X': 'Q', 'N': 'R', 'C': 'S', 'D': 'T',
            'I': 'U', 'J': 'V', 'F': 'W', 'Q': 'X', 'O': 'Y', 'W': 'Z', 'y': 'a', 'p': 'b', 'l': 'c', 't': 'd',
            'a': 'e', 'v': 'f', 'k': 'g', 'r': 'h', 'e': 'i', 'z': 'j', 'g': 'k', 'm': 'l', 's': 'm', 'h': 'n',
            'u': 'o', 'b': 'p', 'x': 'q', 'n': 'r', 'c': 's', 'd': 't', 'i': 'u', 'j': 'v', 'f': 'w', 'q': 'x',
            'o': 'y', 'w': 'z'}
  for letter in phrase:
      if letter.isalpha():
          result += dict_a.get(letter)
      else:
          result += letter
  return result


# To Cipher
def to_cipher(phrase):
  phrase = phrase.replace('to.cipher ', '')
  key = int(phrase[0])
  phrase = phrase[2:]
  result = ''
  for letter in phrase:
      if letter.isalpha():
          # Subtract the ASCII value of capital A, add key, modulus 26, add ASCII value back
          if letter.isupper():
              result += chr((((ord(letter) - 65) + key) % 26) + 65)
          # Subtract the ASCII value of lower a, add key, modulus 26, add ASCII value back
          elif letter.islower():
              result += chr((((ord(letter) - 97) + key) % 26) + 97)
      else:
          result += letter
  return result


  # From Cipher
def from_cipher(phrase):
  phrase = phrase.replace('cipher.to ', '')
  key = int(phrase[0])
  phrase = phrase[2:]
  result = ''
  for letter in phrase:
      if letter.isalpha():
          # Subtract the ASCII value of capital A, subtract key, modulus 26, add ASCII value back
          if letter.isupper():
              result += chr((((ord(letter) - 65) - key) % 26) + 65)
          # Subtract the ASCII value of lower a, subtract key, modulus 26, add ASCII value back
          elif letter.islower():
              result += chr((((ord(letter) - 97) - key) % 26) + 97)
      else:
          result += letter
  return result


# To Pig Latin
def to_pig_latin(phrase):
  phrase = phrase.replace('to.piglatin ', '')
  result = ''
  words = phrase.strip(".?!-").split()
  for word in words:
      result += word[1:] + word[0].lower() + "ay "
  if phrase[-1] == '.' or '?' or '!':
      return result.capitalize().strip() + phrase[-1]
  else:
      return result.strip()


# From Pig Latin
def from_pig_latin(phrase):
  phrase = phrase.replace('piglatin.to ', '')
  phrase = phrase.replace('ay', '')
  result = ''
  words = phrase.strip(".?!-").split()
  for word in words:
      result += word[-1] + word[0:-1].lower()
  if phrase[-1] == '.' or '?' or '!':
      return result.capitalize().strip() + phrase[-1]
  else:
      return result.strip()


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  elif message.content.startswith('to.albhed'):
    await message.channel.send(to_al_bhed(message.content))
  elif message.content.startswith('to.cipher'):
    await message.channel.send(to_cipher(message.content))
  elif message.content.startswith('to.piglatin'):
    await message.channel.send(to_pig_latin(message.content))
  elif message.content.startswith('albhed.to'):
    await message.channel.send(from_al_bhed(message.content))
  elif message.content.startswith('cipher.to'):
    await message.channel.send(from_cipher(message.content))
  elif message.content.startswith('piglatin.to'):
    await message.channel.send(from_pig_latin(message.content))
  elif message.content.startswith('to.help'):
    await message.channel.send('I am a translator bot for not-so-common languages.\n'
    'Here is a list of my available translations, and the command used to invoke them:\n'
    '\n'
    'Al Bhed - `to.albhed Hello!` or `albhed.to Rammu!`\n'
    'Cipher - `to.cipher 3 Hello!` or `cipher.to 3 Jhoor!` (Requires a single digit number to use as a key)\n'
    'Pig Latin - `to.piglatin Hello!` or `piglatin.to Ellohay!`\n')

keep_alive()
client.run(os.getenv('TOKEN'))