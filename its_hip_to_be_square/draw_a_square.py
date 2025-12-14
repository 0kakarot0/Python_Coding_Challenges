import os
import time

from termcolor import colored


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def set_pos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def hits_wall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(''.join([col[y] for col in self._canvas]))


class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.mark = "*"
        self.trail = '#'
        self.pos = [0, 0]
        self.framerate = 0.2

    def move(self, dx, dy):
        pos = [self.pos[0] + dx, self.pos[1] + dy]
        self.draw_if_not_hit_on_wall(pos)

    def up(self):
        self.move(0, -1)

    def down(self):
        self.move(0, 1)

    def right(self):
        self.move(1, 0)

    def left(self):
        self.move(-1, 0)

    def draw(self, pos):
        self.canvas.set_pos(self.pos, self.trail)
        self.pos = pos
        self.canvas.set_pos(self.pos, colored(self.mark, 'yellow'))
        self.canvas.set_pos(self.pos, self.mark)
        self.canvas.print()
        time.sleep(self.framerate)

    def draw_if_not_hit_on_wall(self, pos):
        if not self.canvas.hits_wall(pos):
            self.draw(pos)

    def draw_square(self, size):
        for i in range(0, size):
            self.right()
        for i in range(0, size//2):
            self.down()
        for i in range(0, size):
            self.left()
        for i in range(0, size//2):
            self.up()


canvas = Canvas(30, 30)
scribe = TerminalScribe(canvas)
scribe.draw_square(8)

