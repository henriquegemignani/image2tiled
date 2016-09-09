
def test_extract(tile_extractor, reader_2x2):
    results = tile_extractor.extract(reader_2x2)
    assert len(results.unique_images) == 12
    assert len(results.by_position) == 15
    assert results.by_position[(2, 0)] == results.by_position[(3, 0)]
    unique_images = list(results.unique_images)
    assert unique_images[0] == results.by_position[(0, 0)]
    assert unique_images[2] == results.by_position[(2, 0)]


def test_detect_2x2(tile_extractor, extract_results_2x2):
    rotation_results = tile_extractor.detect(extract_results_2x2)
    assert len(rotation_results.unique_images) == 7
    assert len(rotation_results.by_position) == 15
    unique_images = list(rotation_results.unique_images)
    assert unique_images[0].tobytes() == rotation_results.by_position[(0, 0)].image.tobytes()
    assert unique_images[2].tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()
    assert rotation_results.by_position[(0, 2)].image.tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()


def test_detect_4x4(tile_extractor, extract_results_4x4):
    rotation_results = tile_extractor.detect(extract_results_4x4)
    assert len(rotation_results.unique_images) == 6
    assert len(rotation_results.by_position) == 16
    unique_images = list(rotation_results.unique_images)
    assert unique_images[0].tobytes() == rotation_results.by_position[(0, 0)].image.tobytes()
    assert unique_images[1].tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()
    assert rotation_results.by_position[(0, 1)].image.tobytes() == rotation_results.by_position[(1, 0)].image.tobytes()