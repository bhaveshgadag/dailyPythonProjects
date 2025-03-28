# The program starts by prompting the user to enter some text in the terminal
# After the user presses Enter, they get different statistics about the submitted text
# the number of words, sentences, and characters, the most frequent words used in the text,
# the average word length, and the average sentence length.

text = input("Enter a block of text for analysis:")

text = "Common frogs metamorphose through three distinct developmental life stages - aquatic larva, terrestrial juvenile, and adult. They have corpulent bodies with a rounded snout, webbed feet and long hind legs adapted for swimming in water and hopping on land. Common frogs are often confused with the common toad (Bufo bufo), but frogs can easily be distinguished as they have longer legs, hop, and have a moist skin, whereas toads crawl and have a dry 'warty' skin. The spawn of the two species also differs, in that frog spawn is laid in clumps and toad spawn is laid in long strings."
chars = len(text)

text_arr = text.split()
words = len(text_arr)

# text_arr = text.split(sep='.')
# sentences = len(text_arr)
# print(text_arr)

print("Text Analysis Result:")
print("---------------------")
print(f"Total Characters: {chars}")
print(f"Total Words: {words}")
print(f"Total Sentences: {sentences}")

# Text Analysis Result:
# Total Characters: 
# Total Words:
# Total Sentences:
# Most Frequent Word: (used times)
# Average word length: characters
# Average sentence length: words