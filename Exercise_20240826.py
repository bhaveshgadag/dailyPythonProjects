# The program should allow users to add a word and the translation for that word through a command line interface. 
# The program saves the results in a text file.
# If the user enters “done”, the program closes and adds the data to a text file.

words =[]

while True:
    word = input("Enter a word in Language 1 (or type 'done' to finish): ")
    if word == 'done':
        with open('bilingual-vocab.txt', 'a') as file:
            for word in words:
                file.write(f"{word[0]} - {word[1]}\n")
        break
    else:
        translation = input(f"Enter a '{word}' in Language 2 : ")
        words.append([word, translation])
        print(f"'{word}' (Language 1) has been added with the translation: '{translation}' (Language 2)")
