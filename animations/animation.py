"""Animation class provides a scaffold for the ascii animations used by Display class.

Typical usage example:
    from display import Display
    from animations.animationHangman import AnimationHangman
    display.animation(left_colums_animation=AnimationHangman())
"""
class Animation:
    """Animation class provides a scaffold for the ascii animation frames.

    The class stores a list of ascii animation frames.

    Arguments:
        frames:
            A list of multiline strings that each represents an frame of the ascii animation.

    Attributes:
        frame_count:
            A count of the frames in the animation.

    Methods:
        getFrame(index: int):
            Returns a frame at the specified index of ascii animation as a list of text lines.
    """
    def __init__(self, frames = [" "]):
        """Initializes the method

        The provided list of string ascii animation frames is split into a list of text lines.

        Arguments:
            frames:
                A list of multiline strings that each represents an frame of the ascii animation.
        """
        self.frames = []
        for frame in frames:
            self.frames.append(frame.splitlines())
        self.frame_count = len(self.frames)

    def getFrame(self, index = 0):
        """Return a list of the ascii animation frame at the specified index."""
        return self.frames[index]