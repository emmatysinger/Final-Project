#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
import random
# import time
# import browser

myapp = App()

MAP = ImageAsset("images/united-states-map-png-4-with-transparent-of-usa.png.jpeg")
Map=Sprite(MAP,(20,20))
Map.scale = .44
coordinates = [(740,480), (135,560), (225,415), (610,425), (85,335), (360,320), (965,200), (990,290), (865,573), (805,465), (370,645), (210,170), (670,295), (725,290), (585,245), (495,335), (765,335), (610,505), (1010,100), (905,280), (985,180), (740,205), (565,135), (675,475), (610,340), (310,105), (470,255), (145,260), (975,155), (940,260), (335,425), (910,175), (890,375), (465,110), (790,275), (515,405), (100,145), (875,240), (1015,240), (850,420), (460,180), (740,390), (475,500), (240,295), (950,135), (885,320), (130,60), (825,315), (645,170), (330,205)] 

white = Color(0xfffafa, 1)
black = Color(0x000000, 1)
line = LineStyle(1, black)
dot = CircleAsset(8, line, white)
state_int = -1
state = 0
r_state = 0

for s in coordinates:
    x,y = s
    Sprite(dot, (x, y))

instructions = TextAsset("click 'f' to start the find the state game")
#instructions.style = 20pt Helvetica
Sprite(instructions, (900,900))

#---------------------------------------------------------------------------------------------------------------
capitalQ = False
stateQ = False

states=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states_facts = {'Alabama':["Montegomery", "4,888,000"], 'Alaska':["Juneau", "740,000"], 'Arizona':["Phoenix", "7,123,000"], 'Arkansas':["Little Rock", "3,020,000"], 'California':["Sacramento", "39,776,000"], 'Colorado':["Denver", "5,684,000"], 'Connecticut':["Hartford", "3,588,000"], 'Delaware':["Dover", "971,180"], 'Florida':["Tallahassee", "21,312,000"], 'Georgia':["Atlanta", "10,545,000"], 'Hawaii':["Honolulu", "1,426,000"], 'Idaho':["Boise", "1,753,000"], 'Illnois':["Springfield"], 'Indiana':["Indianapolis"], 'Iowa':["Des Moines"], 'Kansas':["Topeka"], 'Kentucky':["Frankfort"], 'Lousiana':["Baton Rouge"], 'Maine':["Augusta"], 'Maryland':["Annapolis"], 'Massachusetts':["Boston"], 'Michigan':["Lansing"], 'Minnesota':["St. Paul"], 'Mississippi':["Jackson"], 'Missouri':["Jefferson City"], 'Montana':["Helena"], 'Nebraska':["Lincoln"], 'Nevada':["Carson City"], 'New Hampshire':["Concord"], 'New Jersey':["Trenton"], 'New Mexico':["Santa Fe"], 'New York':["Albany"], 'North Carolina':["Raleigh"], 'North Dakota':["Bismarck"], 'Ohio':["Columbus"], 'Oklahoma':["Oklahoma City"], 'Oregon':["Salem"], 'Pennsylvania':["Harrisburg"], 'Rhode Island':["Providence"], 'South Carolina':["Columbia"], 'South Dakota':["Pierre"], 'Tennessee':["Nashville"], 'Texas':["Austin"], 'Utah':["Salt Lake City"], 'Vermont':["Montpelier"], 'Virginia':["Richmond"], 'Washington':["Olympia"], 'West Virginia':["Charleston"], 'Wisconsin':["Madison"], 'Wyoming':["Cheyenne"]}

def determinestate(x,y):
    global state_int, coordinates, state, states
    for s in range(len(coordinates)):
        state = 0
        m,n = coordinates[s]
        if abs(int(x)-m) <= 16 and abs(int(y)-n) <=16:
            d_state = s
            state = states[s]
            break

def ask():
    global r_state
    r_state = random.choice(states)
    if stateQ == True:
        print("Where is {0}?".format(r_state))
    if capitalQ == True:
        answer = input("What is the capital of " + r_state + "? ")
        correct_answer = states_facts[r_state]
        correct_answer = correct_answer[0]
        if answer == correct_answer:
            print ("CORRECT!")
        else:
            print ("Incorrect, the capital of {0} is {1}!".format(r_state, correct_answer))

def capitalquiz(event):
    global capitalQ
    capitalQ = not capitalQ
    if capitalQ == True:
        print("You are playing capital quiz")
    else:
        print("The capital quiz has ended")
    ask()
    

def capitalQuiz(event):
    ask()
    

def findstate(event):           
    global stateQ
    stateQ = not stateQ
    if stateQ == True:
        print("You are playing 'Find the State'")
    else:
        print("'Find the State' game has ended")
    ask()
        

def facts(event):
    global stateQ, capitalQ, states_facts, determinestate,  r_state, ask
    determinestate(event.x,event.y)
    if stateQ == False and capitalQ == False:
        if state == 0:
            print("Please try again")
        else:
            facts = states_facts[state]
            print("""
WELCOME TO {0}!
Capital: {1}
Population: 
""".format(state, facts[0]))
    
    elif stateQ == True:
        if r_state == state:
            print("CORRECT!")
            ask()
        else:
            if state ==0:
                print("Please click on the white dot")
            else:
                print("Sorry that is {0}, please try again".format(state))


myapp.run()
myapp.listenKeyEvent('keydown','c', capitalquiz)
myapp.listenKeyEvent('keydown','f',findstate)
myapp.listenMouseEvent('click',facts)
myapp.listenKeyEvent('keydown','space', capitalQuiz)
