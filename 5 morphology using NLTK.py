import nltk
nltk.download('wordnet')
sentence = "The quick brown fox jumps over the lazy dog."
words = nltk.word_tokenize(sentence)
morphed_words = []
for word in words:
    synsets = nltk.corpus.wordnet.synsets(word)
    if not synsets:
        morphed_words.append((word, []))
    else:
        lemmas = []
        for synset in synsets:
            for lemma in synset.lemmas():
                lemmas.append(lemma.name())
        morphed_words.append((word, lemmas))
for word, lemmas in morphed_words:
    print(f"{word}: {lemmas}")
