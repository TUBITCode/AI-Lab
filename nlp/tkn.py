import nltk
nltk.download('punkt')
# Load the Punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Text to tokenize
text = "Hello! How are you doing? I hope you're having a great day."

# Tokenize the text into sentences
sentences = tokenizer.tokenize(text)

# Print the sentences
for sentence in sentences:
    print(sentence)
