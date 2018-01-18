from pyglet.gl import *

# Direct OpenGL commands to this window.
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
window = pyglet.window.Window(resizable=True)

print(window.height, window.width)

fac = 75
size_h = 20
size_w = 20


i = 0


# Create the update function, for pyglet to run!
def update(dt):

    global red_vertex, blue_vertex, i

    if i%2 == 0:
        red_vertex = pyglet.graphics.vertex_list(4,
                                                 ('v2i', (window.width//2 - size_w//2, window.height//2 - size_h//2,
                                                          window.width//2 - size_w//2, window.height//2 + size_h//2,
                                                          window.width//2 + size_w//2, window.height//2 + size_h//2,
                                                          window.width//2 + size_w//2, window.height//2 - size_h//2)),
                                                 ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0))
                                                 )

        blue_vertex = pyglet.graphics.vertex_list(4,
                                                  ('v2i', (window.width//2 - size_w//2 - 50, window.height//2 - size_h//2,
                                                           window.width//2 - size_w//2 - 50, window.height//2 + size_h//2,
                                                           window.width//2 + size_w//2 - 50, window.height//2 + size_h//2,
                                                           window.width//2 + size_w//2 - 50, window.height//2 - size_h//2)),
                                                  ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0))
                                                  )

    else:
        red_vertex = pyglet.graphics.vertex_list(4,
                                                 ('v2i', (window.width//2 - size_w//2, window.height//2 - size_h//2,
                                                          window.width//2 - size_w//2, window.height//2 + size_h//2,
                                                          window.width//2 + size_w//2, window.height//2 + size_h//2,
                                                          window.width//2 + size_w//2, window.height//2 - size_h//2)),
                                                 ('c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
                                                 )
        blue_vertex = pyglet.graphics.vertex_list(4,
                                                  ('v2i', (window.width//2 - size_w//2 - 50, window.height//2 - size_h//2,
                                                           window.width//2 - size_w//2 - 50, window.height//2 + size_h//2,
                                                           window.width//2 + size_w//2 - 50, window.height//2 + size_h//2,
                                                           window.width//2 + size_w//2 - 50, window.height//2 - size_h//2)),
                                                  ('c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
                                                  )
    i += 1

pyglet.clock.schedule_interval(update, 1)

update(0)

@window.event
def on_draw():

    red_vertex.draw(pyglet.gl.GL_POLYGON)
    blue_vertex.draw(pyglet.gl.GL_POLYGON)

pyglet.app.run()