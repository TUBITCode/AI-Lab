import nltk
from nltk.stem import PorterStemmer

# Create a stemmer object
stemmer = PorterStemmer()

# Define a list of words to stem
words = ["playing", "sing", "plays", "played", "dancing", "helped","threw"]

# Stem each word in the list
for word in words:
    stemmed_word = stemmer.stem(word)
    print(word, "->", stemmed_word)
