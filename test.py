from ursina import *
import math


app= Ursina()

class MainApp(Entity):
    def __init__(self):
        super().__init__()
        
        self.ground = Entity(
            model="plane", 
            scale=(20, 1, 20), 
            collision="box", 
            position=(0, 0, 0), 
            texture_scale=(20, 20), 
            texture="white_cube", 
            shader=None
        )
        
        self.roads = []
        self.drawing_road = False
        #camera.position = (0,0,-40)
        self.cam = EditorCamera()

    def input(self,key):
        if key == 'left mouse down':
            self.drawing_road = True
            #print("Started drawing road")
        elif key == 'left mouse up':
            self.drawing_road = False
            #print("Stopped drawing road")

    def update(self):
        #print(camera.rotation)
        print(mouse.point)
        if self.drawing_road:
            self.draw_road_segment()

    def draw_road_segment(self):
        # Get the current position of the mouse on the plane
        if mouse.point:
            print("drawing")
            position = Vec3(mouse.position.x, 0.1, mouse.position.z)
            road_segment = Entity(
                model='cube',
                color=color.gray,
                scale=(1, 0.1, 3),  # Adjust the width and height as needed
                position=position
            )
            self.roads.append(road_segment)

if __name__ == '__main__':
    game = MainApp()
    app.run()
