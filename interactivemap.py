#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
import random

myapp = App()

MAP = ImageAsset("images/united-states-map-png-4-with-transparent-of-usa.png.jpeg")
Map=Sprite(MAP,(20,20))

width=myapp.width
height=myapp.height
mp_w = Map.width
mp_h = Map.height
if width/mp_w < 0.8*height/mp_h:
    Map.scale = (width-20)/mp_w
else:
    Map.scale = (0.8*height-20)/mp_h

coordinates = []
coordinates_i = [(740,480), (135,560), (225,415), (610,425), (85,335), (360,320), (965,200), (990,290), (865,573), (805,465), (370,645), (210,170), (670,295), (725,290), (585,245), (495,335), (765,335), (610,505), (1010,100), (905,280), (985,180), (740,205), (565,135), (675,475), (610,340), (310,105), (470,255), (145,260), (975,155), (940,260), (335,425), (910,175), (890,375), (465,110), (790,275), (515,405), (100,145), (875,240), (1015,240), (850,420), (460,180), (740,390), (475,500), (240,295), (950,135), (885,320), (130,60), (825,315), (645,170), (330,205)] 
for s in coordinates_i:
    x,y = s
    coordinates.append((x/.44*Map.scale,y/.44*Map.scale))

white = Color(0xfffafa, 1)
black = Color(0x000000, 1)
Medium_Aquamarine = Color(0x66cdaa, 1)
line = LineStyle(1, black)
no_line = LineStyle(1, white)
dot_size = 8/.44*Map.scale
dot = CircleAsset(dot_size, line, white)
blank = CircleAsset(1, no_line, white)
state_int = -1
state = 0
r_state = 0
count = Sprite(blank, (width,height))

box = Sprite(blank, (width,height))

for s in coordinates:
    x,y = s
    Sprite(dot, (x, y))

findstate_i = TextAsset("Press 'f' to play Find the State", style ='12pt Helvetica', width = 150)
capitalQ_i = TextAsset("Press 'c' to play the Capital Quiz", style ='12pt Helvetica', width = 150)
F = Sprite(findstate_i, (0.01*width,0.94*height))
C = Sprite(capitalQ_i, (0.01*width+175,0.94*height))

#---------------------------------------------------------------------------------------------------------------
class Counter(Sprite):
    def __init__(self, count):
        texto = TextAsset(text = str(count), style = '40pt Helvetica')
        super().__init__(texto, (0.01*width, 0.01*height))

class FACT(Sprite):
    def __init__(self, facts, Line, Color):
        fact = TextAsset(text = facts, style ='12pt Helvetica', width = 0.25*width-15)
        box = RectangleAsset(0.25*width - 10, fact.height, Line, Color)
        self.BOX = Sprite(box, (0.75*width - 10, 0.8*height))
        super().__init__(fact, (0.75*width, 0.8*height))
    
    def invisible(self):
        self.BOX.visible = False
        self.visible = False
        
class Correct(App):
    def __init__(self):
        super().__init__()
        correct = ImageAsset("images/white_correct.png")
        self.correct = Sprite(correct)

    def action():
        
    def invisible():
        self.correct.visible = False
        
i = FACT(" ", no_line, white)
#---------------------------------------------------------------------------------------------------------------
capitalQ = False
stateQ = False

