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

width=myapp.width
height=myapp.height
mp_w = Map.width
mp_h = Map.height
if width/mp_w < height/mp_h:
    Map.scale = (width-20)/mp_w
else:
    Map.scale = (height-20)/mp_h
    
print(width, height, Map.scale)

coordinates = []
coordinates_i = [(740,480), (135,560), (225,415), (610,425), (85,335), (360,320), (965,200), (990,290), (865,573), (805,465), (370,645), (210,170), (670,295), (725,290), (585,245), (495,335), (765,335), (610,505), (1010,100), (905,280), (985,180), (740,205), (565,135), (675,475), (610,340), (310,105), (470,255), (145,260), (975,155), (940,260), (335,425), (910,175), (890,375), (465,110), (790,275), (515,405), (100,145), (875,240), (1015,240), (850,420), (460,180), (740,390), (475,500), (240,295), (950,135), (885,320), (130,60), (825,315), (645,170), (330,205)] 
for s in coordinates_i:
    x,y = s
    coordinates.append((x/.44*Map.scale,y/.44*Map.scale))

white = Color(0xfffafa, 1)
black = Color(0x000000, 1)
line = LineStyle(1, black)
dot_size = 8/.44*Map.scale
dot = CircleAsset(dot_size, line, white)
state_int = -1
state = 0
r_state = 0

for s in coordinates:
    x,y = s
    Sprite(dot, (x, y))

instructions = TextAsset("click 'f' to start the find the state game")
Sprite(instructions, (600,600))

#---------------------------------------------------------------------------------------------------------------
capitalQ = False
stateQ = False

states=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states_facts = {'Alabama':["Montegomery", "4,888,000"], 'Alaska':["Juneau", "740,000"], 'Arizona':["Phoenix", "7,123,000"], 'Arkansas':["Little Rock", "3,020,000"], 'California':["Sacramento", "39,776,000"], 'Colorado':["Denver", "5,684,000"], 'Connecticut':["Hartford", "3,588,000"], 'Delaware':["Dover", "971,180"], 'Florida':["Tallahassee", "21,312,000"], 'Georgia':["Atlanta", "10,545,000"], 'Hawaii':["Honolulu", "1,426,000"], 'Idaho':["Boise", "1,753,000"], 'Illnois':["Springfield", "12,768,000"], 'Indiana':["Indianapolis", "6,699,000"], 'Iowa':["Des Moines", "3,160,000"], 'Kansas':["Topeka", "2,918,000"], 'Kentucky':["Frankfort", "4,472,000"], 'Lousiana':["Baton Rouge", "4,682,000"], 'Maine':["Augusta", "1,341,000"], 'Maryland':["Annapolis", "6,079,000"], 'Massachusetts':["Boston", "6,895,000"], 'Michigan':["Lansing", "9,991,000"], 'Minnesota':["St. Paul", "5,628,000"], 'Mississippi':["Jackson", "2,982,000"], 'Missouri':["Jefferson City", "6,135,000"], 'Montana':["Helena", "1,062,000"], 'Nebraska':["Lincoln", "1,932,000"], 'Nevada':["Carson City", "3,056,000"], 'New Hampshire':["Concord", "1,350,000"], 'New Jersey':["Trenton", "9,032,000"], 'New Mexico':["Santa Fe", "2,090,000"], 'New York':["Albany", "19,862,000"], 'North Carolina':["Raleigh", "10,390,000"], 'North Dakota':["Bismarck", "755,000"], 'Ohio':["Columbus", "11,694,000"], 'Oklahoma':["Oklahoma City", "3,940,000"], 'Oregon':["Salem", "4,199,593"], 'Pennsylvania':["Harrisburg", "12,823,000"], 'Rhode Island':["Providence", "1,061,000"], 'South Carolina':["Columbia", "5,088,000"], 'South Dakota':["Pierre", "877,790"], 'Tennessee':["Nashville", "6,782,000"], 'Texas':["Austin", "28,704,330"], 'Utah':["Salt Lake City", "3,159,000"], 'Vermont':["Montpelier", "623,000"], 'Virginia':["Richmond", "8,525,000"], 'Washington':["Olympia", "7,530,000"], 'West Virginia':["Charleston", "1,803,000"], 'Wisconsin':["Madison", "5,818,000"], 'Wyoming':["Cheyenne", "573,000"]}

def determinestate(x,y):
    global state_int, coordinates, state, states
    for s in range(len(coordinates)):
        state = 0
        m,n = coordinates[s]
        if abs(int(x)-m) <= dot_size*2 and abs(int(y)-n) <= dot_size*2:
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
Population: {2}
""".format(state, facts[0], facts[1]))
    
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
