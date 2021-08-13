"""
Simple Minecraft in Python - 'PythonCraft' - Lesson 2
NB. press esc to access mouse, or shift+q to quit
"""
# Import the ursina module, and its First Person character.
from ursina import *
# Import the Perlin Noise module for creating terrain.
from perlin_terrain import Terrain
from character import Character

# Create Window. Set background colour to sky blue.
app = Ursina()
window.color=color.rgb(0,200,255)

# Initialise our terrain.
cambridge = Terrain()

# Initialise our first-person character.
steve = Character()
# Our main program update loop.
def update():
    # Allow character to move over terrain...
    steve.move(cambridge)

def input(key):
    steve.input(key) # Additional key input, like escape.

# Start the program :)
app.run()