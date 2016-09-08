from mock import patch, MagicMock, ANY
import image2tiled.cli


@patch("image2tiled.cli.create_parser")
@patch("image2tiled.cli.handle_args")
def test_main(mock_handle_args, mock_create_parser):
    image2tiled.cli.main()
    mock_create_parser.assert_called_once_with()
    parser = mock_create_parser.return_value
    parser.parse_args.assert_called_once_with()
    mock_handle_args.assert_called_once_with(parser.parse_args.return_value)


# @patch("image2tiled.image_reader.ImageReader")
# @patch("image2tiled.tile_extractor.TileExtractor")
# @patch("image2tiled.rotation_detector.RotationDetector")
# @patch("image2tiled.image_exporter.ImageExporter")
# @patch("image2tiled.tiled_generator.TiledGenerator")
# @patch("image2tiled.cli.save_output")
# def test_handle_args(mock_save_output, mock_tiled_generator, mock_image_exporter, mock_rotation_detector,
#                      mock_tile_extractor, mock_image_reader):
#     args = MagicMock()
#     extract = mock_tile_extractor.return_value.extract
#     detect = mock_rotation_detector.return_value.detect
#     create = mock_image_exporter.return_value.create
#
#     image2tiled.cli.handle_args(args)
#     mock_image_reader.assert_called_once_with(args.map_image, args.tile_size)
#     extract.assert_called_once_with(mock_image_reader.return_value)
#     detect.assert_called_once_with(extract.return_value)
#     create.assert_called_once_with(detect.return_value.unique_images, ANY)