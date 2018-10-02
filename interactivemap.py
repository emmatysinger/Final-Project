#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
import randint
myapp = App()

MAP = ImageAsset("images/US_map.png")

Sprite(MAP)

capital = FALSE
states = {'Alabama':0, 'Alaska':1, 'Arizona':2, 'Arkansas':3, 'California':4, 'Colorado':5, 'Connecticut':6,}
capitals = ["Montegomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford"]
        
def capitalquiz:
    global capital, states, capitals
    capital = not capital
    while capital = TRUE:
        n = randint
        answer = input("What is the capital of" + n + "? ")
        if answer == capitals[n]:
            print ("CORRECT!")
        else:
            print ("Incorrect, the correct answer is" + capitals[n])
    
    
def facts:

def findquiz:

myapp.run()
myapp.ListenKeyEvent('keydown','c',capitalquiz)
myapp.ListenKeyEvent('keydown','f',findquiz)
myapp.ListenKeyEvent('click','c',facts)
