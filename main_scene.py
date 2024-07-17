from ursina import *
from tent import Tent
from ursina.shaders import basic_lighting_shader as bls
from tkinter import filedialog, Tk
import os
from tent_inside import Tent_Inside_Scene

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
        self.ground = Entity(model="plane",scale=(200,1,200),collision="box",position=(0,0,0), texture_scale = (100,100),texture="white_cube",shader=None,enabled=False)
        self.entities.append(self.ground)
        Entity.default_shader = bls
        Draggable.default_shader = bls
        
        for k,v in self.data.items():
             if k == 'Tent':
                e = Tent(name=v['name'],position=(0, 0, 15), tent_data=v['data'])

        self.create_tent_button = Button(
            text='Create Tent',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(-0.5, 0.4),
            on_click=self.create_tent,
            enabled=False
        )
        self.entities.append(self.create_tent_button)
        self.button_to_scene2 = Button(
            text='Go to Scene 2',
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
            position=(-0.5, -0.2),
            on_click=self.upload_image,
            enabled=False
        )
        self.entities.append(self.upload_image_button)
        self.cam = EditorCamera()
        self.cam.position = (50, 50, -100)
        self.cam.enabled=False
        self.entities.append(self.cam)
        

    def create_tent(self):
            self.count += 1
            tent_data = {
                "AC": 30,
                "Fans": 15,
                "Speakers": 10,
                "TV": 2,
                "Lights": 30,
                "Dustbins": 20,
                "Total_Cost": 1500000
            }
            e = Tent(position=(0, 0, self.count*15), cost=1000, tent_data=tent_data,name=str(self.count))
            self.entities.append(e)
    
    def create_tent_from_saved(self,data):
            self.count += 1
            tent_data = {
                "AC": 30,
                "Fans": 15,
                "Speakers": 10,
                "TV": 2,
                "Lights": 30,
                "Dustbins": 20,
                "Total_Cost": 1500000
            }
            e = Tent(position=(0, 0, self.count*15), cost=1000, tent_data=tent_data,name=str(self.count))
            self.entities.append(e)

    def enable(self):
        for entity in self.entities:
            entity.enabled = True

    def disable(self):
        for entity in self.entities:
            entity.enabled = False

    def go_to_scene2(self):
        self.app.show_scene(Tent_Inside_Scene(self.app,name="test",tent_data=self.data['Tent']['data']))

    def upload_image(self):
        # Hide the root window of Tkinter
        root = Tk()
        root.withdraw()
        # Open file dialog
        initial_dir = os.getcwd()
        file_path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            
            # Load the selected image as a texture
            
            self.img_name=file_path
            if self.ground.enabled:
                path = os.path.relpath(file_path, initial_dir)
                texture = load_texture(path)
                self.ground.texture = texture
                self.ground.texture_scale = (1,1)
        root.destroy()

