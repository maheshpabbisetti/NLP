import nltk
nltk.download('punkt')
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
text = "This is a sample text for part-of-speech tagging."
words = word_tokenize(text)
tagged_words = nltk.pos_tag(words)
print(tagged_words)
