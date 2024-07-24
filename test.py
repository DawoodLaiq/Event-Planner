from ursina import *
import math
from guard import Guard
from worker import Worker
app= Ursina()

Worker(position=(0,0,0), cost=2000, power=0)
EditorCamera()
app.run()
