# Translator Obscura
### A translator discord bot for not-so-common "languages"
#### Video Demo:  https://youtu.be/abFgtvbN9WI
#### Description:
This program can take words and sentences as input and return the translated equivalent for whichever option you select. Currently supports 4 translation modes: Al Bhed, Bmoji, Cipher, and Pig Latin.
### Translation Modes
#### Al Bhed:
> "The Al Bhed have their own language. Working like a substitution cipher (a language system replacing certain letters with others), it shares the same syntax and grammar as English in the English versions of Final Fantasy X and Final Fantasy X-2. Any spoken Al Bhed is styled in purple in written dialogue, with characters translated from Al Bhed in pink."

*https://finalfantasy.fandom.com/wiki/Al_Bhed#Language*
#### Bmoji
> B Button Emoji is an ideogram featuring a red block with the letter "B" written inside. While some have used to symbol to represent the B blood type, it has also been used online to represent the Bloods street gang and the kinship slang term "B" (short for "brother"). Additionally, characters in words are often replaced with the emoji..."

*https://knowyourmeme.com/memes/b-button-emoji-%F0%9F%85%B1*
#### Cipher
> "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence."

*https://en.wikipedia.org/wiki/Caesar_cipher*
#### Pig Latin
> "Pig Latin, or "Igpay Atinlay" is a language game or argot in which English words are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such a suffix. For example, "Wikipedia" would become "Ikipediaway" (the "W" is moved from the beginning and has "ay" appended to create a suffix). The objective is to conceal the words from others not familiar with the rules. The reference to Latin is a deliberate misnomer; Pig Latin is simply a form of argot, cant, or jargon unrelated to Latin, and the name is used for its English connotations as a strange and foreign-sounding language. It is most often used by young children as a fun way to confuse people unfamiliar with Pig Latin."

*https://en.wikipedia.org/wiki/Pig_Latin*
### Files
#### main.py:
Main program. Connects to discord application and allows usage of commands to run the functions within.
#### keep_alive.py:
Creates a Flask webserver that can be pinged to monitor online status of the bot.
### How To Use
In order to add this to your own discord server, you would have to download the files and self host, updating the `TOKEN` value in the last line of main.py. Once added, you can send the message `to.help` in any text channel that the bot has permissions for. This will display the current command/functionality list.

The individual commands are pretty straightforward. For example, you either want to translate something from English `to.albhed` or from `albhed.to` English.