"""
Hello world! 2.0 - iteration
"""
from ursina import *
from randVec3 import randVec3

app = Ursina()
window.color=color.pink
tex='earth' # Load our texture.
mod='cube'  # Load the default cube model.

for i in range(280):
    p = Entity(model=mod, texture=tex,
                position=randVec3())

def update(): 
    eye.rotation_y+=2*time.dt

eye = EditorCamera()
app.run()
