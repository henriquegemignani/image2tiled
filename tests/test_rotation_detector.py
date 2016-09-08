

def test_detect_2x2(rotation_detector, extract_results_2x2):
    rotation_results = rotation_detector.detect(extract_results_2x2)
    assert len(rotation_results.unique_images) == 7
    assert len(rotation_results.by_position) == 15
    unique_images = list(rotation_results.unique_images)
    assert unique_images[0].tobytes() == rotation_results.by_position[(0, 0)].image.tobytes()
    assert unique_images[2].tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()
    assert rotation_results.by_position[(0, 2)].image.tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()


def test_detect_4x4(rotation_detector, extract_results_4x4):
    rotation_results = rotation_detector.detect(extract_results_4x4)
    assert len(rotation_results.unique_images) == 6
    assert len(rotation_results.by_position) == 16
    unique_images = list(rotation_results.unique_images)
    assert unique_images[0].tobytes() == rotation_results.by_position[(0, 0)].image.tobytes()
    assert unique_images[1].tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()
    assert rotation_results.by_position[(0, 1)].image.tobytes() == rotation_results.by_position[(1, 0)].image.tobytes()