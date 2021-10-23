"""
Let's try to make a mushroom! :)
"""
from ursina import *

app = Ursina()

# First, we need the 'base' of the mushroom
base = Entity(model='cube')
base.color = color.rgb(244,244,244) # Nearly full white.
base.scale_x = 0.8
base.scale_z = 0.8
base.scale_y = 1.2

# Next we need the 'cap' of the mushroom.
cap = Entity(model='sphere')
cap.color = color.red
cap.y = 0.8
cap.scale_x = 3
cap.scale_z = 3

# Now we just need the white dots on the cap.
dot = Entity(model='sphere')
dot.color=color.white
dot.y = 1.2
dot.scale = 0.5

d2 = duplicate(dot)
d2.x = -0.5

d3 = duplicate(dot)
d3.x = 0.8
d3.z = -0.8
d3.y = 1

d4 = duplicate(dot)
d4.x = 0.4
d4.z = 0.9
d4.y = 1

d5 = duplicate(dot)
d5.x = -0.8
d5.z = -0.8
d5.y = 1

EditorCamera()
app.run()