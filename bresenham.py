import math


def stop(black_pixels, pixel, width, height):
    """
    Check if current pixel is black or is on border
    """
    if pixel in black_pixels or pixel[0] == width or pixel[1] == height:
        return True
    return False


def bresenham(black_pixels, start_point, end_point, width, height):
    """
    Main function that uses Bresenham's algorithm to iterate through image
    and during this - calculates distance and return list of pixels to color.
    """
    x1 = start_point[0]
    y1 = start_point[1]
    x2 = end_point[0]
    y2 = end_point[1]
    x = x1
    y = y1
    distance = 0
    pixel_list = []
    max_distance = 60
    no_hit_distance = 255

    # Calculate the direction with X axix

    if (x1 < x2):
        xi = 1
        dx = x2 - x1
    else:
        xi = -1
        dx = x1 - x2

    # Calculate the direction with Y axis

    if (y1 < y2):
        yi = 1
        dy = y2 - y1
    else:
        yi = -1
        dy = y1 - y2

    # first pixel and beggining of iterating

    end = stop(black_pixels, (x, y), width, height)
    while not end and distance < max_distance:
        pixel_list.append((x, y))
        distance = int(math.sqrt((x - x1)**2 + (y - y1)**2))

        # If we take X axix as reference

        if (dx > dy):
            ai = (dy - dx) * 2
            bi = dy * 2
            d = bi - dx

            # Iterating through X

            while (x != x2):

                while not end and distance < max_distance:

                    # Factor test

                    if (d >= 0):
                        x += xi
                        y += yi
                        d += ai
                    else:
                        d += bi
                        x += xi

                    end = stop(black_pixels, (x, y), width, height)
                    if not end:
                        pixel_list.append((x, y))
                        distance = int(math.sqrt((x - x1)**2 + (y - y1)**2))

                else:

                    break

        # If we take Y axix as reference

        else:
            ai = (dx - dy) * 2
            bi = dx * 2
            d = bi - dy

            # Iterating through Y

            while (y != y2):

                while not end and distance < max_distance:

                    # Factor test

                    if (d >= 0):
                        x += xi
                        y += yi
                        d += ai
                    else:
                        d += bi
                        y += yi

                    end = stop(black_pixels, (x, y), width, height)
                    if not end:
                        pixel_list.append((x, y))
                        distance = int(math.sqrt((x - x1)**2 + (y - y1)**2))

                else:
                    break

    if distance >= max_distance and not end:
        distance = no_hit_distance
        return [distance, pixel_list]
    return [distance, pixel_list]
