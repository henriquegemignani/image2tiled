import argparse
import os
import math
import json
from image2tiled.image_reader import ImageReader
from image2tiled.tile_extractor import TileExtractor
from image2tiled.image_exporter import ImageExporter
from image2tiled.tiled_generator import TiledGenerator


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-directory", default=os.getcwd(), help="The directory to where save the files.")
    parser.add_argument("--max-image-size", type=int, default=2048, help="Generated won't have a dimension bigger than this.")
    parser.add_argument("--tile-size", type=int, required=True, help="The tile size to cut the image with.")
    parser.add_argument("--no-rotation", dest="rotation", default=True, action='store_false', help="BUDEGA")
    parser.add_argument("map_image", help="The image to cut.")
    return parser


def save_output(output_directory, map_name, tiled_json, images):
    for image in images:
        image.save(os.path.join(output_directory,
                                image.filename))
    with open(os.path.join(output_directory,
                           map_name + ".json"), "w") as output_json_file:
        json.dump(tiled_json, output_json_file)


def handle_args(args):
    reader = ImageReader(args.map_image, args.tile_size)
    rotation_results = TileExtractor(has_rotations=args.rotation).extract(reader)
    images_per_row = math.floor(args.max_image_size / args.tile_size)

    final_image = ImageExporter().create(rotation_results.unique_images,
                                         images_per_row)
    file, ext = os.path.splitext(os.path.basename(args.map_image))
    final_image.filename = file + "-tilemap" + ext

    assert final_image.width <= args.max_image_size, "Generated image is wider than allowed"
    assert final_image.height <= args.max_image_size, "Generated image is heigher than allowed"

    tiled_generator = TiledGenerator(args.tile_size, reader.num_tiles, images_per_row)
    tiled_generator.add_layer(rotation_results, final_image)
    tiled_json = tiled_generator.json()
    save_output(args.output_directory, file, tiled_json, [final_image])


def main():
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)