states=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states_facts = {'Alabama':["Montegomery", "4,888,000", "Yellowhammer"], 'Alaska':["Juneau", "740,000", "Last Frontier"], 'Arizona':["Phoenix", "7,123,000", "Grand Canyon"], 'Arkansas':["Little Rock", "3,020,000", "Natural"], 'California':["Sacramento", "39,776,000", "Golden"], 'Colorado':["Denver", "5,684,000", "Centennial"], 'Connecticut':["Hartford", "3,588,000", "Constitution"], 'Delaware':["Dover", "971,180", "First"], 'Florida':["Tallahassee", "21,312,000", "Sunshine"], 'Georgia':["Atlanta", "10,545,000", "Peach"], 'Hawaii':["Honolulu", "1,426,000", "Aloha"], 'Idaho':["Boise", "1,753,000", "Gem"], 'Illinois':["Springfield", "12,768,000", "Prairie"], 'Indiana':["Indianapolis", "6,699,000", "Hoosier"], 'Iowa':["Des Moines", "3,160,000", "Hawkeye"], 'Kansas':["Topeka", "2,918,000", "Sunflower"], 'Kentucky':["Frankfort", "4,472,000", "Bluegrass"], 'Lousiana':["Baton Rouge", "4,682,000", "Pelican"], 'Maine':["Augusta", "1,341,000", "Pine Tree"], 'Maryland':["Annapolis", "6,079,000", "Old Line"], 'Massachusetts':["Boston", "6,895,000", "Bay"], 'Michigan':["Lansing", "9,991,000", "Great Lakes"], 'Minnesota':["St. Paul", "5,628,000", "North Star"], 'Mississippi':["Jackson", "2,982,000", "Magnolia"], 'Missouri':["Jefferson City", "6,135,000", "Show Me"], 'Montana':["Helena", "1,062,000", "Treasure"], 'Nebraska':["Lincoln", "1,932,000", "Cornhusker"], 'Nevada':["Carson City", "3,056,000", "Silver"], 'New Hampshire':["Concord", "1,350,000", "Granite"], 'New Jersey':["Trenton", "9,032,000", "Garden"], 'New Mexico':["Santa Fe", "2,090,000", "Land of Enchantment"], 'New York':["Albany", "19,862,000", "Empire"], 'North Carolina':["Raleigh", "10,390,000", "Tar Heel"], 'North Dakota':["Bismarck", "755,000", "Peace Garden"], 'Ohio':["Columbus", "11,694,000", "Buckeye"], 'Oklahoma':["Oklahoma City", "3,940,000", "Sooner"], 'Oregon':["Salem", "4,199,593", "Beaver"], 'Pennsylvania':["Harrisburg", "12,823,000", "Keystone"], 'Rhode Island':["Providence", "1,061,000", "Ocean"], 'South Carolina':["Columbia", "5,088,000", "Palmetto"], 'South Dakota':["Pierre", "877,790", "Mount Rushmore"], 'Tennessee':["Nashville", "6,782,000", "Volunteer"], 'Texas':["Austin", "28,704,330", "Lone Star"], 'Utah':["Salt Lake City", "3,159,000", "Beehive"], 'Vermont':["Montpelier", "623,000", "Green Mountain"], 'Virginia':["Richmond", "8,525,000", "Old Dominion"], 'Washington':["Olympia", "7,530,000", "Evergreen"], 'West Virginia':["Charleston", "1,803,000", "Mountain"], 'Wisconsin':["Madison", "5,818,000", "Badger"], 'Wyoming':["Cheyenne", "573,000", "Equality"]}
#---------------------------------------------------------------------------------------------------------------
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
        answer = input("""What is the capital of {0}? 
        
        
        
        
        
        
         
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """.format(r_state))
        correct_answer = states_facts[r_state]
        correct_answer = correct_answer[0]
        if answer == correct_answer:
            print ("CORRECT!")
        else:
            print ("Incorrect, the capital of {0} is {1}!".format(r_state, correct_answer))
            
def visible():
    i.invisible() 
    count.visible = False
    
    if stateQ == True or capitalQ == True:
        F.visible = False
        C.visible = False
    else: 
        F.visible = True
        C.visible = True

#---------------------------------------------------------------------------------------------------------------
def capitalquiz(event):
    global capitalQ, i
    capitalQ = not capitalQ
    visible()
    if capitalQ == True:
        print("You are playing capital quiz")
        print("For a new question press the spacebar")
        print("To quit the game press 'c' again")

    else:
        print("The capital quiz has ended")

    
def capitalQuiz(event):
    ask()
    
def findstate(event):           
    global stateQ, i, c, count
    stateQ = not stateQ
    visible()
    if stateQ == True:
        c = 0
        count = Counter(0)
        print("You are playing 'Find the State'")
        print("To quit the game press 'f' again")

    else:
        print("'Find the State' game has ended")

    ask()

def facts(event):
    global stateQ, capitalQ, states_facts, determinestate,  r_state, ask, i, box, c, count
    determinestate(event.x,event.y)
    if stateQ == False and capitalQ == False:
        if state == 0:
            print("Please try again")
        else:
            visible()
            facts = states_facts[state]
            facts = """
WELCOME TO {0}!
Capital: {1}
Population: {2}
Nickname: The {3} State
""".format(state, facts[0], facts[1], facts[2])
            i = FACT(facts, line, Medium_Aquamarine)
    
    elif stateQ == True:
        visible()
        if r_state == state:
            print("CORRECT!")
            c += 1
            count = Counter(c)
            ask()
        else:
            if state ==0:
                print("Please click on the white dot")
                count = Counter(c)
            else:
                print("Sorry that is {0}, please try again".format(state))
                c = 0
                count = Counter(c)


myapp.run()
myapp.listenKeyEvent('keydown','c', capitalquiz)
myapp.listenKeyEvent('keydown','f',findstate)
myapp.listenMouseEvent('click',facts)
myapp.listenKeyEvent('keydown','space', capitalQuiz)
