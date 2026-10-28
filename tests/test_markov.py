"""Unit tests (unittest discovery in the tests folder)."""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "06_markov_text_generator"))

import markov  # noqa: E402


class TestMarkov(unittest.TestCase):
    def test_chain_and_generate(self):
        chain = markov.build_chain("a b a c")
        self.assertEqual(chain["a"], ["b", "c"])
        text = markov.generate(chain, "a", 5, seed=1)
        self.assertTrue(text.startswith("a"))
        self.assertLessEqual(len(text.split()), 5)


if __name__ == "__main__":
    unittest.main()
