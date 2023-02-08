greenface= Actor('character')
greenface.pos 100,50

WIDTH= 500
HEIGHT= 300
BACKGROUND _COLOR = (255,0,0)

def draw():
    screen.fill((0,0,250))
    greenface.draw()
def update():
    greenface.left = greenface.left +2


