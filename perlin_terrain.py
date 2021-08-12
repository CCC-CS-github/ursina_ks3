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

        self.blocks = []
        self.size=32

        # A basic 2D flat ground.
        self.basicFloor = Entity(model='quad',scale=2000,
                            y=self.bedrock-1-0.01,
                            rotation_x=90,
                            texture='grass.png',
                            texture_scale=(2000/12,2000/12),
                            collider='box')

        if generateOnStart:
            self.generateTerrain()
    
    def controlCharacter(self, _character):
        from ursina import lerp, time
        from numpy import floor
        # How high or low can we step/drop?
        step_height=3
        character_height=1.8

        # Need to adjust to correct position...
        x = _character.x - 0.5
        z = _character.z + 0.5
        y = _character.y

        # What y is the terrain at this position?
        target_y = floor((self.noise([x/self.freq,
                            z/self.freq]))*self.amp +
                            character_height)  
        
        # How far are we from the target y?
        target_dist = target_y - y
        # Can we step up or down?
        if target_dist < step_height and target_dist > -step_height:
            y = lerp(y, target_y, 9.807*time.dt)
            _character.grav_speed = 0
        elif target_dist < -step_height:
            # This means we're falling!
            _character.grav_speed += (_character.grav_acc * time.dt)
            y -= _character.grav_speed
        
        _character.y = y

    def generateTerrain(self):
        from numpy import floor
        from random import randint

        self.displayStartMessage()

        # Catch division by zero.
        if self.freq <= 0: self.freq = 24

        for i in range(1,self.size*self.size):
            b=Entity(   model='block.obj',
                        texture='block_texture.png')
            b.y=self.bedrock
            b.x=i/self.size-floor(self.size/2)
            b.z=i%self.size-floor(self.size/2)
            b.y = floor((self.noise([b.x/self.freq,
                            b.z/self.freq]))*self.amp)
            tint=randint(200,255)
            b.color=color.rgb(tint,tint,tint)
            b.rotation_y=randint(0,3)*90
            self.blocks.append(b)            

    def displayStartMessage(self):
        moo=Text(   text='<bold><black>Generating terrain...',
                    background=True)
        moo.x = -0.7
        moo.y = 0.4
        moo.scale=2
        moo.background.color=color.orange
        moo.appear(speed=0.15)