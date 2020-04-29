def abbreviate(words):
    words = words.upper().replace("_"," ").replace("-", " ")
    return ''.join(word[0] for word in words.split())
