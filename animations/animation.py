class Animation:
    def __init__(self, frames = []):
        self.frames = []
        for frame in frames:
            self.frames.append(frame.splitlines())
        self.frame_count = len(self.frames)

    def getFrame(self, index = 0):
        return self.frames[index]