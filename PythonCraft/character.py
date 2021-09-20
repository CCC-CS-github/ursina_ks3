"""
Set up first person character.
Add current gravity speed and gravity acceleration
to first person character object.
These are used by the lerping perlin gravity system,
which is currently in the perlin_terrain module.
"""

from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Text, color
from numpy import floor
import time

class Character():
    def __init__(self,speed=2):
        self.character = FirstPersonController()
        self.character.cursor.visible=False
        self.character.speed=speed
        self.character.gravity=0.0
        self.character.grav_acc=0.2
        self.character.grav_speed=0
        self.character.x = 6
        self.character.z = 53
        self.character.y = 32
        self.locationMessage = Text(text='xyz',
                                    origin=(0,0),
                                    background=False)
        # Hack
        self.prevTime = time.time()

    def input(self,key):
        if key == 'escape':
            if self.character.enabled: 
                self.character.disable()
            else: self.character.enable()

    def move(self,_terrain):
        from ursina import lerp, time as ursina_time

        self.displayLocation()

        # *** Hack
        if time.time()-self.prevTime >= 0.0:
            if _terrain.pos<_terrain.terrainSize*_terrain.terrainSize:
                _terrain.generateTerrain()
            self.prevTime=time.time()
            

        # How high or low can we step/drop?
        # Just using this next line as hack before
        # refactoring -- i.e. we have copied across
        # this code from perlin_terrain.
        # So, we want to reference character variables
        # directly instead of through _character!
        _character = self.character
        step_height=3
        character_height=2

        # Need to adjust to correct position...
        x = floor(_character.x + 0.5)
        z = floor(_character.z + 0.5)
        y = _character.y

        # What y is the terrain at this position?
        # NB their are two modes of perlin terrain -
        # ordinary (one octave) and advanced (three).
        target_y=_terrain.bedrock
        if _terrain.advancedTerrain==True:
            target_y += _terrain.advancedPerlin(x,z)
        else:
            target_y += _terrain.getPerlin(x,z)

        target_y += character_height  
        
        # How far are we from the target y?
        target_dist = target_y - y
        # Can we step up or down?
        if target_dist < step_height and target_dist > -step_height:
            y = lerp(y, target_y, 9.807*ursina_time.dt)
            _character.grav_speed = 0
        elif target_dist < -step_height:
            # This means we're falling!
            _character.grav_speed += (_character.grav_acc * ursina_time.dt)
            y -= _character.grav_speed
        
        _character.y = y
    
    def displayLocation(self):
        self.locationMessage.text=('<bold><white>'+
                    str(int(self.character.x)) + ' ' +
                    str(int(self.character.y)) + ' ' +
                    str(int(self.character.z)))
        
        self.locationMessage.scale=2
        self.locationMessage.create_background()
        self.locationMessage.background.color=color.gray
        self.locationMessage.x = 0.5
        self.locationMessage.y = 0.4