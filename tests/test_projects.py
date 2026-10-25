"""Run with:  python -m unittest discover tests"""
import contextlib
import io
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for folder in ["01_rule_based_chatbot", "02_sentiment_classifier", "03_tic_tac_toe_ai",
               "04_number_guesser_ai", "05_spam_detector"]:
    sys.path.insert(0, os.path.join(ROOT, folder))

import chatbot          # noqa: E402
import sentiment        # noqa: E402
import tictactoe        # noqa: E402
import guesser          # noqa: E402
import spam_detector    # noqa: E402
from data import TRAIN_DATA, TEST_DATA  # noqa: E402


class TestChatbot(unittest.TestCase):
    def test_name(self):
        self.assertIn("Abhinaba", chatbot.get_reply("my name is Abhinaba"))

    def test_barca(self):
        self.assertIn("Barça", chatbot.get_reply("I love Barcelona"))


class TestSentiment(unittest.TestCase):
    def test_accuracy(self):
        model = sentiment.NaiveBayes()
        model.train(TRAIN_DATA)
        correct = sum(model.predict(t) == label for t, label in TEST_DATA)
        self.assertGreaterEqual(correct / len(TEST_DATA), 0.8)


class TestTicTacToe(unittest.TestCase):
    def test_blocks_win(self):
        X, O, E = tictactoe.HUMAN, tictactoe.AI, tictactoe.EMPTY
        board = [X, X, E, E, O, E, E, E, E]
        self.assertEqual(tictactoe.best_move(board), 2)

    def test_takes_win(self):
        X, O, E = tictactoe.HUMAN, tictactoe.AI, tictactoe.EMPTY
        board = [O, O, E, X, X, E, X, E, E]
        self.assertEqual(tictactoe.best_move(board), 2)

    def test_ai_never_loses(self):
        """Play every possible human move sequence; the AI must never lose."""
        def play(board):
            if tictactoe.winner(board) == tictactoe.HUMAN:
                return False
            if tictactoe.winner(board) or tictactoe.is_full(board):
                return True
            for i in range(9):
                if board[i] == tictactoe.EMPTY:
                    b = board[:]
                    b[i] = tictactoe.HUMAN
                    if not (tictactoe.winner(b) or tictactoe.is_full(b)):
                        b[tictactoe.best_move(b)] = tictactoe.AI
                    if not play(b):
                        return False
            return True
        self.assertTrue(play([tictactoe.EMPTY] * 9))


class TestGuesser(unittest.TestCase):
    def test_finds_every_number_in_7(self):
        for secret in range(1, 101):
            def answer(prompt, s=secret):
                n = int(prompt.split()[2].rstrip("?"))
                return "y" if n == s else ("h" if s > n else "l")
            with contextlib.redirect_stdout(io.StringIO()):
                found, guesses = guesser.guess_number(answer_fn=answer)
            self.assertEqual(found, secret)
            self.assertLessEqual(guesses, 7)


class TestSpam(unittest.TestCase):
    def test_learns_training_set(self):
        w, b = spam_detector.train(spam_detector.TRAIN)
        for text, label in spam_detector.TRAIN:
            self.assertEqual(int(spam_detector.is_spam(text, w, b)), label)


if __name__ == "__main__":
    unittest.main()
