import pytest
import os

_path = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def image_2x2():
    return os.path.join(_path, "sample_files", "2x2.png")


@pytest.fixture()
def image_4x4():
    return os.path.join(_path, "sample_files", "4x4.png")


@pytest.fixture
def reader_2x2(image_2x2):
    import image2tiled.image_reader
    return image2tiled.image_reader.ImageReader(image_2x2, 2)


@pytest.fixture
def reader_4x4(image_4x4):
    import image2tiled.image_reader
    return image2tiled.image_reader.ImageReader(image_4x4, 4)


@pytest.fixture()
def tile_extractor():
    import image2tiled.tile_extractor
    return image2tiled.tile_extractor.TileExtractor()


@pytest.fixture()
def rotation_detector():
    import image2tiled.rotation_detector
    return image2tiled.rotation_detector.RotationDetector()


@pytest.fixture()
def extract_results_2x2(tile_extractor, reader_2x2):
    return tile_extractor.extract(reader_2x2)