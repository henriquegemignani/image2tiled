

def test_detect(rotation_detector, extract_results_2x2):
    rotation_results = rotation_detector.detect(extract_results_2x2)
    assert len(rotation_results.unique_images) == 7
    assert len(rotation_results.tiles) == 12
    assert len(rotation_results.by_position) == 15