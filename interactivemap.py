#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
myapp = App()

MAP = ImageAsset("images/US_map.png")

Sprite(MAP)

def capitalquiz:
    states = {'Alabama':0, 'Alaska':1, 'Arizona':2, 'Arkansas':3, 'California':4, 'Colorado':5, 'Connecticut':6,}
    capitals = ["Montegomery", "Juneau", 
    
def facts:

def findquiz:

myapp.run()
myapp.ListenKeyEvent('keydown','c',capitalquiz)
myapp.ListenKeyEvent('keydown','f',findquiz)
myapp.ListenKeyEvent('click','c',facts)
