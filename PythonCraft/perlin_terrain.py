"""
Simple Perlin noise terrain generator.
"""
from perlin_noise import PerlinNoise
from ursina import Entity, Text, color
from numpy import floor

class Terrain():
    def __init__(self, generateOnStart=True,
                    amplitude=16,
                    frequency=24,
                    seed=2021,
                    advanced=False,
                    a1=64,a2=32,a3=4,
                    f1=512,f2=128,f3=24):
        self.freq = frequency
        self.amp = amplitude
        self.seed = seed
        self.noise = PerlinNoise(seed=self.seed,octaves=1)
        self.bedrock = -9 # What is base height?

        # Advanced-mode overloading.
        self.advancedTerrain = advanced
        if advanced==True:
            self.amp1 = a1
            self.amp2 = a2
            self.amp3 = a3
            self.freq1 = f1
            self.freq2 = f2
            self.freq3 = f3

        self.blocks = []
        self.blockMod = 'block.obj'
        self.blockTex = 'block_texture.png'
        self.size=4        # I.e. width. Default 6.
        self.terrainSize=16 # Ditto. Default 12.

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
        """
        NB. terrain generation is called from the
        character module's update function.
        Would be better, perhaps, to call the
        character's movement from the terrain module.
        We do not call the terrain generation from 
        the main module in order to keep that concise.
        """
        from random import randint
        
        # self.displayStartMessage()

        self.chunks.append(Entity(model=self.blockMod,
                        texture=self.blockTex))

        # Catch division by zero.
        if self.freq <= 0: 
            self.freq = 24
            print('frequency must be greater than zero. Thank you.')
        
        for i in range(self.size*self.size):
            b=Entity(   model=self.blockMod,
                        texture=self.blockTex)
            b.y=self.bedrock
            # *** position hack!
            b.x=floor((self.pos/self.terrainSize))*self.size+floor(i/self.size)
            b.z=floor((self.pos%self.terrainSize))*self.size+floor(i%self.size)
            
            # If using basic terrain, just use one
            # octave of perlin noise.
            # If using advanced, pass over three octaves.
            if self.advancedTerrain == False:
                b.y += self.getPerlin(b.x,b.z)
            else:
                b.y += self.advancedPerlin(b.x,b.z)
            
            # b.y += self.bedrock
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

    def advancedPerlin(self,_x,_z):
        y = 0
        y += ((self.noise([_x/self.freq1,
                    _z/self.freq1]))*self.amp1)
        y += ((self.noise([_x/self.freq2,
                    _z/self.freq2]))*self.amp2)
        y += ((self.noise([_x/self.freq3,
                    _z/self.freq3]))*self.amp3)
        return floor(y)

    def getPerlin(self,_x,_z):
        return floor((  self.noise([_x/self.freq,
                        _z/self.freq]))*self.amp)

    def displayStartMessage(self):
        moo=Text(   text='<bold><black>Generating terrain...',
                    background=True)
        moo.x = -0.7
        moo.y = 0.4
        moo.scale=2
        moo.background.color=color.orange
        moo.appear(speed=0.15)