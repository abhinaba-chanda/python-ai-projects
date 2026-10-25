# 🤖 Python AI Projects

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![No API key](https://img.shields.io/badge/API%20key-not%20needed-success?style=for-the-badge)
![Offline](https://img.shields.io/badge/runs-offline-blueviolet?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

Beginner-friendly **AI projects in pure Python**. No libraries to install, no API keys, no internet needed.
Each project shows the idea behind a real AI technique in a small file you can read in a few minutes.

## 📂 Projects

| # | Project | AI idea | Run it |
|---|---------|---------|--------|
| 1 | [Rule-based chatbot](01_rule_based_chatbot/chatbot.py) | Pattern matching (like ELIZA, 1966) | `python chatbot.py` |
| 2 | [Sentiment classifier](02_sentiment_classifier/sentiment.py) | Naive Bayes, written from scratch | `python sentiment.py` |
| 3 | [Tic-tac-toe AI](03_tic_tac_toe_ai/tictactoe.py) | Minimax search (it never loses) | `python tictactoe.py` |
| 4 | [Number guesser](04_number_guesser_ai/guesser.py) | Binary search (max 7 guesses for 1-100) | `python guesser.py` |
| 5 | [Spam detector](05_spam_detector/spam_detector.py) | Perceptron that learns word weights | `python spam_detector.py` |

## 🚀 How to run

You only need [Python 3.9 or newer](https://www.python.org/downloads/).

```bash
git clone https://github.com/abhinaba-chanda/python-ai-projects.git
cd python-ai-projects/03_tic_tac_toe_ai
python tictactoe.py
```

On Windows you can also use `py tictactoe.py`.

## 🧪 Tests

```bash
python -m unittest discover tests -v
```

The tests check that the chatbot replies, the classifier gets at least 80% right on new sentences,
the tic-tac-toe AI never loses (it plays every possible game against you), and the guesser always finds the number in 7 tries.

## 🧠 What I learned

- **Chatbot:** regular expressions and how early chatbots worked before modern AI.
- **Naive Bayes:** counting words + probability = a working text classifier. Log probabilities and Laplace smoothing.
- **Minimax:** recursion and game trees. The AI imagines every future move.
- **Binary search:** why halving is so fast (2⁷ = 128 > 100).
- **Perceptron:** the simplest "neural network". It learns from its mistakes.

## 📜 License

[MIT](LICENSE) © Abhinaba Chanda
