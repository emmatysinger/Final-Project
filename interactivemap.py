#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
import random
myapp = App()

MAP = ImageAsset("images/united-states-map-png-4-with-transparent-of-usa.png.jpeg")
Map=Sprite(MAP,(20,20))
Map.scale = .44
coordinates = []

white = Color(0xfffafa, 1)
black = Color(0x000000, 1)
line = LineStyle(1, black)
dot = CircleAsset(10, line, white)


#---------------------------------------------------------------------------------------------------------------
capitalQ = False
stateQ = False
states=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states_facts = {'Alabama':["Montegomery"], 'Alaska':["Juneau"], 'Arizona':["Phoenix"], 'Arkansas':["Little Rock"], 'California':["Sacramento"], 'Colorado':[ "Denver"], 'Connecticut':["Hartford"], 'Delaware':["Dover"], 'Florida':["Tallahassee"], 'Georgia':["Atlanta"], 'Hawaii':["Honolulu"], 'Idaho':["Boise"], 'Illnois':["Springfield"], 'Indiana':["Indianapolis"], 'Iowa':["Des Moines"], 'Kansas':["Topeka"], 'Kentucky':["Frankfort"], 'Lousiana':["Baton Rouge"], 'Maine':["Augusta"], 'Maryland':["Annapolis"], 'Massachusetts':["Boston"], 'Michigan':["Lansing"], 'Minnesota':["St. Paul"], 'Mississippi':["Jackson"], 'Missouri':["Jefferson City"], 'Montana':["Helena"], 'Nebraska':["Lincoln"], 'Nevada':["Carson City"], 'New Hampshire':["Concord"], 'New Jersey':["Trenton"], 'New Mexico':["Santa Fe"], 'New York':["Albany"], 'North Carolina':["Raleigh"], 'North Dakota':["Bismarck"], 'Ohio':["Columbus"], 'Oklahoma':["Oklahoma City"], 'Oregon':["Salem"], 'Pennsylvania':["Harrisburg"], 'Rhode Island':["Providence"], 'South Carolina':["Columbia"], 'South Dakota':["Pierre"], 'Tennessee':["Nashville"], 'Texas':["Austin"], 'Utah':["Salt Lake City"], 'Vermont':["Montpelier"], 'Virginia':["Richmond"], 'Washington':["Olympia"], 'West Virginia':["Charleston"], 'Wisconsin':["Madison"], 'Wyoming':["Cheyenne"]}
#states_location = {'Alabama':[800,700], 'Alaska':[100,100], 'Arizona':[100,100], 'Arkansas':[700,600], 'California':[100,900], 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'}

# for s in states:
#      coordinates_list = states_location[s]
#      coordinates.append((coordinates_list[0], coordinates_list[1]))

for s in coordinates:
    x,y = coordinates[s]
    Sprite(dot, (x, y))

     
def capitalquiz(event):
    global capitalQ, states, states_facts
    capitalQ = not capitalQ
    if capitalQ == True:
        state = random.choice(states)
        answer = input("What is the capital of " + state + "? ")
        correct_answer = states_facts[state]
        correct_answer = correct_answer[0]
        if answer == correct_answer:
            print ("CORRECT!")
        else:
            print ("Incorrect, the capital of {0} is {1}!".format(state, correct_answer))
    

def findquiz(event):
    global stateQ, states, states_location
    stateQ = not stateQ
    if state == True:
        state = random.choice(states)

def facts(event):
    global stateQ, capitalQ, states_location, states_facts
    #while stateQ == False and capitalQ == False:

    
myapp.run()
myapp.listenKeyEvent('keydown','c', capitalquiz)
myapp.listenKeyEvent('keydown','f',findquiz)
myapp.listenKeyEvent('click','c',facts)
