"""
Hello world! 2.0 - iteration
"""
from ursina import *
from random import randint

app = Ursina()
window.color=color.pink
tex='grass'
mod='cube'

def randVec3(rad=10):
    import numpy as np
    """
    [https://gist.github.com/andrewbolster/10274979]
    Generates a random 3D unit vector (direction) with a uniform spherical distribution
    Algo from http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
    :return:
    """
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta )
    return (x*rad,y*rad,z*rad)

for i in range(100):
    p = Entity(model=mod, texture=tex,
                position=randVec3())
    

def update():
    eyeball.rotation_y+=2*time.dt
    eyeball.rotation_x+=2*time.dt

eyeball = EditorCamera()



app.run()