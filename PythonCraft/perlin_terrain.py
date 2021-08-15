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
        self.freq = frequency
        self.amp = amplitude
        self.seed = seed
        self.noise = PerlinNoise(seed=self.seed,octaves=1)
        self.bedrock = -9 # What is base height?

        # self.blocks = []
        self.blockMod = 'block.obj'
        self.blockTex = 'block_texture.png'
        self.size=6        # I.e. width.
        self.terrainSize=12 # Ditto.

        self.chunks = []


        # A basic 2D flat ground.
        self.basicFloor = Entity(model='quad',scale=2000,
                            y=self.bedrock+0.1-self.amp/2,
                            rotation_x=90,
                            texture='grass.png',
                            texture_scale=(20/12,20/12),
                            collider='box')

        # *** position hack
        self.pos=0

        if generateOnStart:
            self.generateTerrain()

    def generateTerrain(self):
        from numpy import floor
        from random import randint
        
        # self.displayStartMessage()

        self.chunks.append(Entity(model=self.blockMod,
                        texture=self.blockTex))

        # Catch division by zero.
        if self.freq <= 0: self.freq = 24
        
        for i in range(self.size*self.size):
            b=Entity(   model=self.blockMod,
                        texture=self.blockTex)
            b.y=self.bedrock
            # *** position hack!
            b.x=floor((self.pos/self.terrainSize))*self.size+floor(i/self.size)
            b.z=floor((self.pos%self.terrainSize))*self.size+floor(i%self.size)
            b.y = floor((self.noise([b.x/self.freq,
                            b.z/self.freq]))*self.amp)
            b.y += self.bedrock
            tint=randint(150,255)
            b.color=color.rgb(tint,tint,tint)
            b.rotation_y=randint(0,3)*90
            b.parent=self.chunks[-1]
            b.disable()
            # self.blocks.append(b)

        # ***
        self.chunks[-1].combine()

        # *** position hack
        self.pos+=1

    def displayStartMessage(self):
        moo=Text(   text='<bold><black>Generating terrain...',
                    background=True)
        moo.x = -0.7
        moo.y = 0.4
        moo.scale=2
        moo.background.color=color.orange
        moo.appear(speed=0.15)