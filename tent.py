from ursina import *

class Tent(Entity):
    def __init__(self, position=(0,0,0), cost=1000, tent_data=dict(), name=str):
        super().__init__(
            parent=scene,
            model='Assets/Marque.obj',
            color=color.azure,
            scale=1,
            origin=(0,-1,0),
            position=position,
            collider='box',
            plane_direction=(0, 1, 0)
        )
        self.cost = cost
        self.name = name
        self.dragging = False
        self.tips = Tooltip(f"Marquee {self.name}\nAC: {tent_data.get('AC', 0)}\nFans: {tent_data.get('Fans', 0)}\nSpeakers: {tent_data.get('Speakers', 0)}\nLights: {tent_data.get('Lights', 0)}\nDustbins: {tent_data.get('Dustbins', 0)}\nTotal Cost: {tent_data.get('Total_Cost', 0)}")
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
        elif held_keys['shift'] and self.hovered:
            self.dragging = True if mouse.left else False
        elif key == 'backspace' and self.hovered:
            destroy(self)
            self.tips.enabled = False

    def update(self):
        if self.dragging and mouse.left:
            self.position = Vec3(mouse.world_point.x, self.position.y, mouse.world_point.z)
        
        else:
            self.dragging = False
        if self.hovered:
            self.tips.enabled = True
        else:
            self.tips.enabled = False


        