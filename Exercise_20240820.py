# The program starts by prompting the user to enter some text in the terminal
# After the user presses Enter, they get different statistics about the submitted text
# the number of words, sentences, and characters, the most frequent words used in the text,
# the average word length, and the average sentence length.

import re

word_len = []
freq_dict = {}
avg_sentence_len = 0
sentence_len = []

def remove_punctuations(text):
    return re.sub(r'[^\w\s]','',text)

text = input("Enter a block of text for analysis:")

chars = len(text)

# Sentences
sentences_arr = [x for x in text.split(sep='.') if len(x) > 0]
sentences = len(sentences_arr)

# Average sentence length in words
for sentence in sentences_arr:
    sentence_len.append(len(remove_punctuations(sentence).lower().split()))

# Total words
freq = remove_punctuations(text).lower()
freq = freq.split()
words = len(freq)

# Most freq word and avg word length
for word in freq:
    if word in freq_dict.keys():
        word_freq = freq_dict.get(word)
        freq_dict.update({word:word_freq + 1})
    else:
        freq_dict.update({word:1})
    word_len.append(len(word))

sorted_d = [[w, freq_dict[w]] for w in sorted(freq_dict, key=freq_dict.get, reverse=True)]
avg_word_len = sum(word_len) / len(word_len)

# Result
print("Text Analysis Result:")
print("---------------------")
print(f"Total Characters: {chars}")
print(f"Total Words: {words}")
print(f"Total Sentences: {sentences}")
print(f"Most Frequent Word: '{sorted_d[0][0]}' (used {sorted_d[0][1]} times)")
print(f"Average word length: {avg_word_len:.2f} characters")
print(f"Average sentence length: {(sum(sentence_len)/sentences):.0f} words")
