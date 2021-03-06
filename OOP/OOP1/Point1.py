import math
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
def print_point(p):
    print(f'({p.x},{p.y})')
    
# mich = Point()
# print(mich)
# print(type(mich))
# print(mich.__doc__)
# mich.x = 2
# mich.y = 3
# print(mich.x, mich.y)

# print_point(mich)

# print(hasattr(mich, 'x'))
# print(hasattr(mich, 'z'))
# print(dir(mich))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    d_x = p2.x - p1.x
    d_y = p2.y - p1.y
    d = math.sqrt(d_x ** 2 + d_y ** 2)
    return d


# another_point = Point()
# another_point.x = 6
# another_point.y = 8
# another_point.x, another_point.y = 6, 8

# print_point(mich)
# print_point(another_point)
# print(distance_between_points(mich, another_point))


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

# print(distance_between_points(mich, box.corner))
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 30
box.corner.y = 40

def find_center(box):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    center = Point()
    center.x = box.corner.x + box.width / 2
    center.y = box.corner.y + box.height / 2
    return center


# center_of_box = find_center(box)
# print_point(center_of_box)


def grow_rectangle(box, cw, ch):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    box.width += cw
    box.height += ch


def print_rectangle(box):
    """
    prints the width, height and lower-left corner of the given Rectangle object
    """
    print(f"width: {box.width}, height:{box.height}")
    print("the lower-left corner:")
    print_point(box.corner)


# print_rectangle(box)
# grow_rectangle(box, 100, 100)
# print("After growing...")
# print_rectangle(box)


def main():
    my_point = Point()
    print(Point.__doc__)
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    print('Is my_point an instance of Point?', isinstance(my_point, Point))
    print('Is my_point an instance of Rectangle?',isinstance(my_point, Rectangle))
    print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 70
    box.corner.y = 80

    print('Does box have an attribute x?', hasattr(box, 'x'))
    print('Does box have an attribute corner?', hasattr(box, 'corner'))
    print('Rectangle has these:', dir(box))

    center = find_center(box)
    print_point(center)
    print_rectangle(box)
    grow_rectangle(box, 50, 100)
    print_rectangle(box)


if __name__ == "__main__":
    main()
