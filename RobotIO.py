class WrongAmountOfDataError(Exception):
    pass


class WrongCoordinatesError(Exception):
    pass


class RobotIO():
    """
    Class RobotIO. Contains attributes:
    :param text_handle: handle to text file with info about Robot
    :type text_path: str

    :param text_res_path: Path where to save text results.
    :type img_path: str

    :param img_res_path: Path where to save graphic results.
    :type img_res_path: str

    :param ht: image height.
    :type h: int

    :param w: image width.
    :type w: int
    """
    def __init__(self, text_handle, text_res_path, img_res_path, config):
        self._text_handle = text_handle
        self._text_res_path = text_res_path
        self._img_res_path = img_res_path
        self._w = int(config["image_width"])
        self._h = int(config["image_height"])

    def text_into_numbers(self):
        """
        Returning values of variables which are given in txt file.
        """
        lines = [row.strip() for row in self._text_handle if row.strip()]
        if len(lines) != 3:
            print(lines)
            raise WrongAmountOfDataError("Should be given x, y, alpha")
        lines_2 = {}
        for i in range(len(lines)):
            line1 = lines[i].split("=")[0].strip()
            line2 = lines[i].split("=")[1].strip()
            if line1.lower() == "x":
                if int(line2) > self._w or int(line2) < 0:
                    raise WrongCoordinatesError(f'x is between [0, {self._w}]')
                lines_2["x"] = int(line2)
            elif line1.lower() == "y":
                if int(line2) > self._h or int(line2) < 0:
                    raise WrongCoordinatesError(f'y is between [0, {self._h}]')
                lines_2["y"] = int(line2)
            else:
                lines_2["alpha"] = int(line2)
        return lines_2

    def save_to_file(self, distance, im):
        """
        Save all progresses to files.
        """
        file = open(self._text_res_path, "w")
        for single_line in distance:
            file.write(f'{single_line}\n')
        file.close()
        im.save(self._img_res_path)
