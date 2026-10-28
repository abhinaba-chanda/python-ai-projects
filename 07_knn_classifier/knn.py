"""k-nearest neighbours from scratch (no libraries)."""
from collections import Counter
import math


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def predict(train, point, k=3):
    """train is a list of (features, label)."""
    nearest = sorted(train, key=lambda item: distance(item[0], point))[:k]
    return Counter(label for _, label in nearest).most_common(1)[0][0]


if __name__ == "__main__":
    data = [((1, 1), "red"), ((1, 2), "red"), ((5, 5), "blue"), ((6, 5), "blue")]
    print(predict(data, (2, 1)))
