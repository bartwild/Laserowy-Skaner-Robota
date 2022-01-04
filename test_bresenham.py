from bresenham import bresenham, stop


def test_stop():
    black_pixels = [(135, 119)]
    assert stop(black_pixels, (135, 119), 320, 240) is True


def test_bresenham():
    assert bresenham([(3, 5), (7, 11)], (3, 6), (10, 15),
                     20, 16) == [5, [(3, 6), (4, 7), (5, 8), (5, 9),
                                 (6, 10)]]


def test_bresenham_black_pixel_on_start():
    assert bresenham([(3, 6), (7, 11)], (3, 6), (10, 15),
                     20, 16) == [0, []]


def test_bresenham_start_on_border():
    assert bresenham([(3, 6), (7, 11)], (20, 16), (10, 15),
                     20, 16) == [0, []]


def test_bresenham_hitting_border():
    assert bresenham([(3, 6), (7, 11)], (18, 15), (26, 18),
                     20, 16) == [1, [(18, 15), (19, 15)]]


def test_bresenham_max_distance():
    wynik = [(x, 1) for x in range(1, 62)]
    assert bresenham([], (1, 1), (99, 1),
                     100, 100) == [255, wynik]
