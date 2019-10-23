import os
import random

num_words = input("How many words do you want to get? \n")
sentence = []

with open('/usr/share/dict/words', "r") as f:
    for _ in num_words:
        sentence.append(random.choice("/usr/share/dict/words"))