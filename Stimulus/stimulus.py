from pyglet.gl import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window(resizable=True)

print(window.height, window.width)

fac = 75
size_h = 20
size_w = 20

@window.event
def on_draw():

    pyglet.graphics.draw(4, pyglet.gl.GL_POLYGON,
    ('v2f', (window.width/2 - size_w/2, window.height/2 - size_h/2,
             window.width/2 - size_w/2, window.height/2 + size_h/2,
             window.width/2 + size_w/2, window.height/2 + size_h/2,
             window.width/2 + size_w/2, window.height/2 - size_h/2))
    # ('c3b', (255, 255, 255,
    #          255, 255, 255,
    #          255, 255, 255,
    #          255, 255, 255))

    )


pyglet.app.run()