from animations.animation import Animation

class AnimationHangmanLives(Animation):
    def __init__(self):
        super().__init__([
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=======
''','''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=======
''','''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=======
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=======
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=======
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=======
''','''
  +---+
  |   |
      |
      |
      |
      |
=======
'''
        ])