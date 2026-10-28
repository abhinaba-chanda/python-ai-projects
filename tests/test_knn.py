"""Unit tests (unittest discovery in the tests folder)."""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "07_knn_classifier"))

import knn  # noqa: E402


class TestKnn(unittest.TestCase):
    def test_predict(self):
        data = [((1, 1), "red"), ((1, 2), "red"), ((2, 1), "red"), ((5, 5), "blue"), ((6, 5), "blue")]
        self.assertEqual(knn.predict(data, (1.5, 1.5)), "red")
        self.assertEqual(knn.predict(data, (6, 6), k=2), "blue")
        self.assertAlmostEqual(knn.distance((0, 0), (3, 4)), 5.0)


if __name__ == "__main__":
    unittest.main()
