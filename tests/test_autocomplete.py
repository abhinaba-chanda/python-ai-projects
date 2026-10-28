"""Unit tests (unittest discovery in the tests folder)."""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "08_word_autocomplete"))

import autocomplete  # noqa: E402


class TestAutocomplete(unittest.TestCase):
    def test_suggest(self):
        t = autocomplete.Trie()
        for w in ["car", "cart", "care", "dog"]:
            t.insert(w)
        self.assertEqual(t.suggest("car"), ["car", "care", "cart"])
        self.assertEqual(t.suggest("x"), [])


if __name__ == "__main__":
    unittest.main()
