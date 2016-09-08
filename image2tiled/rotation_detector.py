from PIL import Image
import collections


RotatedTile = collections.namedtuple("RotatedTile", ["image", "rotation"])


def _flip(image, method):
    if method is None:
        return image
    else:
        return image.transpose(method)


def _create_flips(image):
    results = []
    for horizontal_flip in (None, Image.FLIP_LEFT_RIGHT):
        h_flip_image = _flip(image, horizontal_flip)
        for rotation_flip in (None, Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270):
            results.append((_flip(h_flip_image, rotation_flip), (horizontal_flip, rotation_flip)))
    return results



class RotationDetector:
    Results = collections.namedtuple("Results", ["unique_images", "by_position"])

    def detect(self, extraction_results):
        unique_images = []
        by_position = {}

        old_to_new_mapping = {}
        for image_bytes, image in extraction_results.unique_images.items():
            if image_bytes not in old_to_new_mapping:
                # This image is a new one
                flips = _create_flips(image)
                unique_images.append(image)
                for rot_image, rotation in flips:
                    old_to_new_mapping[rot_image.tobytes()] = RotatedTile(image, rotation)

        for tile, bytes in extraction_results.by_position.items():
            by_position[tile] = old_to_new_mapping[bytes]

        return RotationDetector.Results(unique_images, by_position)
