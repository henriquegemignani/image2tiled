

class TileExtractor:
    def extract(self, reader):
        num_cols, num_rows = reader.num_tiles

        images_by_bytes = {}

        for row in range(num_rows):
            for col in range(num_cols):
                image = reader.get_tile(col, row)
                image_bytes = image.tobytes()
                if image_bytes not in images_by_bytes:
                    images_by_bytes[image_bytes] = image

        return images_by_bytes