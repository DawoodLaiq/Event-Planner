from ursina import *

class Speaker(Entity):
    def __init__(self, position=(0,0,0), cost=int, power=int):
        super().__init__(
            parent=scene,
            model="Assets/speaker.obj",
            texture="Assets/speaker_text.png",
            #color="#1A2421",
            scale=10,
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
    
    def input(self, key):
        if held_keys['shift'] and self.hovered:
            self.dragging = True if mouse.left else False
        elif key == 'r' and self.hovered:
            self.rotation_y += 90
        elif key == 't' and self.hovered:
            self.rotation_y -= 90
        
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