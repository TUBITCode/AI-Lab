import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# Define a sentence to analyze
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Perform POS tagging on the tokens
pos_tags = nltk.pos_tag(tokens)

# Print the POS tags
print(pos_tags)
