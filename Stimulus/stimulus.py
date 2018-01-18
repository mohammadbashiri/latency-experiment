from pyglet.gl import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window(resizable=True)

print(window.height, window.width)

fac = 75
size_h = 20
size_w = 20


# label = pyglet.text.Label('Hello, world',
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')

# Create the update function, for pyglet to run!
def update(dt):
    pass

pyglet.clock.schedule(update)

@window.event
def on_draw():

    pyglet.graphics.draw(4, pyglet.gl.GL_POLYGON,
    ('v2f', (window.width/2 - size_w/2, window.height/2 - size_h/2,
             window.width/2 - size_w/2, window.height/2 + size_h/2,
             window.width/2 + size_w/2, window.height/2 + size_h/2,
             window.width/2 + size_w/2, window.height/2 - size_h/2))
    )


pyglet.app.run()