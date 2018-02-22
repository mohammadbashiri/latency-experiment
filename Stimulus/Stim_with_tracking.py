import pyglet
pyglet.options['debug_gl'] = False
pyglet.options['debug_gl_trace'] = False
import ratcave as rc
import natnetclient as natnet
from Stimulus.stimulus import Stimulus

# initiate a natnet object
client = natnet.NatClient()
LED = client.rigid_bodies['LED']

# create a window and project it on the display of your choice
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
mywin = pyglet.window.Window(fullscreen=True, screen=screen, vsync=False)
fr = pyglet.window.FPSDisplay(mywin)

# initialize a stim object
plane = rc.WavefrontReader(rc.resources.obj_primitives).get_mesh('Plane', drawmode=rc.POINTS)
plane.point_size = 4.
plane.position.xyz = 0, 0, -3
plane.rotation.x = 0
plane.scale.xyz = .2
# plane.uniforms['diffuse'] = [0., 0., 0.]

@mywin.event
def on_draw():
    mywin.clear()
    with rc.default_shader:
        plane.draw()


    # fr.draw()
    # print(plane.position, LED.position)

def update(dt):
    plane.position.x = -LED.position.x * 1.65 - .388
    plane.position.y = LED.position.z * 1

pyglet.clock.schedule(update)

pyglet.app.run()