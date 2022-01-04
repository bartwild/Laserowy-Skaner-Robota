import math
import configparser
from PIL import Image
from RobotIO import RobotIO
from bresenham import bresenham
import argparse
import sys
import copy


class WrongImageSizeError(Exception):
    pass


class Robot():
    """
    Class Robot. Contains attributes:
    :param im: Image we're working on
    :type im: object from PIL

    :param x: Robot's position on horizontal axix. 0 is on left.
    :type x: int

    :param y: Robot's position on vertical axix. 0 is on top.
    :type y: int

    :param alpha: Robot's direction angle on the beginning. Read like degrees.
    :type alpha: int

    :param total_range: Robot's angle of total rotation. Read like degrees.
    :type a_range: int

    :param rotation_range: Robot's angle of single rotation. Read like degrees.
    :type rotation_range: int

    :param height: image height.
    :type height: int

    :param width: image width.
    :type width: int
    """

    def __init__(self, img_path, config, robotio):
        """
        Assignment of Variables, opening image and config.
        """
        self._robotio = robotio
        self._total_range = int(config["total_angle"])
        self._rotation_range = int(config["rotation_angle"])
        self._width = int(config["image_width"])
        self._height = int(config["image_height"])
        self._im = self.open_image(img_path)
        values = self._robotio.text_into_numbers()
        self._x = values["x"]
        self._y = values["y"]
        self._alpha = values["alpha"]

    def open_image(self, img_path):
        """
        Opening image for Robot.
        """
        im1 = Image.open(img_path)
        im = copy.deepcopy(im1)
        im = im.convert("RGB")
        im1.close()
        w, h = im.size
        if w != self._width or h != self._height:
            raise WrongImageSizeError(f'Image must be {self._width}x{self._height}px')
        return im

    def black_pixels(self):
        black_pixels_list = []
        for x in range(self._width):
            for y in range(self._height):
                if self._im.getpixel((x, y)) == (0, 0, 0):
                    black_pixels_list.append((x, y))
        return black_pixels_list

    def rgb_of_pixel(self, x, y):
        """
        Returns color of pixel in RGB format
        """
        RGB = self._im.getpixel((x, y))
        return RGB

    def color_pixels(self, pixel_list):
        """
        Colors the pixels in RGB format - Red color
        """
        for pixels in pixel_list:
            self._im.putpixel((pixels), (255, 0, 0))

    def ending_point_for_bresenham(self, angle):
        """
        Calculate end of line that would go through whole image -
        for the best approximation.
        """
        current_angle_degrees = (self._alpha + (self._rotation_range * angle)
                                 - (self._total_range/2)) % 360
        current_angle = (current_angle_degrees * math.pi) / 180
        a = math.tan(current_angle)
        new_x = self._x
        new_y = self._y

        if current_angle_degrees == 90:
            return (new_x, 0)

        elif current_angle_degrees == 270:
            return (new_x, self._height)

        elif current_angle_degrees > 90 and current_angle_degrees < 270:
            while new_x > 0 and new_y > 0 and\
                   new_x < self._width and new_y < self._height:
                new_x -= 1
                new_y += a
            return(new_x, new_y)

        elif (current_angle_degrees > 270 and current_angle_degrees <= 360) or\
             (current_angle_degrees >= 0 and current_angle_degrees < 90):
            while new_x > 0 and new_y > 0 and\
                   new_x < self._width and new_y < self._height:
                new_x += 1
                new_y -= a
            return(new_x, new_y)

    def draw_a_line_calculate_distance(self):
        """
        Calls function bresenham for every angle in estabilished range.
        Next calls method to color pixels.
        Result is given to save method in RobotIO.
        """
        distance = []
        black_pixels = self.black_pixels()
        for angle in range(int(self._total_range/(self._rotation_range) + 1)):
            end_point = self.ending_point_for_bresenham(angle)
            wyniki = bresenham(black_pixels, (self._x, self._y),
                               end_point, self._width, self._height)
            distance.append(wyniki[0])
            self.color_pixels(wyniki[1])
        self._robotio.save_to_file(distance, self._im)


def main(arguments):
    """
    Function that uses argparse to parse the command line arguments.
    Else it assigns the default arguments that were given in exercise.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--text-path", default="parametry.txt")
    parser.add_argument("--image-path", default="otoczenie.png")
    parser.add_argument("--text-res_path", default="wyniki.txt")
    parser.add_argument("--image-res_path", default="symulacja.png")
    parser.add_argument("--config", default="config.txt")
    args = parser.parse_args(arguments[1:])
    config_parser = configparser.ConfigParser()
    config_parser.read(args.config)
    config = {"image_width": config_parser["DEFAULT"]["image_width"],
              "image_height": config_parser["DEFAULT"]["image_height"],
              "rotation_angle": config_parser["DEFAULT"]["rotation_angle"],
              "total_angle": config_parser["DEFAULT"]["total_angle"]}
    with open(args.text_path) as text_file:
        robotio = RobotIO(text_file, args.text_res_path,
                          args.image_res_path, config)
        robot = Robot(args.image_path, config, robotio)
        robot.draw_a_line_calculate_distance()


if __name__ == "__main__":
    main(sys.argv)
