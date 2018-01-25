import pyglet
import itertools
import numpy as np

class plane:

    def __init__(self, window=None, x=0, y=0, width=1, height=1, color=(255, 0, 0)):

        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color * 4

        self.vertices = pyglet.graphics.vertex_list(4,
                                                    ('v2i', (self._x - self._width//2, self._y - self._height//2,
                                                             self._x - self._width//2, self._y + self._height//2,
                                                             self._x + self._width//2, self._y + self._height//2,
                                                             self._x + self._width//2, self._y - self._height//2)),
                                                    ('c3B', self._color)
                                                    )

class Stimulus:

    def __init__(self, window=None, type='POINT', x=0, y=0, width=1, height=1, color=(255, 255, 255)):

        self.type = type
        self._win = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        self._height = val

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        self._color = val

    def draw(self):
        if self.type == 'POINT':
            self._obj = plane(window=self._win, x=self.x, y=self.y,
                              width=self.width, height=self.height, color=self.color)
            self._obj.vertices.draw(pyglet.gl.GL_POLYGON)



if __name__ == '__main__':

    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_screens()[1]
    mywin = pyglet.window.Window(fullscreen=True, screen=screen)

    # initialize a stim object
    mypoint = Stimulus(window=mywin, type='POINT', x=mywin.width//2, y=mywin.height//2, width=10, height=10)


    @mywin.event
    def on_draw():
        mywin.clear()
        mypoint.draw()

    heights = itertools.cycle([100,10])
    colors = itertools.cycle([(255, 0, 0),(0, 255, 0)])
    def update(dt):
        Stimulus.x = next(heights)
        Stimulus.color = next(colors)

    pyglet.clock.schedule_interval(update, 1)

    pyglet.app.run()