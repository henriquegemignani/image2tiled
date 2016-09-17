import os

from PIL import Image

FLIPPED_HORIZONTALLY_FLAG = 0x80000000
ROTATION_FLAGS = {
    None: 0,
    Image.ROTATE_90: 0x60000000,
    Image.ROTATE_180: 0xc0000000,
    Image.ROTATE_270: 0xa0000000
}


class TiledGenerator:
    def __init__(self, tile_size, num_tiles, tiles_per_row=8):
        self.layers = []
        self.tile_sets = []
        self.next_gid = 1
        self.tile_size = tile_size
        self.num_columns, self.num_rows = num_tiles
        self.tiles_per_row = tiles_per_row

    def add_layer(self, rotation_results, final_image, layer_name=None):
        index_for_image = {i.tobytes(): v for v, i in enumerate(rotation_results.unique_images)}

        if layer_name is None:
            layer_name = "Tile Layer {}".format(1 + len(self.layers))

        def encode_data():
            data = []
            for row in range(self.num_rows):
                for column in range(self.num_columns):
                    rotated_tile = rotation_results.by_position[(column, row)]
                    index = self.next_gid + index_for_image[rotated_tile.image.tobytes()]
                    # TODO: add rotation flags
                    horizontal_flip, rotation_flip = rotated_tile.rotation
                    if horizontal_flip is not None:
                        index |= FLIPPED_HORIZONTALLY_FLAG
                    index |= ROTATION_FLAGS[rotation_flip]
                    data.append(index)
            return data
        self.layers.insert(0, {
            "data": encode_data(),
            "height": self.num_rows,
            "name": layer_name,
            "opacity": 1,
            "type": "tilelayer",
            "visible": True,
            "width": self.num_columns,
            "x": 0,
            "y": 0
        })
        self.tile_sets.append({
            "columns": self.tiles_per_row,
            "firstgid": self.next_gid,
            "image": final_image.filename,
            "imageheight": final_image.height,
            "imagewidth": final_image.width,
            "margin": 0,
            "name": os.path.splitext(final_image.filename)[0],
            "spacing": 0,
            "tilecount": len(rotation_results.unique_images),
            "tileheight": self.tile_size,
            "tilewidth": self.tile_size
        })
        self.next_gid += len(rotation_results.unique_images)

    def json(self):
        return {
            "height": self.num_rows,
            "layers": self.layers,
            "nextobjectid": 1,
            "orientation": "orthogonal",
            "renderorder": "right-down",
            "tileheight": self.tile_size,
            "tilesets": self.tile_sets,
            "tilewidth": self.tile_size,
            "version": 1,
            "width": self.num_columns
        }