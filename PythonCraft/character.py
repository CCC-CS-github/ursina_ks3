"""
Set up first person character.
Add current gravity speed and gravity acceleration
to first person character object.
These are used by the lerping perlin gravity system,
which is currently in the perlin_terrain module.
"""

from ursina.prefabs.first_person_controller import FirstPersonController

class Character():
    def __init__(self,speed=2):
        self.character = FirstPersonController()
        self.character.cursor.visible=False
        self.character.speed=speed
        self.character.gravity=0
        self.character.grav_acc=0.2
        self.character.grav_speed=0
        # character.gravity=0.6 # Maybe we leave this out (concision).
    
    def input(self,key):
        if key == 'escape':
            if self.character.enabled: 
                self.character.disable()
            else: self.character.enable()
    
    def move(self,_terrain):
        from ursina import lerp, time
        from numpy import floor

        # How high or low can we step/drop?
        # Just using this next line as hack before
        # refactoring -- i.e. we have copied across
        # this code from perlin_terrain.
        # So, we want to reference character variables
        # directly instead of through _character!
        _character = self.character
        step_height=3
        character_height=1.8

        # Need to adjust to correct position...
        x = _character.x + 0.5
        z = _character.z - 0.5
        y = _character.y

        # What y is the terrain at this position?
        target_y = floor((_terrain.noise([x/_terrain.freq,
                            z/_terrain.freq]))*_terrain.amp +
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