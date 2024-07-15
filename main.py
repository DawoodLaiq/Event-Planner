from ursina import *
from tent import Tent
from ursina.shaders import basic_lighting_shader as bls
from main_scene import Main_Scene
from tent_inside import Tent_Inside_Scene
from main_menu import Main_Menu

class MainApp(Ursina):
    def __init__(self):
        super().__init__()
        self.current_scene = None
        self.first = Main_Menu(self)
        self.main_scene = Main_Scene(self)
        self.tent_inside_scene = Tent_Inside_Scene(self)
        self.show_scene(self.first)

    def show_scene(self, scene):
        if self.current_scene:
            self.current_scene.disable()
        self.current_scene = scene
        self.current_scene.enable()


app = MainApp()
app.run()

