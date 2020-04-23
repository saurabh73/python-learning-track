import re
from collections import Counter
pattern = re.compile(r"[\s,\.:!&@\$%\^_]+")
def count_words(sentence):
    sentence = sentence.lower().strip()
    words = map(lambda word: word.strip("'") , filter(lambda word: word.strip() != '', pattern.split(sentence)))
    return dict(Counter(words))

