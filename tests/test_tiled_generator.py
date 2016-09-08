import image2tiled.tiled_generator
import json
import pprint


def test_json(image_exporter, rotation_detector, extract_results_4x4, reader_4x4, tiled_4x4):
    rotation_results = rotation_detector.detect(extract_results_4x4)
    new_image = image_exporter.create(rotation_results.unique_images, 20)
    new_image.filename = "4x4_tiles.png"
    with open(tiled_4x4) as tiled_4x4_file:
        tiled_4x4_data = json.load(tiled_4x4_file)

    tiled = image2tiled.tiled_generator.TiledGenerator(reader_4x4.tile_size,
                                                       reader_4x4.num_tiles,
                                                       tiles_per_row=6)
    tiled.add_layer(rotation_results, new_image)
    assert tiled.json() == tiled_4x4_data