"""
Simple Perlin noise terrain generator.
"""
from perlin_noise import PerlinNoise
from ursina import Entity, Text, color

class Terrain():
    def __init__(self, generateOnStart=True,
                    amplitude=16,
                    frequency=24,
                    seed=2021):
        self.freq = amplitude
        self.amp = frequency
        self.seed = seed
        self.noise = PerlinNoise(seed=self.seed,octaves=1)
        self.bedrock = -9 # What is base height?

        self.blocks = {}

        # A basic 2D flat ground.
        self.basicFloor = Entity(model='quad',scale=2000,
                            y=self.bedrock,
                            rotation_x=90,
                            texture='grass.png',
                            texture_scale=(2000/12,2000/12),
                            collider='box')

        if generateOnStart:
            self.generateTerrain()
    
    def generateTerrain(self):
        self.displayStartMessage()

        

    def displayStartMessage(self):
        moo=Text(   text='<bold><black>Generating terrain...',
                    background=True)
        moo.x = -0.7
        moo.y = 0.4
        moo.scale=2
        moo.background.color=color.orange
        moo.appear(speed=0.15)