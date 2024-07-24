from ursina import *

class Light(Entity):
    currently_dragged_entity = None
    def __init__(self, position=(0,0,0), cost=int, power=int):
        super().__init__(
            parent=scene,
            model="Assets/light.gltf",
            #texture="Assets/light_text.jpg",
            color="#1A2421",
            scale=0.02,
            origin=(0,0,0),
            position=position,
            collider='box',
            plane_direction=(0, 1, 0)
        )
        self.cost = cost
        self.power = power
        self.dragging = False
        self.tips = Tooltip(f"Cost: {self.cost}\nPower: {self.power}")
        self.tips.background.color = color.hsv(0,0,0,.8)

        self.light = PointLight(parent=self, position=(0, 2, 0), color=color.white)
        self.light.intensity = self.power / 5
    
    def input(self, key):
        if held_keys['shift'] and self.hovered and Light.currently_dragged_entity is None:
            if mouse.left:
                Light.currently_dragged_entity = self
                self.dragging = True
        elif key == 'left mouse up':
            if self.dragging:
                self.dragging = False
                Light.currently_dragged_entity = None
        elif key == 'r' and self.hovered:
            self.rotation_y += 90
        elif key == 't' and self.hovered:
            self.rotation_y -= 90
        
        elif key == 'backspace' and self.hovered:
            destroy(self)
            self.tips.enabled = False
    
    def update(self):
        if self.dragging:
            try:
                self.position = (mouse.world_point.x, self.position.y, mouse.world_point.z)
            except:
                print("Not selected")
        else:
            self.dragging = False
        if self.hovered:
            self.tips.enabled = True
        else:
            self.tips.enabled = False