"""
The computer guesses YOUR number using binary search.

Think of a number between 1 and 100. The AI halves the range
every time, so it always finds it in 7 guesses or fewer
(because 2^7 = 128 > 100).

Run:  python guesser.py
"""


def guess_number(low=1, high=100, answer_fn=input):
    guesses = 0
    while low <= high:
        mid = (low + high) // 2
        guesses += 1
        reply = answer_fn(f"Is it {mid}? (h = higher, l = lower, y = yes): ").strip().lower()
        if reply == "y":
            print(f"🎯 Got it in {guesses} guesses!")
            return mid, guesses
        if reply == "h":
            low = mid + 1
        elif reply == "l":
            high = mid - 1
        else:
            guesses -= 1
            print("Please type h, l or y.")
    print("Hmm, your answers don't add up. Did you change your number? 😄")
    return None, guesses


if __name__ == "__main__":
    print("Think of a number between 1 and 100, I'll guess it!")
    try:
        guess_number()
    except (EOFError, KeyboardInterrupt):
        print("\nBye!")
