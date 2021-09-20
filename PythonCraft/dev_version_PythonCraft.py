"""
private dev for the PythonCraft code -- i.e. in case
I break the original, PythonCraft.py.
Also -- I want the original kept to approx. 30 lines.
"""
# Import the ursina module, and its First Person character.
from ursina import *
# Import the Perlin Noise module for creating terrain.
from perlin_terrain import Terrain
from character import Character

# Create Window. Set background colour to sky blue.
app = Ursina()
window.color=color.rgb(0,200,255)
# ***
# scene.fog_density = 0.02
# scene.fog.color = rgb(0,200,255)

# Initialise our terrain.
# cambridge = Terrain(frequency=48,amplitude=32)
# ***
cambridge = Terrain(advanced=True,
                    a1=100,f1=212,
                    a2=50,f2=180,
                    a3=1,f3=1,
                    seed=1984)

# Initialise and set up our first-person character.
steve = Character(speed=6)

# Our main program update loop.
def update():
    # Allow character to move over terrain.
    steve.move(cambridge)

# Function that responds to key and mouse presses.
def input(key):
    steve.input(key) # Character responds to 'escape' key.

# Start the program :)
app.run()