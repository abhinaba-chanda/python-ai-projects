"""Tiny word-level Markov chain text generator."""
import random
from collections import defaultdict


def build_chain(text):
    words = text.split()
    chain = defaultdict(list)
    for a, b in zip(words, words[1:]):
        chain[a].append(b)
    return dict(chain)


def generate(chain, start, length=10, seed=None):
    rng = random.Random(seed)
    word, out = start, [start]
    for _ in range(length - 1):
        options = chain.get(word)
        if not options:
            break
        word = rng.choice(options)
        out.append(word)
    return " ".join(out)


if __name__ == "__main__":
    sample = "the cat sat on the mat and the cat ran to the door"
    print(generate(build_chain(sample), "the", 8))
