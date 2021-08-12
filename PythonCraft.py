"""
Simple Minecraft in Python - 'PythonCraft' - Lesson 2
NB. press shift+q to quit
"""
# Import the ursina module, and its First Person character.
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# Import the Perlin Noise module for creating terrain.
from perlin_terrain import Terrain

# Create Window. Set background colour to sky blue.
app = Ursina()
window.color=color.rgb(0,200,255)

# Initialise our terrain.
cambridge = Terrain()

# Setup our first-person character.
steve = FirstPersonController()
steve.cursor.visible=False
steve.gravity=0
steve.grav_acc = 0.2
steve.grav_speed = 0
# steve.gravity=0.6 # Maybe we leave this out (concision).
# steve.speed = 0.01

def update():
    cambridge.controlCharacter(steve)

def input(key):
    if key == 'escape':
        if steve.enabled: steve.disable()
        else: steve.enable()

# Start the program :)
app.run()