import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

# Create a lemmatizer object
lemmatizer = WordNetLemmatizer()

# Define a list of words to lemmatize
words = ["playing", "sing", "plays", "played", "dancing", "beaten","got"]

# Lemmatize each word in the list
for word in words:
    lemmatized_word = lemmatizer.lemmatize(word)
    print(word, "->", lemmatized_word)
