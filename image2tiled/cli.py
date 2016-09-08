import argparse
import os
import math
from image2tiled.image_reader import ImageReader
from image2tiled.tile_extractor import TileExtractor
from image2tiled.rotation_detector import RotationDetector
from image2tiled.image_exporter import ImageExporter


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-directory", default=os.getcwd(), help="The directory to where save the files.")
    parser.add_argument("--max-image-size", type=int, default=2048, help="Generated won't have a dimension bigger than this.")
    parser.add_argument("--tile-size", type=int, required=True, help="The tile size to cut the image with.")
    parser.add_argument("map_image", help="The image to cut.")
    return parser


def handle_args(args):
    reader = ImageReader(args.map_image, args.tile_size)
    extraction_results = TileExtractor().extract(reader)
    rotation_results = RotationDetector().detect(extraction_results)

    final_image = ImageExporter().create(rotation_results.unique_images,
                                         math.floor(args.max_image_size / args.tile_size))

    file, ext = os.path.splitext(os.path.dirname(args.map_image))
    final_image.save(os.path.join(args.output_directory,
                                  file + "-tilemap" + ext))


def main():
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)