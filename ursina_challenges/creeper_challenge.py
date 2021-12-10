"""Creeper - aka Notch's Mistake"""
from ursina import *

app = Ursina()

body=Entity(model='cube',scale_y=2,scale_z=0.5,color=color.green)
frontfeet=Entity(model='cube',scale=0.5,y=-1.5,scale_x=1)
frontfeet.color=color.rgb(0,100,0)
frontfeet.z=-0.5
backfeet = duplicate(frontfeet)
backfeet.z=0.5

EditorCamera()
app.run()
