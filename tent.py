from ursina import *
from ursina.shaders import basic_lighting_shader as bls

class Tent(Entity):
    currently_dragged_entity = None
    def __init__(self, position=(0,0,0),cost=int,tent_data=dict(), name=str):
        super().__init__(
            parent=scene,
            model='Assets/Marque.obj',
            color=color.gray,
            scale=1,
            origin=(0,-1,0),
            position=position,
            collider='box',
            plane_direction=(0, 1, 0),
            shader=bls
        )
        self.cost = cost
        self.name = name
        self.dragging = False
        self.tips = Tooltip(f"Tent Name: {self.name}\nAC: {tent_data.get('AC', {}).get('quantity', 0)}\nFans: {tent_data.get('Fans', {}).get('quantity', 0)}\nSpeakers: {tent_data.get('Speakers', {}).get('quantity', 0)}\nLights: {tent_data.get('Lights', {}).get('quantity', 0)}\nDustbins: {tent_data.get('Dustbins', {}).get('quantity', 0)}\nTotal Cost: {tent_data.get('Total_Estimation', {}).get('quantity', 0)}")
        self.tips.background.color = color.hsv(0,0,0,.8)

    def input(self, key):
        
        
        if key == 'r' and self.hovered:
            self.rotation_y += 90
        elif key == 't' and self.hovered:
            self.rotation_y -= 90
        elif key == 'up arrow' and self.hovered:
            self.scale *= 1.1  # Increase scale by 10%
        elif key == 'down arrow' and self.hovered:
            self.scale *= 0.9  # Decrease scale by 10%
        elif held_keys['shift'] and self.hovered and Tent.currently_dragged_entity is None:
            if mouse.left:
                Tent.currently_dragged_entity = self
                self.dragging = True
        elif key == 'left mouse up':
            if self.dragging:
                self.dragging = False
                Tent.currently_dragged_entity = None
        elif key == 'backspace' and self.hovered:
            destroy(self)
            self.tips.enabled = False

    def update(self):
        if self.dragging and mouse.left:
            try:
                self.position = Vec3(mouse.world_point.x, self.position.y, mouse.world_point.z)
            except:
                print("Not selected")
        
        else:
            self.dragging = False
        if self.hovered:
            self.tips.enabled = True
        else:
            self.tips.enabled = False


        