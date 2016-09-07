from PIL import Image


class ImageReader:
    def __init__(self, image_name, tile_size, margin=0):
        self.image = Image.open(image_name)
        self.tile_size = tile_size
        self.margin = margin

    def get_tile(self, tile_x, tile_y):
        pos_x = (self.tile_size * tile_x) + (self.margin * (tile_x + 1))
        pos_y = (self.tile_size * tile_y) + (self.margin * (tile_y + 1))
        box = (pos_x, pos_y, pos_x + self.tile_size, pos_y + self.tile_size)
        return self.image.crop(box)

    @property
    def num_tiles(self):
        actual_tile_size = self.tile_size + self.margin
        return self.image.width / actual_tile_size, self.image.height / actual_tile_size
