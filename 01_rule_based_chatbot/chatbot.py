"""
A simple rule-based chatbot.

It does not use any AI library or API key. It matches patterns
(regular expressions) in what you type and picks a reply.
This is how the very first chatbots, like ELIZA (1966), worked.

Run:  python chatbot.py
"""
import random
import re
from datetime import datetime

# Each rule: (pattern, list of possible replies)
# {0} in a reply is filled with the text captured by the pattern.
RULES = [
    (r"\b(hi|hello|hey|namaste)\b", ["Hello! 👋", "Hey there!", "Namaste! 🙏"]),
    (r"\bmy name is (\w+)", ["Nice to meet you, {0}!", "Hi {0}, great name!"]),
    (r"\bhow are you\b", ["I'm just Python code, but I'm running great! How about you?"]),
    (r"\bi am (sad|tired|bored|angry)\b", ["Sorry you feel {0}. Maybe some music or football will help? ⚽🎵"]),
    (r"\bi am (happy|good|fine|great)\b", ["Awesome! Glad you're {0} 😄"]),
    (r"\b(football|soccer)\b", ["Football is the best sport! Who is your favourite player?"]),
    (r"\b(messi|barca|barcelona)\b", ["Visca Barça! 🔵🔴 Messi is the GOAT."]),
    (r"\b(python|javascript|coding|programming)\b", ["Coding is a superpower. Keep practising every day! 💻"]),
    (r"\bwhat time is it\b|\btime\b", ["__TIME__"]),
    (r"\b(joke|funny)\b", [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the Python programmer wear glasses? Because he couldn't C. 👓",
    ]),
    (r"\b(thanks|thank you)\b", ["You're welcome!", "Anytime! 😊"]),
]

DEFAULT_REPLIES = [
    "Interesting! Tell me more.",
    "Hmm, I'm not sure I understand. Can you say it another way?",
    "I'm a simple bot, I only know a few topics: football, coding, jokes, time...",
]

EXIT_WORDS = {"bye", "quit", "exit", "goodbye"}


def get_reply(message: str) -> str:
    """Return the bot's reply for one message."""
    text = message.strip()
    for pattern, replies in RULES:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            reply = random.choice(replies)
            if reply == "__TIME__":
                return "It's " + datetime.now().strftime("%I:%M %p") + " ⏰"
            groups = match.groups()
            # Names get a capital letter, everything else stays lowercase
            groups = [g.title() if "name" in pattern else g.lower() for g in groups]
            return reply.format(*groups) if groups else reply
    return random.choice(DEFAULT_REPLIES)


def main():
    print("🤖 ChatBot: Hi! Type something (or 'bye' to quit).")
    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if message.lower().strip() in EXIT_WORDS:
            break
        print("🤖 ChatBot:", get_reply(message))
    print("🤖 ChatBot: Bye! See you soon 👋")


if __name__ == "__main__":
    main()
