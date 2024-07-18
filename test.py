from ursina import *
from ursina.prefabs.primitives import *
from ursina.shaders import fxaa_shader
app = Ursina()
window.color=color.black

Entity(model='plane', scale=10, y=-2, texture='shore')
EditorCamera()
Entity(model='quad', color=color.red, double_sided=True)
Entity(model='quad', color=color.green, z=-.001, scale=.5, texture='circle')
camera.shader = fxaa_shader
camera.clip_plane_far=100
Sky()

def input(key):
    if key == 'space':
        if not camera.shader:
            camera.shader = fxaa_shader
        else:
            camera.shader = None


app.run()