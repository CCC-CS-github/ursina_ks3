"""
Simple Minecraft in Python - 'PythonCraft' - Lesson 2
NB. press shift+q to quit
"""
# Import the ursina module, and its First Person character.
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# Import the Perlin Noise module for creating terrain.
from perlin_noise import PerlinNoise

# Create Window. Set background colour to sky blue.
app = Ursina()
window.color=color.rgb(0,200,255)

# A basic 2D flat ground.
basicFloor = Entity(model='quad',scale=2000,rotation_x=90,
    texture='grass.png',texture_scale=(2000/12,2000/12))

# Setup our first-person character.
steve = FirstPersonController()
steve.cursor.visible=False
steve.gravity=0
steve.speed = 0.01

# Start the program :)
app.run()