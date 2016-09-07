

class TileExtractor:
    def extract(self, reader):
        num_col, num_row = reader.num_tiles

        images_by_bytes = {}

        row = 0
        for col in range(num_col):
            image = reader.get_tile(col, row)
            image_bytes = image.tobytes()
            if image_bytes not in images_by_bytes:
                images_by_bytes[image_bytes] = image

        return images_by_bytes