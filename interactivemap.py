#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
import random
myapp = App()

MAP = ImageAsset("images/US_map.png")

Sprite(MAP)

capital = False
states=['Alabama':("Montegomery"), 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states_facts = {'Alabama':("Montegomery"), 'Alaska':("Juneau"), 'Arizona':("Phoenix"), 'Arkansas':("Little Rock"), 'California':("Sacramento"), 'Colorado':( "Denver"), 'Connecticut':("Hartford"), 'Delaware':("Dover"), 'Florida':("Tallahassee"), 'Georgia':("Atlanta"), 'Hawaii':("Honolulu"), 'Idaho':("Boise"), 'Illnois':("Springfield"), 'Indiana':("Indianapolis"), 'Iowa':("Des Moines"), 'Kansas':("Topeka"), 'Kentucky':("Frankfort"), 'Lousiana':("Baton Rouge"), 'Maine':("Augusta"), 'Maryland':("Annapolis"), 'Massachusetts':("Boston"), 'Michigan':("Lansing"), 'Minnesota':("St. Paul"), 'Mississippi':("Jackson"), 'Missouri':("Jefferson City"), 'Montana':("Helena), 'Nebraska':("Lincoln"), 'Nevada':("Carson City"), 'New Hampshire':("Concord"), 'New Jersey':("Trenton"), 'New Mexico':("Santa Fe"), 'New York':("Albany"), 'North Carolina':("Raleigh"), 'North Dakota':("Bismarck"), 'Ohio':("Columbus"), 'Oklahoma':("Oklahoma City"), 'Oregon':("Salem"), 'Pennsylvania':("Harrisburg"), 'Rhode Island':("Providence"), 'South Carolina':("Columbia"), 'South Dakota':("Pierre"), 'Tennessee':("Nashville"), 'Texas':("Austin"), 'Utah':("Salt Lake City"), 'Vermont':("Montpelier"), 'Virginia':("Richmond"), 'Washington':("Olympia"), 'West Virginia':("Charleston"), 'Wisconsin':("Madison"), 'Wyoming':("Cheyenne")}
 
        
def capitalquiz(event):
    global capital, states, states_facts
    capital = not capital
    if capital == True:
        n = random.randint(0, 50)
        print(states{n})
        # answer = input("What is the capital of" + n + "? ")
        # if answer == capitals[n]:
        #     print ("CORRECT!")
        # else:
        #     print ("Incorrect, the correct answer is" + capitals[n])
    
    
# def facts(event):

# def findquiz(event):

myapp.run()
myapp.listenKeyEvent('keydown','c', capitalquiz)
# myapp.listenKeyEvent('keydown','f',findquiz)
# myapp.listenKeyEvent('click','c',facts)
