"""The class extends Animation class and provides a list of ascii animation frames.

For more details see the parent class docstring.
"""
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