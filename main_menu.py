from ursina import *
from tent import Tent
from ursina.shaders import basic_lighting_shader as bls

class Main_Menu(Entity):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.entities=[]
        self.daudsons_logo=Entity(model="quad", position=(2,-1,-1),scale=(6,1.5,1),texture="Assets/daudsons_logo.jpeg")
        self.entities.append(self.daudsons_logo)
        self.background=Entity(model="quad", position=(0,0,0),scale=20,texture="grass")
        self.entities.append(self.background)
        self.start_button = Button(
            text='START',
            color=color.azure,
            scale=(0.5, 0.2),
            position=(-0.5, -0.4),
            on_click=self.start
        )
        self.entities.append(self.start_button)
    def start(self):
        self.app.show_scene(self.app.main_scene)
        for e in self.entities:
            destroy(e)