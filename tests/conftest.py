import pytest
import os

_path = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def image_2x2():
    return os.path.join(_path, "sample_files", "2x2.png")


@pytest.fixture
def reader_2x2(image_2x2):
    import image2tiled.image_reader
    return image2tiled.image_reader.ImageReader(image_2x2, 2)