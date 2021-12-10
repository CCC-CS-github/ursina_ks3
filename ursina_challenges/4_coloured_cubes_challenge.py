from ursina import *

app = Ursina()

window.color = color.rgb(200,200,0)

tl = Entity(model='cube',color=color.red)
tr = Entity(model='cube',color=color.green)
bl = Entity(model='cube',color=color.blue)
br = Entity(model='cube',color=color.rgb(200,0,200))

pos = 2

tl.x = -pos
bl.x = -pos
tr.x = pos
br.x = pos
tl.y = pos
bl.y = -pos
tr.y = pos
br.y = -pos

app.run()
