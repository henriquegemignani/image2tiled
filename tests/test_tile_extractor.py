
def test_extract(tile_extractor, reader_2x2):
    results = tile_extractor.extract(reader_2x2)
    assert len(results.unique_images) == 12
    assert len(results.by_position) == 15
    assert results.by_position[(2, 0)] == results.by_position[(3, 0)]
    unique_images = list(results.unique_images)
    assert unique_images[0] == results.by_position[(0, 0)]
    assert unique_images[2] == results.by_position[(2, 0)]
