from ursina import *
from tent import Tent
from air_conditioner import Air_Conditioner
from fans import Fan
from dustbins import Dustbin
from speakers import Speaker
from ursina.shaders import basic_lighting_shader as bls
from tv import TV

class Tent_Inside_Scene(Entity):
    def __init__(self, app, name, tent_data):
        super().__init__()
        self.app = app
        self.tent_name=name
        self.entities=[]
        self.AC=tent_data['AC']
        self.Speakers=tent_data['Speakers']
        self.Dustbins=tent_data['Dustbins']
        self.Fans=tent_data['Fans']
        self.TV=tent_data['TV']
        self.Lights=tent_data['Lights']
        self.Total_Cost=tent_data['Total_Cost']
        self.ground = Entity(model='plane',position=(0,0,0), scale=(100, 1, 100),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.ground)
        self.left_wall = Entity(parent=self.ground,model='cube',position=(20,0,0), scale=(1, 100, 100),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.left_wall)
        self.right_wall = Entity(parent=self.ground,model='cube',position=(-20,0,0), scale=(1, 100, 100),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.right_wall)
        self.front_wall = Entity(parent=self.ground,model='cube',position=(0,0,20), scale=(100, 100, 1),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.front_wall)
        self.back_wall = Entity(parent=self.ground,model='cube',position=(0,0,20), scale=(100, 100, 1),texture="white_cube",texture_scale=(20,20), color=color.light_gray,enabled=False)
        self.entities.append(self.back_wall)

        self.house = Entity(model='cube', scale=(2, 2, 2), color=color.red, position=(0, 1, 0),enabled=False)
        self.entities.append(self.house)

        for e in self.AC:
            Air_Conditioner(position=(0,0,int(e)*10),cost=1000, power=2000)

        for e in self.Fans:
            Fan(position=(10,0,int(e)*10),cost=100, power=200)

        for e in self.Dustbins:
            Dustbin(position=(10,0,int(e)*10),cost=100, power=200)

        for e in self.Speakers:
            Speaker(position=(10,0,int(e)*10),cost=100, power=200)

        for e in self.Lights:
            Light(position=(10,0,int(e)*10),cost=100, power=200)

        for e in self.TV:
            TV(position=(10,0,int(e)*10),cost=100, power=200)

        self.button_to_scene1 = Button(
            text='Go Back',
            color=color.orange,
            scale=(0.2, 0.1),
            position=(0.7, 0.4),
            on_click=self.go_to_scene1,
            enabled=False
        )
        self.entities.append(self.button_to_scene1)
        self.cam = EditorCamera()
        self.cam.position = (50, 50, -100)
        self.cam.enabled = False
        self.entities.append(self.cam)

    def enable(self):
        for entity in self.entities:
            entity.enabled = True

    def disable(self):
        for entity in self.entities:
            entity.enabled = False
        
    def go_to_scene1(self):
        self.app.show_scene(self.app.main_scene)
    
    def create_AC(self):
        e = Air_Conditioner()
        