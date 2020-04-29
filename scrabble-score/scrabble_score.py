letter_score = dict({
    'Q': 10, 'Z': 10,
    'J': 8, 'X': 8,
    'K': 5,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'D': 2, 'G': 2,
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1
})

def score(word):
    return sum(letter_score.get(ch, 1) for ch in word.upper())
