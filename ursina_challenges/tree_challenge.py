"""Simple Tree""" 
from ursina import *

app = Ursina()

canopy=Entity(model='cube',color=color.green,scale=4)
trunk=Entity(model='cube',color=color.brown,scale_y=8)
trunk.y=-6

EditorCamera()

app.run()
