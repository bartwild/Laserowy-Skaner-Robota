from Robot import Robot, WrongImageSizeError
from RobotIO import RobotIO
import pytest
from io import StringIO
from PIL import UnidentifiedImageError
import os


def test_change_color():
    handle = StringIO(
        "x = 135\n"
        + "y = 90\n"
        + "α = 90\n"
    )
    config = {"image_width": "320",
              "image_height": "240",
              "rotation_angle": "10",
              "total_angle": "180"}
    robotio = RobotIO(handle, "wyniki.txt", "symulacja.png", config)
    robot = Robot("otoczenie.png", config, robotio)
    assert robot.rgb_of_pixel(200, 100) == (255, 255, 255)
    robot.color_pixels([(200, 100)]) == (255, 0, 0)
    assert robot.rgb_of_pixel(200, 100) == (255, 0, 0)


def test_ending_point():
    handle = StringIO(
        "x = 135\n"
        + "y = 90\n"
        + "α = 90\n"
    )
    config = {"image_width": "320",
              "image_height": "240",
              "rotation_angle": "10",
              "total_angle": "180"}
    robotio = RobotIO(handle, "wyniki.txt", "symulacja.png", config)
    robot = Robot("otoczenie.png", config, robotio)
    assert robot.ending_point_for_bresenham(0) == (320, 90)


def test_single_line_in_program():
    handle = StringIO(
        "x = 135\n"
        + "y = 90\n"
        + "α = 90\n"
    )
    config = {"image_width": "320",
              "image_height": "240",
              "rotation_angle": "10",
              "total_angle": "180"}
    robotio = RobotIO(handle, "test_wyniki.txt", "test_symulacja.png", config)
    robot = Robot("otoczenie.png", config, robotio)
    assert robot.ending_point_for_bresenham(0) == (320, 90)
    robot.draw_a_line_calculate_distance()
    assert robot.rgb_of_pixel(135, 89) == (255, 0, 0)
    os.remove("test_wyniki.txt")
    os.remove("test_symulacja.png")


def test_image_path_not_image():
    handle = StringIO(
        "x = 135\n"
        + "y = 90\n"
        + "α = 90\n"
    )
    config = {"image_width": "320",
              "image_height": "240",
              "rotation_angle": "10",
              "total_angle": "180"}
    robotio = RobotIO(handle, "wyniki.txt", "symulacja.png", config)
    with pytest.raises(UnidentifiedImageError):
        Robot("parametry.txt", config, robotio)


def test_wrong_image_size():
    handle = StringIO(
        "x = 135\n"
        + "y = 90\n"
        + "α = 90\n"
    )
    config = {"image_width": "320",
              "image_height": "240",
              "rotation_angle": "10",
              "total_angle": "180"}
    robotio = RobotIO(handle, "wyniki.txt", "symulacja.png", config)
    with pytest.raises(WrongImageSizeError):
        Robot("kreski.png", config, robotio)
