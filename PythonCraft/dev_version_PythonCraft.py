"""
private dev for the PythonCraft code -- i.e. in case
I break the original, PythonCraft.py.
Also -- I want that original kept to its 30 lines,
esp. since I've taken screenshot and used on presentation.
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

# Initialise and set up our first-person character.
steve = Character()

# Our main program update loop.
def update():
    # Allow character to move over terrain.
    steve.move(cambridge)

# Function that responds to key and mouse presses.
def input(key):
    steve.input(key) # Character responds to 'escape' key.

# Start the program :)
app.run()