from RobotIO import (WrongAmountOfDataError,
                     RobotIO,
                     WrongCoordinatesError)
from Robot import Robot
from io import StringIO
import pytest
import os


def test_open_file_assign_variables():
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
    variables = robotio.text_into_numbers()
    assert variables["x"] == 135
    assert variables["y"] == 90
    assert variables["alpha"] == 90


def test_wrong_amount_of_data_given():
    config = {"image_width": "320",
              "image_height": "240",
              "rotation_angle": "10",
              "total_angle": "180"}
    handle = StringIO(
        "x = 135\n"
        + "α = 90\n"
    )

    reader = RobotIO(handle, "wyniki.txt", "symulacja.png", config)
    with pytest.raises(WrongAmountOfDataError):
        reader.text_into_numbers()


def test_wrong_data_given():
    config = {"image_width": "320",
              "image_height": "240",
              "rotation_angle": "10",
              "total_angle": "180"}
    handle = StringIO(
        "x = 335\n"
        + "y = 90\n"
        + "α = 90\n"
    )
    reader = RobotIO(handle, "wyniki.txt", "symulacja.png", config)
    with pytest.raises(WrongCoordinatesError):
        reader.text_into_numbers()


def test_save_to_file():
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
    robot.draw_a_line_calculate_distance()
    file = open("test_wyniki.txt", "r")
    assert file.readline() == "57\n"
    os.remove("test_wyniki.txt")
    os.remove("test_symulacja.png")
