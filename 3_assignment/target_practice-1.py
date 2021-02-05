#2/5/2021
#Debra Sparr
#Assignment 3 - graphics

from graphics import *


def draw_target():
    """ Creating a target using graphics.py """
    using_graphics = True
    win = GraphWin('Archery Target', 400, 400)
    win.setBackground('grey')
    instructions = Text(Point(100, 15), text="Press 'q' to end process")
    instructions.setSize(12)
    instructions.setTextColor('black')
    instructions.draw(win)

    circle_colors_tuple = ('black', 'blue', 'red', 'yellow')

    try :
        while win :
            center = Point(200, 200)
            circle_1 = Circle(center, 160)
            circle_1.setFill('white')
            circle_1.draw(win)
            current_radius = circle_1.getRadius()

            for i in range(4):
                current_radius = shrink_radius(current_radius)
                new_circ = Circle(center, current_radius)
                new_circ.setFill(circle_colors_tuple[i])
                new_circ.draw(win)

            if win.getKey() == 'q':
                raise GraphicsError

    except GraphicsError :
        print('Application closed')
    except Exception as err :
        print(f'Some error occurred : {err}')


def shrink_radius(radius):
    return radius-30

if __name__ == '__main__' :
    draw_target()