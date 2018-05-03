import pyglet
pyglet.options['debug_gl'] = False
pyglet.options['debug_gl_trace'] = False
import ratcave as rc
import natnetclient as natnet

# initiate a natnet object
client = natnet.NatClient()  # read_rate=1000
LED = client.rigid_bodies['LED']

# create a window and project it on the display of your choice
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
mywin = pyglet.window.Window(fullscreen=True, screen=screen, vsync=False)
fr = pyglet.window.FPSDisplay(mywin)

# initialize a stim object
plane = rc.WavefrontReader(rc.resources.obj_primitives).get_mesh('Plane', drawmode=rc.POINTS)
plane.point_size = 10.
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
                                                   # for 1280x720: 2.4 - 1.085
def update(dt):                                    # for 1024x768: 2.9 - 1.2
    plane.position.x = -LED.position.x * 2.4 - 1.085 # for [3] 1920x1080: 1.6 - .39
    plane.position.y = LED.position.z - .15

pyglet.clock.schedule(update)

pyglet.app.run()