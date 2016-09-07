from mock import patch
import pytest
import image2tiled.tile_extractor


@pytest.fixture()
def extractor():
    return image2tiled.tile_extractor.TileExtractor()


def test_extract(extractor, reader_2x2):
    assert len(extractor.extract(reader_2x2)) == 12
