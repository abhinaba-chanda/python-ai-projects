"""
Keyword-weight spam detector (a tiny "perceptron").

Each word gets a weight. The program LEARNS the weights from examples
using the perceptron rule: when it makes a mistake, it nudges the
weights of the words in that message up or down.

Run:  python spam_detector.py
"""
import re

TRAIN = [
    ("win a free iphone now click here", 1),
    ("congratulations you won a lottery prize claim now", 1),
    ("cheap loans available click the link", 1),
    ("free money offer limited time only", 1),
    ("you are selected for a cash reward", 1),
    ("are we still playing football tomorrow", 0),
    ("can you send me the python notes", 0),
    ("happy birthday have a great day", 0),
    ("the match starts at 8 pm", 0),
    ("let's meet after class to study", 0),
]


def words(text):
    return re.findall(r"[a-z]+", text.lower())


def train(data, epochs=20, lr=1.0):
    weights, bias = {}, 0.0
    for _ in range(epochs):
        mistakes = 0
        for text, label in data:
            score = bias + sum(weights.get(w, 0.0) for w in words(text))
            guess = 1 if score > 0 else 0
            error = label - guess          # +1, 0 or -1
            if error:
                mistakes += 1
                bias += lr * error
                for w in words(text):
                    weights[w] = weights.get(w, 0.0) + lr * error
        if mistakes == 0:
            break
    return weights, bias


def is_spam(text, weights, bias):
    return bias + sum(weights.get(w, 0.0) for w in words(text)) > 0


def main():
    weights, bias = train(TRAIN)
    top = sorted(weights.items(), key=lambda kv: kv[1], reverse=True)[:5]
    print("Most 'spammy' words learned:", ", ".join(w for w, _ in top))
    tests = ["claim your free prize now", "see you at football practice", "click here to win cash"]
    for t in tests:
        print(("🚫 SPAM " if is_spam(t, weights, bias) else "✅ OK   ") + "<- " + t)
    print("\nType a message to check (empty line to quit):")
    while True:
        try:
            t = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not t:
            break
        print("   🚫 SPAM" if is_spam(t, weights, bias) else "   ✅ Not spam")


if __name__ == "__main__":
    main()
