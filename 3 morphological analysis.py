import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

def morphological_analysis(sentence):
    tokens = word_tokenize(sentence)
    lemmatizer = WordNetLemmatizer()
    analyzed_words = []

    for token in tokens:
        # Perform lemmatization to get the base form of the word
        base_word = lemmatizer.lemmatize(token)
        # Get the part of speech (POS) tag for the word
        pos_tag = nltk.pos_tag([token])[0][1]
        analyzed_words.append((token, base_word, pos_tag))

    return analyzed_words

# Example usage
if __name__ == "__main__":
    sentence = "The quick brown foxes are jumping over the lazy dogs"
    analysis = morphological_analysis(sentence)
    print("Word\t\tBase Form\tPOS Tag")
    print("-------------------------------------------")
    for word, base_form, pos_tag in analysis:
        print(f"{word}\t\t{base_form}\t\t{pos_tag}")
