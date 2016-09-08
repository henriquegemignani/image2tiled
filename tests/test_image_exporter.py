from mock import patch, call, ANY
import math
import pytest


class MockImage:
    pass


@pytest.mark.parametrize("tile_size, num_images, images_per_row", [
(8, 6, 4),
(16, 6, 4),
(16, 50, 1),
(16, 1, 50),
(16, 50, 50),
])
@patch("PIL.Image.new")
def test_create(mock_image_new, image_exporter, tile_size, num_images, images_per_row):
    images = [MockImage() for _ in range(num_images)]
    images[0].width = tile_size
    images[0].height = tile_size

    new_image = image_exporter.create(images, images_per_row)
    box = (tile_size*min(images_per_row, num_images), tile_size*math.ceil(num_images / images_per_row))

    mock_image_new.assert_called_once_with("RGBA", box)
    assert new_image == mock_image_new.return_value
    new_image.paste.assert_has_calls([
        call(image, ANY)
        for image in images
    ])
