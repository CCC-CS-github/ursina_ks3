"""
Hello world!
3D rotating planet
Ursina Lesson 1
"""

from ursina import *

app = Ursina()

planet = Entity(model='sphere', texture='earth')
planet.scale = 4

def update():
    planet.rotation_y += 0.4

app.run()
