import random
pos_tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', '.', ',', ':', '(', ')', '[', ']', '``', "''", '```', "'''", '```', "''`"]
word_tags = {
    'This': ['DT'],
    'is': ['VBZ'],
    'a': ['DT'],
    'sample': ['NN'],
    'text': ['NN'],
    'for': ['IN'],
    'part-of-speech': ['NN'],
    'tagging': ['NN'],
    '.': ['.']
}
transitions = {
    'DT': {'DT': 0.5, 'IN': 0.5, '.': 0.0},
    'IN': {'IN': 0.5, 'NN': 0.5, '.': 0.0},
    'NN': {'DT': 0.1, 'IN': 0.1, '.': 0.8},
    'VBZ': {'DT': 0.0, 'IN': 0.0, '.': 0.0},
    '.': {'.': 1.0}
}
emissions = {
    'DT': {'This': 1.0},
    'IN': {'for': 1.0},
    'NN': {'sample': 1.0, 'text': 1.0, 'part-of-speech': 1.0, 'tagging': 1.0},
    'VBZ': {'is': 1.0},
    '.': {'.': 1.0}
}
input_text = "This is a sample text for part-of-speech tagging.".split()
tag_sequence = []
for word in input_text:
    if word in emissions:
        probabilities = {tag: emissions[word].get(tag, 0.0) * transitions[prev_tag].get(tag, 0.0) for tag in pos_tags}
    else:
        probabilities = {tag: 1.0 / len(pos_tags) for tag in pos_tags}
    total = sum(probabilities.values())
    probabilities = {tag: prob / total for tag, prob in probabilities.items()}
    tag = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
    tag_sequence.append(tag)
    prev_tag = tag
print("Input text:", input_text)
print("Tag sequence:", tag_sequence)
