"""Small hand-written dataset for the sentiment classifier."""

TRAIN_DATA = [
    ("I love this movie, it was amazing", "positive"),
    ("What a great match, the team played brilliantly", "positive"),
    ("This is the best day of my life", "positive"),
    ("I am so happy with my new phone", "positive"),
    ("The food was delicious and the service was excellent", "positive"),
    ("Fantastic goal, what a beautiful finish", "positive"),
    ("I really enjoyed the concert, the music was awesome", "positive"),
    ("This game is fun and exciting", "positive"),
    ("Wonderful experience, I would recommend it", "positive"),
    ("The code finally works, I feel great", "positive"),
    ("Nice work, I like it a lot", "positive"),
    ("Such a good and helpful tutorial", "positive"),
    ("I hate this movie, it was boring", "negative"),
    ("What a terrible match, the team played badly", "negative"),
    ("This is the worst day ever", "negative"),
    ("I am so sad and disappointed with my new phone", "negative"),
    ("The food was cold and the service was awful", "negative"),
    ("Horrible defending, we lost again", "negative"),
    ("I did not enjoy the concert, the sound was bad", "negative"),
    ("This game is slow and annoying", "negative"),
    ("Awful experience, I would not recommend it", "negative"),
    ("The code keeps crashing, I feel angry", "negative"),
    ("Bad work, I dislike it", "negative"),
    ("Such a useless and confusing tutorial", "negative"),
]

TEST_DATA = [
    ("The match was amazing and exciting", "positive"),
    ("I love the music", "positive"),
    ("Great tutorial, very helpful", "positive"),
    ("The service was terrible", "negative"),
    ("I hate when the code crashes", "negative"),
    ("Boring and slow game", "negative"),
]
