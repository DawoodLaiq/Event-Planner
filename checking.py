from ursina import *
from direct.actor.Actor import Actor
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.primitives import *
from ursina.shaders import fxaa_shader
from ursina.shaders import lit_with_shadows_shader
from ursina.shaders import basic_lighting_shader as bls
from air_conditioner import Air_Conditioner
from fans import Fan
from speakers import Speaker
from lights import Light
from tv import TV
app = Ursina(use_ingame_console=True)

Entity.default_shader = bls
Draggable.default_shader = bls
EditorCamera()
#Ground = Entity(model="plane",scale=(200,1,200),collision="box",position=(0,0,0),texture="Assets/daudsons_logo.jpeg",shader=None)

#e = Entity(model="Assets/bin.obj",position=(0,0,0),rotation=(0,0,0),scale=0.001,collider='box')
e2 = TV(position=(0,1,0),cost=500,power=200)

ground = Entity(model='plane', scale=(100, 1, 100), texture='white_cube',color=color.gray, shader=lit_with_shadows_shader)

#camera.position = (10, 10, -10)
app.run()

