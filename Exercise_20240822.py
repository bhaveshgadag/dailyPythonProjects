# Program where users can add a word and the translation for that word through a command line interface. 
# The program saves the results in a CSV file.

import csv

words = {}

while True:
    word = input("Enter a word in Language 1 (or type 'done' to finish): ")
    if word == 'done':
        
        break
    else:
        translation = input(f"Enter a '{word}' in Language 2 : ")
        words.update({word: translation})
        print(f"'{word}' (Language 1) has been added with the translation: '{translation}' (Language 2)")
