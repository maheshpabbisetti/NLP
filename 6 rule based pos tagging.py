import re
rules = {
    "VBZ": [r"(.*s)$"],  # Present tense 3rd person singular verbs
    "NNS": [r"(.*s)$", r"^(.*)$"],  # Plural nouns and proper nouns
    "NN": [r"^(.*)$"],  # Singular nouns
    "JJ": [r"(.*ly)$"],  # Adjectives ending in "ly"
    "JJR": [r"(.*er)$"],  # Comparative adjectives
    "JJS": [r"(.*est)$"],  # Superlative adjectives
}
tags = {
    "VBZ": "Verb, present tense, 3rd person singular",
    "NNS": "Noun, plural",
    "NN": "Noun, singular",
    "JJ": "Adjective",
    "JJR": "Adjective, comparative",
    "JJS": "Adjective, superlative",
}
def tag_word(word):
  for tag, patterns in rules.items():
    for pattern in patterns:
      if re.match(pattern, word):
        return word, tags[tag]
  return word, "UNKNOWN"
sentence = "The dog chased the cat quickly."
tagged_words = [tag_word(word) for word in sentence.split()]
print(tagged_words)
