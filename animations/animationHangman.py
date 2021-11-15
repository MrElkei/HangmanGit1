from animations.animation import Animation

class AnimationHangman(Animation):
    def __init__(self):
        super().__init__([
"""  
  +---+
 /    |
 O    |
/|\\   |
/ \\   |
      |
=======
""",
"""  
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=======
""",
"""  
  +---+
   \\  |
   O  |
  /|\\ |
  / \\ |
      |
=======
""",
"""  
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=======
"""
        ])