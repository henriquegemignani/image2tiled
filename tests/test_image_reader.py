from mock import patch
import pytest
import image2tiled.image_reader


@pytest.mark.parametrize("tile_size, margin, position, result", [
    (7, 0, (0, 0), (0, 0, 7, 7)),
    (9, 0, (0, 0), (0, 0, 9, 9)),
    (7, 1, (0, 0), (1, 1, 8, 8)),
    (7, 2, (12, 12), (110, 110, 117, 117)),
])
@patch("PIL.Image.open")
def test_get_tile(mock_image_open, tile_size, margin, position, result):
    mock_image = mock_image_open.return_value
    reader = image2tiled.image_reader.ImageReader("myimage.png", tile_size, margin)

    assert reader.get_tile(*position) == mock_image.crop.return_value
    mock_image_open.assert_called_once_with("myimage.png")
    mock_image.crop.assert_called_once_with(result)


def test_num_tiles(reader_2x2):
    assert reader_2x2.num_tiles == (5, 3)
    assert type(reader_2x2.num_tiles[0]) == int
    assert type(reader_2x2.num_tiles[1]) == int
