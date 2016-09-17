import argparse
import json
import math
import os

from image2tiled.image_exporter import ImageExporter
from image2tiled.image_reader import ImageReader
from image2tiled.tile_extractor import TileExtractor
from image2tiled.tiled_generator import TiledGenerator


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-directory", default=os.getcwd(), help="The directory to where save the files.")
    parser.add_argument("--max-image-size", type=int, default=2048,
                        help="Generated won't have a dimension bigger than this.")
    parser.add_argument("--tile-size", type=int, required=True, help="The tile size to cut the image with.")
    parser.add_argument("--no-rotation", dest="rotation", default=True, action='store_false',
                        help="Don't generate rotated or flipped tiles.")
    parser.add_argument("layers", nargs='+', help="The image to cut.")
    return parser


def save_output(output_directory, map_name, tiled_json, images):
    for image in images:
        image.save(os.path.join(output_directory,
                                image.filename))
    with open(os.path.join(output_directory,
                           map_name + ".json"), "w") as output_json_file:
        json.dump(tiled_json, output_json_file)


def handle_args(args):
    tile_extractor = TileExtractor(has_rotations=args.rotation)
    images_per_row = math.floor(args.max_image_size / args.tile_size)

    num_tiles = ImageReader(args.layers[0], args.tile_size).num_tiles
    tiled_generator = TiledGenerator(args.tile_size, num_tiles, images_per_row)

    generated_images = []
    for layer_image in args.layers:
        reader = ImageReader(layer_image, args.tile_size)

        assert num_tiles == reader.num_tiles, "Layer {} has {} tiles, instead of expected {}".format(layer_image,
                                                                                                     reader.num_tiles,
                                                                                                     num_tiles)
        rotation_results = tile_extractor.extract(reader)
        final_image = ImageExporter().create(rotation_results.unique_images,
                                             images_per_row)
        image_filename, ext = os.path.splitext(os.path.basename(layer_image))
        final_image.filename = image_filename + "-tilemap" + ext

        assert final_image.width <= args.max_image_size, "Generated image is wider than allowed"
        assert final_image.height <= args.max_image_size, "Generated image is heigher than allowed"
        generated_images.append(final_image)
        tiled_generator.add_layer(rotation_results, final_image)

    tiled_json = tiled_generator.json()
    save_output(args.output_directory, "map", tiled_json, generated_images )


def main():
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)