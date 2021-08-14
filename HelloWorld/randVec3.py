def randVec3(rad=10):
    import numpy as np
    """
    [I added the radius parameter (see also return line) 
        and numpy import]
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