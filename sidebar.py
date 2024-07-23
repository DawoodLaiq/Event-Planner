from ursina import *

class Sidebar(WindowPanel):
    def __init__(self, **kwargs):
        super().__init__(
            title='Tent Data Estimations',
            content=(),
            popup=False,
            position=(0.5,0.5,0),
            **kwargs
        )
        
        self.visible=False
        self.panel.enabled = self.visible
        
        
        


    def toggle(self):
        self.visible = not self.visible
        self.panel.enabled = self.visible

    def update_info(self, tent_data):
        content_data=[]
        for k,v in tent_data.items():
            content_data.append(Text(f'-----{k}-----'))
            for k2,v2 in v.items():
                content_data.append(Text(f'{k2}: {v2}'))
        
        self.content = (content_data)
                
        self.layout()
        self.add_script(Scrollable())
