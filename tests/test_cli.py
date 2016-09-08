from mock import patch
import image2tiled.cli


@patch("image2tiled.cli.create_parser")
@patch("image2tiled.cli.handle_args")
def test_main(mock_handle_args, mock_create_parser):
    image2tiled.cli.main()
    mock_create_parser.assert_called_once_with()
    parser = mock_create_parser.return_value
    parser.parse_args.assert_called_once_with()
    mock_handle_args.assert_called_once_with(parser.parse_args.return_value)