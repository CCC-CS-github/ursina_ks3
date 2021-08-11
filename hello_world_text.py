"""
Hello world!
3D rotating planet
Ursina Lesson 1
"""

from ursina import *

app = Ursina()

planet = Entity(model='sphere', texture='earth')
planet.scale = 4

message = Text('<bold>hello world!',background=True)
message.scale=2
message.background.color=color.lime
message.appear(speed=0.1)

def update():
    planet.rotation_y += 0.4

app.run()
