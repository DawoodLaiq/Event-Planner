from ursina import *
from main_scene import Main_Scene
from tent_inside import Tent_Inside_Scene
from main_menu import Main_Menu
from sidebar import Sidebar

app = Ursina()

class MainApp():
    def __init__(self):
        super().__init__()
        self.current_scene = None
        self.first = Main_Menu(self)
        self.main_scene = Main_Scene(self)
        
        self.show_scene(self.first)

    

    def show_scene(self, scene):
        if self.current_scene:
            self.current_scene.disable()
        self.current_scene = scene
        self.current_scene.enable()


if __name__ == '__main__':
    game = MainApp()
    app.run()

