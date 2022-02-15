import string
import re

class TextContainer:

    def __init__(self, text):
        self.text = text
    
    def wordCount(self):
        words = len(self.text.split())
        print("There are " + str(words) + "words in the text.")

    def charCount(self):
        chars = 0
        for char in self.text:
            chars += 1
        print("There are " + str(chars) + "chars in the text.")
    
    def asciiLetters(self):
        letters = 0
        for char in self.text:
            if char in string.ascii_letters:
                letters += 1
        print("There are " + str(letters) + " ASCII letters in the text.")

    def noPunct(self):
        newText = self.text.translate({ord(char):None for char in string.punctuation})
        return newText

    
tc = TextContainer("Lorem! Ipsum# Skoliosis?")
print(tc.noPunct())
    