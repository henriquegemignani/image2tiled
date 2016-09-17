import json
import os

import pytest

import image2tiled.tiled_generator

_path = os.path.dirname(os.path.abspath(__file__))


def test_json(image_exporter, tile_extractor, reader_4x4, tiled_4x4):
    rotation_results = tile_extractor.extract(reader_4x4)
    new_image = image_exporter.create(rotation_results.unique_images, 20)
    new_image.filename = "4x4_tiles.png"
    with open(tiled_4x4) as tiled_4x4_file:
        tiled_4x4_data = json.load(tiled_4x4_file)

    tiled = image2tiled.tiled_generator.TiledGenerator(reader_4x4.tile_size,
                                                       reader_4x4.num_tiles)
    tiled.add_layer(rotation_results, new_image, tiles_per_row=6)
    assert tiled.json() == tiled_4x4_data


@pytest.mark.parametrize("filename", [
    "example_4_small1",
    "example_4_small2",
    "example_4_original",
])
def test_json_full_16x16(image_exporter, tile_extractor, filename):
    import image2tiled.image_reader
    reader = image2tiled.image_reader.ImageReader(os.path.join(_path, "sample_files", filename + ".png"), 16)
    results = tile_extractor.extract(reader)
    images_per_row = 128

    new_image = image_exporter.create(results.unique_images, images_per_row)
    new_image.filename = filename + "-tilemap.png"
    with open(os.path.join(_path, "sample_files", filename + ".json")) as tiled_file:
        tiled_data = json.load(tiled_file)

    tiled = image2tiled.tiled_generator.TiledGenerator(reader.tile_size,
                                                       reader.num_tiles)
    tiled.add_layer(results, new_image, tiles_per_row=images_per_row)
    assert tiled.json() == tiled_data
