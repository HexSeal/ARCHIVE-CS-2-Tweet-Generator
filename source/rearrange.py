import random

words = []
random_words = []

def rearrange():
    for word in words:
        random_words.append(random.choice(words))
    return random_words