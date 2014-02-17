import random


def generate_(wordlist, count=4, min_len=4, max_len=10):
    words_matched = 0
    words = [""] * 4

    for i, w in enumerate(wordlist):
        w = w.strip()
        if min_len <= len(w) <= max_len:
            words_matched += 1
            for j in range(count):
                if random.randint(1, words_matched) == 1:
                    words[j] = w

    if words_matched == 0:
        raise ValueError("No words matched")

    return (words, words_matched)

def generate(*args, **kwargs):
    return generate_(*args, **kwargs)[0]
