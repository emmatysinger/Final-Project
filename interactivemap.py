#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
import random
myapp = App()

MAP = ImageAsset("images/US_map.png")

Sprite(MAP)

capital = FALSE
states = {'Alabama':0, 'Alaska':1, 'Arizona':2, 'Arkansas':3, 'California':4, 'Colorado':5, 'Connecticut':6, 'Delaware':7, 'Florida':8, 'Georgia':9, 'Hawaii':10, 'Idaho':11, 'Inidian':13, 'Iowa':14, 'Kansas':15, 'Kentucky':16, 'Lousiana':17, 'Maine':18, 'Maryland':19, 'Massachusetts':20, 'Michigan':12, 'Minnesota':22, 'Mississippi':23, 'Missouri':24, 'Montana':25, 'Nebraska':26, 'Nevada':27, 'New Hampshire':28, 'New Jersey':29, 'New Mexico':30, 'New York':31, 'North Carolina':32, 'North Dakota':33, 'Ohio':34, 'Oklahoma':35, 'Oregon':36, 'Pennsylvania':37, 'Rhode Island':38, 'South Carolina':39, 'South Dakota':40, 'Tennessee':41, 'Texas':42, 'Utah':43, 'Vermont':44, 'Virginia':45, 'Washington':46, 'West Virginia':47, 'Wisconsin':48, 'Wyoming':49} }
capitals = ["Montegomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "St. Paul", "Jackson", "Jeffereson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]
        
def capitalquiz(event):
    global capital, states, capitals
    capital = not capital
    while capital == TRUE:
        n = random.randint(0, 51)
        answer = input("What is the capital of" + n + "? ")
        if answer == capitals[n]:
            print ("CORRECT!")
        else:
            print ("Incorrect, the correct answer is" + capitals[n])
    
    
# def facts(event):

# def findquiz(event):

myapp.run()
myapp.ListenKeyEvent('keydown','c', capitalquiz)
# myapp.ListenKeyEvent('keydown','f',findquiz)
# myapp.ListenKeyEvent('click','c',facts)
