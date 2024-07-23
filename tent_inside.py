from ursina import *
from tent import Tent
from air_conditioner import Air_Conditioner
from fans import Fan
from lights import Light
from dustbins import Dustbin
from speakers import Speaker
from ursina.shaders import basic_lighting_shader as bls

from tv import TV
from sidebar import Sidebar

class Tent_Inside_Scene(Entity):
    def __init__(self, app, name, tent_data):
        super().__init__()
        self.app = app
        Entity.default_shader = bls
        self.tent_data = tent_data
        self.tent_name=name
        self.entities=[]
        self.room_width=80
        self.room_depth=160
        self.ground_width=80
        self.ground_height=160
    
        
        
        self.sidebar = Sidebar()
        self.toggle_button = Button(
            text='Toggle Sidebar',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(0.5, 0.4),
            on_click=self.toggle_sidebar
        )
        self.entities.append(self.toggle_button)
        
        self.tent_data['Total_Estimation']['quantity'] = self.tent_data['AC']['quantity'] + self.tent_data['Fans']['quantity'] + self.tent_data['Speakers']['quantity'] + self.tent_data['TV']['quantity'] + self.tent_data['Lights']['quantity'] + self.tent_data['Dustbins']['quantity']
        self.tent_data['Total_Estimation']['cost'] = self.tent_data['AC']['cost'] + self.tent_data['Fans']['cost'] + self.tent_data['Speakers']['cost'] + self.tent_data['TV']['cost'] + self.tent_data['Lights']['cost'] + self.tent_data['Dustbins']['cost']
        self.tent_data['Total_Estimation']['power'] = self.tent_data['AC']['power'] + self.tent_data['Fans']['power'] + self.tent_data['Speakers']['power'] + self.tent_data['TV']['power'] + self.tent_data['Lights']['power'] + self.tent_data['Dustbins']['power']
        
        self.spawn_grid_of_lights()
        self.spawn_base_inside()
        self.spawn_AC()
        self.spawn_fans()
        

        for e in range(self.tent_data['TV']['quantity']):
            en = TV(position=(0,0,(e*40)-50),cost=self.tent_data['TV']['cost'], power=self.tent_data['TV']['power'])
            self.entities.append(en)
        
        
        for e in range(self.tent_data['Dustbins']['quantity']):
            en = Dustbin(position=(-25,0,(e*8)-50), rotation=(0, -90, 0),cost=self.tent_data['Dustbins']['cost'], power=self.tent_data['Dustbins']['power'])
            self.entities.append(en)
        
        for e in range(self.tent_data['Speakers']['quantity']):
            en = Speaker(position=(15,0,(e*5)-50),cost=self.tent_data['Speakers']['cost'], power=self.tent_data['Speakers']['power'])
            self.entities.append(en)
        
        self.button_to_scene1 = Button(
            text='Go Back',
            color=color.orange,
            scale=(0.2, 0.1),
            position=(0.7, 0.4),
            on_click=self.go_to_scene1,
            enabled=False
        )
        self.entities.append(self.button_to_scene1)
        self.create_AC_button = Button(
            text='Add AC',
            icon='Assets/img_ac.png',
            color=color.azure,
            scale=(0.2, 0.3),
            position=(-0.5, 0.4),
            on_click=self.create_AC,
            enabled=False
        )
        self.entities.append(self.create_AC_button)
        
        self.cam = EditorCamera()
        self.cam.position = (50, 50, -100)
        self.cam.enabled = False
        self.entities.append(self.cam)


    def spawn_base_inside(self):
        self.ground = Entity(model='plane',position=(0,0,0), scale=(80, 1, 160),texture="white_cube",texture_scale=(20,20), color=color.light_gray,shader=bls,enabled=False)
        self.entities.append(self.ground)
        self.left_wall = Entity(model='cube',position=(40,7,0), scale=(1, 20, 160),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.left_wall)
        self.right_wall = Entity(model='cube',position=(-40,7,0), scale=(1, 20, 160),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.right_wall)
        self.front_wall = Entity(model='cube',position=(0,7,80), scale=(80, 20, 1),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.front_wall)
        self.back_wall = Entity(model='cube',position=(0,7,-80), scale=(80, 20, 1),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.back_wall)

    def spawn_AC(self):
        total_length = 2 * self.room_width + self.room_depth
        gap = total_length / self.tent_data['AC']['quantity']

        for i in range(self.tent_data['AC']['quantity']):
            if i * gap < self.room_width:
                x = i * gap - self.room_width / 2
                z = -self.room_depth / 2
                rotation = (0, 0, 0)
            elif i * gap < self.room_width + self.room_depth:
                x = -self.room_width / 2
                z = (i * gap - self.room_width) - self.room_depth / 2
                rotation = (0, 90, 0)
            else:
                x = (i * gap - (self.room_width + self.room_depth)) - self.room_width / 2
                z = self.room_depth / 2
                rotation = (0, 180, 0)
            
            en = Air_Conditioner(position=(x, -4, z), rotation=rotation, cost=self.tent_data['AC']['cost'], power=self.tent_data['AC']['power'])
            self.entities.append(en)
        

    def spawn_fans(self):
        quantity = self.tent_data['Fans']['quantity']
        half_quantity = quantity // 2
        gap = 20  # Define the gap width between the left and right groups

        # Calculate spacing
        spacing_z = self.ground_height / (half_quantity + 1)

        # Left side
        for e in range(half_quantity):
            x = -self.ground_width / 4
            z = (e + 1) * spacing_z - self.ground_height / 2
            en = Fan(position=(x, 1, z), rotation=(0, 90, 0), cost=self.tent_data['Fans']['cost'], power=self.tent_data['Fans']['power'])
            self.entities.append(en)

        # Right side
        for e in range(half_quantity):
            x = self.ground_width / 4
            z = (e + 1) * spacing_z - self.ground_height / 2
            en = Fan(position=(x, 0, z), rotation=(0, -90, 0), cost=self.tent_data['Fans']['cost'], power=self.tent_data['Fans']['power'])
            self.entities.append(en)
        
        
    def spawn_grid_of_lights(self):
        quantity = self.tent_data['Lights']['quantity']
        aspect_ratio = self.ground_width / self.ground_height

        # Calculate the number of columns and rows based on the aspect ratio and quantity
        columns = int((quantity * aspect_ratio) ** 0.5)
        rows = (quantity + columns - 1) // columns

        # Calculate spacing based on ground dimensions and number of columns/rows
        spacing_x = self.ground_width / (columns + 1)
        spacing_z = self.ground_height / (rows + 1)

        for row in range(rows):
            for col in range(columns):
                if len(self.entities) >= quantity:
                    break
                x = (col + 1) * spacing_x - self.ground_width / 2
                z = (row + 1) * spacing_z - self.ground_height / 2
                en = Light(position=(x, 20, z), cost=self.tent_data['Lights']['cost'], power=self.tent_data['Lights']['power'])
                self.entities.append(en)
        

    def enable(self):
        for entity in self.entities:
            entity.enabled = True
            entity.shader = bls

    def disable(self):
        for entity in self.entities:
            entity.enabled = False
        
    def go_to_scene1(self):
        self.app.show_scene(self.app.main_scene)
    
    def create_AC(self):
        e = Air_Conditioner(position=(0,0,0),cost=self.tent_data['AC']['cost'], power=self.tent_data['AC']['power'])
        self.entities.append(e)
    
    def toggle_sidebar(self):
        self.sidebar.toggle()
        self.update_sidebar()

    def update_sidebar(self):
        
        self.sidebar.update_info(self.tent_data)
    
    def input(self, key):
        if key == 'p':
            self.wp.enabled = False
        elif key == 'u':
            self.wp.enabled = True
        
    