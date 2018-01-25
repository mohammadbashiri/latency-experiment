import itertools
import pyglet 
import ratcave as rc
import numpy as np

OSCILLATE = True

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
win = pyglet.window.Window(resizable=True, screen=screen, fullscreen=True)


plane = rc.WavefrontReader(rc.resources.obj_primitives).get_mesh('Plane', drawmode=rc.POINTS)
plane.point_size = 4.
plane.position.xyz = 0, 0, -2
plane.rotation.x = 0
plane.scale.xyz = .2


colors = (
	[1., 1., 1.],
	[1., 0., 0.],
	[0., 1., 0.],
	[0., 0., 1.],
	[1., 1., 0.],
	[0., 1., 1.],
	[1., 0., 1.],
)

@win.event
def on_draw():
    win.clear()
    with rc.default_shader:
        for x, color in zip(np.linspace(0, .15, 7), colors):
            plane.position.x = x
            plane.uniforms['diffuse'] = color
            plane.draw()

	
ys = itertools.cycle([.1, 0])
def update(dt, ys):
	if OSCILLATE:
		plane.position.y = next(ys)
	
pyglet.clock.schedule(update, ys)

pyglet.app.run()