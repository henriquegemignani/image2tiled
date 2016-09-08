

def test_detect(rotation_detector, extract_results_2x2):
    rotation_results = rotation_detector.detect(extract_results_2x2)
    assert len(rotation_results.unique_images) == 7
    assert len(rotation_results.by_position) == 15
    unique_images = list(rotation_results.unique_images)
    assert unique_images[0].tobytes() == rotation_results.by_position[(0, 0)].image.tobytes()
    assert unique_images[2].tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()

    print(rotation_results.by_position[(2, 0)])
    print(rotation_results.by_position[(0, 2)])

    assert rotation_results.by_position[(0, 2)].image.tobytes() == rotation_results.by_position[(2, 0)].image.tobytes()