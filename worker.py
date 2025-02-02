from ursina import *

class Worker(Entity):
    currently_dragged_entity = None
    def __init__(self, position=(0,0,0), cost=int, power=int):
        super().__init__(
            parent=scene,
            model="Assets/worker.gltf",
            scale=3,
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
        if held_keys['shift'] and self.hovered and Worker.currently_dragged_entity is None:
            if mouse.left:
                Worker.currently_dragged_entity = self
                self.dragging = True
        elif key == 'left mouse up':
            if self.dragging:
                self.dragging = False
                Worker.currently_dragged_entity = None
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
                self.position = Vec3(mouse.world_point.x, self.position.y, mouse.world_point.z)
            except:
                print("Not selected")
        else:
            self.dragging = False
        if self.hovered:
            self.tips.enabled = True
        else:
            self.tips.enabled = False