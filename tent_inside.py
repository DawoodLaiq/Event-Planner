from ursina import *
from tent import Tent
from air_conditioner import Air_Conditioner
from fans import Fan
from lights import Light
from dustbins import Dustbin
from speakers import Speaker
from ursina.shaders import basic_lighting_shader as bls
from ursina.shaders import matcap_shader as lws

from tv import TV
from sidebar import Sidebar

class Tent_Inside_Scene(Entity):
    def __init__(self, app, name, tent_data):
        super().__init__()
        self.app = app
        self.tent_data = tent_data
        self.tent_name=name
        self.entities=[]
        
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
        
        self.sidebar = Sidebar()
        self.toggle_button = Button(
            text='Toggle Sidebar',
            color=color.azure,
            scale=(0.2, 0.1),
            position=(0.5, 0.4),
            on_click=self.toggle_sidebar
        )
        
        for e in range(self.tent_data['AC']['quantity']):
            Air_Conditioner(position=(-30,0,int(e)*5),cost=self.tent_data['AC']['cost'], power=self.tent_data['AC']['power'])

        for e in range(self.tent_data['Fans']['quantity']):
            Fan(position=(10,0,int(e)*5),cost=self.tent_data['Fans']['cost'], power=self.tent_data['Fans']['power'])

        for e in range(self.tent_data['Dustbins']['quantity']):
            Dustbin(position=(15,0,int(e)*5),cost=self.tent_data['Dustbins']['cost'], power=self.tent_data['Dustbins']['power'])

        for e in range(self.tent_data['Speakers']['quantity']):
            Speaker(position=(20,0,int(e)*5),cost=self.tent_data['Speakers']['cost'], power=self.tent_data['Speakers']['power'])
        
        for e in range(self.tent_data['Lights']['quantity']):
            Light(position=(0,10,int(e)*15),cost=self.tent_data['Lights']['cost'], power=self.tent_data['Lights']['power'])

        #self.tent_data['Total_Estimation']['quantity']
        #self.tent_data['Total_Estimation']['cost']
        #self.tent_data['Total_Estimation']['power']
        
        for e in range(self.tent_data['TV']['quantity']):
            TV(position=(0,0,int(e)*20),cost=self.tent_data['TV']['cost'], power=self.tent_data['TV']['power'])
        
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

    def enable(self):
        for entity in self.entities:
            entity.enabled = True
            entity.shader = lws

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
        
    