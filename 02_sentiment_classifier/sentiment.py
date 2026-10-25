"""
Naive Bayes sentiment classifier, written from scratch.

No libraries like scikit-learn are used. You will see how
"machine learning" for text works with simple counting + probability:

    P(class | words)  is proportional to  P(class) * product of P(word | class)

We use log probabilities (to avoid tiny numbers) and Laplace
smoothing (+1) so unseen words don't make the probability zero.

Run:  python sentiment.py
"""
import math
import re
from collections import Counter, defaultdict

from data import TRAIN_DATA, TEST_DATA


def tokenize(text: str) -> list[str]:
    """Lowercase the text and split it into words."""
    return re.findall(r"[a-z']+", text.lower())


class NaiveBayes:
    def __init__(self):
        self.class_counts = Counter()           # how many sentences per class
        self.word_counts = defaultdict(Counter)  # word counts per class
        self.vocab = set()

    def train(self, data):
        for text, label in data:
            self.class_counts[label] += 1
            for word in tokenize(text):
                self.word_counts[label][word] += 1
                self.vocab.add(word)

    def scores(self, text: str) -> dict:
        total_docs = sum(self.class_counts.values())
        words = tokenize(text)
        result = {}
        for label in self.class_counts:
            # log P(class)
            score = math.log(self.class_counts[label] / total_docs)
            total_words = sum(self.word_counts[label].values())
            for word in words:
                # log P(word | class) with Laplace (+1) smoothing
                count = self.word_counts[label][word] + 1
                score += math.log(count / (total_words + len(self.vocab)))
            result[label] = score
        return result

    def predict(self, text: str) -> str:
        s = self.scores(text)
        return max(s, key=s.get)


def main():
    model = NaiveBayes()
    model.train(TRAIN_DATA)
    print(f"Trained on {len(TRAIN_DATA)} sentences, vocabulary of {len(model.vocab)} words.\n")

    correct = 0
    for text, label in TEST_DATA:
        guess = model.predict(text)
        correct += guess == label
        mark = "✅" if guess == label else "❌"
        print(f"{mark} {guess:8} <- {text}")
    print(f"\nTest accuracy: {correct}/{len(TEST_DATA)} = {correct / len(TEST_DATA):.0%}\n")

    print("Now try your own sentences (empty line to quit):")
    while True:
        try:
            text = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not text:
            break
        emoji = "😊" if model.predict(text) == "positive" else "😞"
        print(f"   {model.predict(text)} {emoji}")


if __name__ == "__main__":
    main()
