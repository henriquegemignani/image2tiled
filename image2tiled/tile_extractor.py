import collections


class TileExtractor:
    Results = collections.namedtuple("Results", ["unique_images", "by_position"])

    def extract(self, reader):
        num_cols, num_rows = reader.num_tiles

        unique_images = collections.OrderedDict()
        by_position = {}

        for row in range(num_rows):
            for col in range(num_cols):
                image = reader.get_tile(col, row)
                image_bytes = image.tobytes()
                if image_bytes not in unique_images:
                    unique_images[image_bytes] = image
                by_position[(col, row)] = image_bytes

        return TileExtractor.Results(unique_images, by_position)