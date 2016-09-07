import collections


RotatedTile = collections.namedtuple("RotatedTile", ["image", "rotation"])

class RotationDetector:
    Results = collections.namedtuple("Results", ["unique_images", "tiles", "by_position"])

    def detect(self, extraction_results):
        pass
