"""
Hello world! 2.0 - iteration
"""
from ursina import *

app = Ursina()

planet = Entity(model='sphere', texture='earth',scale=4)

app.run()