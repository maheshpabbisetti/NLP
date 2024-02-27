from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
conversation = [
    ("how are you?", "question"),
    ("what is this?", "question"),
    ("It starts at 7 PM.", "statement"),
    ("Are there any tickets available?", "question"),
    ("Yes, there are a few left.", "statement"),
    ("Great! I'd like to buy two tickets.", "request"),
    ("Sure, that'll be $20.", "statement"),
    ("Here you go.", "acknowledgement")
]
X, y = zip(*conversation)
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
pipeline.fit(X, y)
new_dialogues = [
    "hello! how are you today?",
    "i am doing well, thank you. how about you?",
    "can you please pass the salt?",
    "shure, here you go."
]
predicted_dialogue_acts = pipeline.predict(new_dialogues)
for dialogue, act in zip(new_dialogues, predicted_dialogue_acts):
    print("Dialogue: '{}', Predicted Dialogue Act: '{}'".format(dialogue, act))
