from ursina import *
from tent import Tent
#from tkinter import filedialog, Tk
import os
from tent_inside import Tent_Inside_Scene
from guard import Guard
from ursina.prefabs.file_browser import FileBrowser
from ursina.prefabs.grid_editor import PixelEditor

class Main_Scene(Entity):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.count=0
        self.entities=[]
        #if not data:
        self.data= {
                "Tent": { "name": "Marquee 1", "size_x" : 500, "size_y": 500, "cost" : 50000, "power" : 20000, "data": {
                "AC": { "quantity" : 30, "cost" : 1500, "power" : 2000},
                "Fans": { "quantity" : 10, "cost" : 150, "power" : 200},
                "Speakers": { "quantity" : 7, "cost" : 100, "power" : 100},
                "TV": { "quantity" : 2, "cost" : 250, "power" : 150},
                "Lights": { "quantity" : 35, "cost" : 15, "power" : 20},
                "Dustbins": { "quantity" : 5, "cost" : 5, "power" : 0},
                "Total_Estimation": { "quantity" : 0, "cost" : 0, "power" : 0}
            } } 
            }
        
        self.img_name=''
        self.ground = Entity(model="plane",scale=(200,1,200),collider="box",position=(0,0,0), texture_scale = (100,100),texture="white_cube",shader=None,enabled=False)
        self.entities.append(self.ground)
        
        for k,v in self.data.items():
             if k == 'Tent':
                e = Tent(name=v['name'],position=(0, 0, 15), tent_data=v['data'])
                self.entities.append(e)

        self.create_tent_button = Button(
            text='Create Tent',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(-0.8, 0.45),
            on_click=self.create_tent,
            enabled=False
        )
        self.entities.append(self.create_tent_button)
        self.button_to_scene2 = Button(
            text='Go inside the tent',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(0.7, 0.4),
            on_click=self.go_to_scene2,
            enabled=False
        )
        self.entities.append(self.button_to_scene2)
        self.upload_image_button = Button(
            text='Upload Image',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(-0.8, 0.2),
            on_click=self.upload_image,
            enabled=False
        )
        self.entities.append(self.upload_image_button)
        self.cam = EditorCamera()
        self.cam.position = (50, 50, -100)
        self.cam.enabled=False
        self.entities.append(self.cam)

        self.roads = []
        self.drawing_road = False
        self.erasing_road = False
        
        self.add_guard_button = Button(
            text='Add guard',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(-0.8, 0),
            on_click=self.add_guard,
            enabled=False
        )
        self.entities.append(self.add_guard_button)
        
        
        self.toggle_road_button = Button(
            text='Draw Road',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(-0.8, -0.2),
            on_click=self.toggle_road,
            enabled=False
        )
        self.entities.append(self.toggle_road_button)

        self.toggle_road_erase_button = Button(
            text='Erase Road',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(-0.8, -0.4),
            on_click=self.toggle_erase_road,
            enabled=False
        )
        self.entities.append(self.toggle_road_erase_button)



    def add_guard(self):
        e = Guard(position=(5,0,0), cost=2000, power=0)
        self.entities.append(e)


    def toggle_road(self):
        self.drawing_road = not self.drawing_road

    def toggle_erase_road(self):
        self.erasing_road = not self.erasing_road

    def create_tent(self):
            self.count += 1
            
            e = Tent(position=(0, 0, self.count*15), cost=1000, tent_data=self.data['Tent']['data'],name=str(self.data['Tent']['name']))
            self.entities.append(e)
    
    def create_tent_from_saved(self,data):
            self.count += 1
            e = Tent(position=(0, 0, self.count*15), cost=1000, tent_data=tent_data,name=str(self.count))
            self.entities.append(e)

    def enable(self):
        for entity in self.entities:
            entity.enabled = True

        for road in self.roads:
            road.enabled = True

    def disable(self):
        for entity in self.entities:
            entity.enabled = False
        
        for road in self.roads:
            road.enabled = False
        
        self.drawing_road = False
        self.erasing_road = False

    def go_to_scene2(self):
        self.app.show_scene(Tent_Inside_Scene(self.app,name=self.data['Tent']['name'],tent_data=self.data['Tent']['data']))

    def upload_image(self):
        self.file_browser = FileBrowser(file_types=('.png', '.jpg', '.jpeg','.PNG'), position=(0,0), on_submit=self.on_file_selected)
        self.file_browser.open()

    def on_file_selected(self, paths):
        if paths:
            initial_dir = os.getcwd()
            file_path = paths[0]
            if self.ground.enabled:
                path = os.path.relpath(file_path, initial_dir)
                print(path)
                texture = load_texture(path)
                self.ground.texture = texture
                self.ground.texture_scale = (1, 1)
                self.file_browser.close()


    def update(self):
        if self.drawing_road and mouse.left:
            self.draw_road_segment()
        elif self.erasing_road and mouse.left:
            self.erase_road_segment()

    def draw_road_segment(self):
        # Get the current position of the mouse on the plane
        
        if mouse.world_point:
            position = Vec3(mouse.world_point.x, 0.1, mouse.world_point.z)
            road_segment = Entity(
                model='quad',
                color=color.black,
                rotation=(90,0,0),
                scale=(2, 2, 0.1),  # Adjust the width and height as needed
                position=position,
                collider="box"
            )
            self.roads.append(road_segment)

    def erase_road_segment(self):
        for road in self.roads:
            if road.hovered:
                destroy(road)
                self.roads.remove(road)
                break