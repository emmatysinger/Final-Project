#Emma Tysinger
#Credits:

#INTERACTIVE MAP
from ggame import *
from random import randint
import random

myapp = App()

#-----------    SPRITE INFO ----------------------------------------------------------------------------#
white = Color(0xfffafa, 1)
black = Color(0x000000, 1)
Medium_Aquamarine = Color(0x66cdaa, 1)
Pink = Color(0xeea2ad, 1)
line = LineStyle(1, black)
no_line = LineStyle(1, white)
Bright_Green = Color(0x00c957, 1)
Bright_Red = Color(0xee2c2c, 1)
Mute_Green = Color(0x00c957, 0.25)
Mute_Red = Color(0xee2c2c, 0.25)

#-----------    CREATE MAP ----------------------------------------------------------------------------#
MAP = ImageAsset("images/united-states-map-png-4-with-transparent-of-usa.png.jpeg")
Map=Sprite(MAP,(20,20))

width=myapp.width
height=myapp.height
mp_w = 2346
mp_h = 1484
if width/mp_w < 0.8*height/mp_h:
    Map.scale = (width-20)/mp_w
else:
    Map.scale = (0.8*height-20)/mp_h

#-----------    STATE COORDINATES   --------------------------------------------------------------------------#
coordinates = []
coordinates_i = [(740,480), (135,560), (225,415), (610,425), (85,335), (360,320), (965,200), (990,290), (865,573), (805,465), (370,645), (210,170), (670,295), (725,290), (585,245), (495,335), (765,335), (610,505), (1010,100), (905,280), (985,180), (740,205), (565,135), (675,475), (610,340), (310,105), (470,255), (145,260), (975,155), (940,260), (335,425), (910,175), (890,375), (465,110), (790,275), (515,405), (100,145), (875,240), (1015,240), (850,420), (460,180), (740,390), (475,500), (240,295), (950,135), (885,320), (130,60), (825,315), (645,170), (330,205)] 
for s in coordinates_i: 
    x,y = s
    coordinates.append((x/.44*Map.scale,y/.44*Map.scale))

dot_size = 8/.44*Map.scale
dot = CircleAsset(dot_size, line, white)
for s in coordinates:
    x,y = s
    Sprite(dot, (x, y))
    
Delaware = LineAsset(57/0.44*Map.scale, 4/.44*Map.scale, line)
Delaware = Sprite(Delaware, (935/0.44*Map.scale,290/0.44*Map.scale))
RI = LineAsset(25/0.44*Map.scale, 35/.44*Map.scale, line)
RI = Sprite(RI, (1000/0.44*Map.scale,205/0.44*Map.scale))

#-----------    VARIABLES   --------------------------------------------------------------------------#
blank = CircleAsset(1, no_line, white)
state_int = -1
state = 0
r_state = 0
count = Sprite(blank, (width,height))
time = Sprite(blank, (width,height))
box = Sprite(blank, (width,height))
go = 0
q = 0
states_used = []
correct_states = []

#------------    SPRITE CLASSES    --------------------------------------------------------------------------#
class Counter(Sprite):
    def __init__(self, count):
        texto = TextAsset(text = str(count), style = '45px Helvetica', color = black)
        super().__init__(texto, (0.01*width, 0.01*height))
        
class Timer(Sprite):
    def __init__(self, time):
        texto = TextAsset(text = str(time), style = '45px Helvetica')
        super().__init__(texto, (0.94*width, 0.01*height))

class FACT(Sprite):
    def __init__(self, facts, Line, Color):
        fact = TextAsset(text = facts, style ='18px Helvetica', width = 0.3*width-15)
        box = RectangleAsset(0.3*width - 10, fact.height, Line, Color)
        self.BOX = Sprite(box, (0.7*width - 10, 0.8*height))
        super().__init__(fact, (0.7*width, 0.8*height))
    
    def invisible(self):
        self.BOX.visible = False
        self.visible = False
        
class Correct(Sprite):
    global go
    def __init__(self,x,y):
        correct = ImageAsset("images/white_correct.png")
        super().__init__(correct, (x,y))
        self.vx = 0
        self.vy = 0
        
    def invisible(self):
        self.visible = False

    def action(self):
        self.vx += randint(0,4)/10
        self.vy += randint(0,4)/10
        self.x += randint(10,30)*sin(self.vx)
        self.y += randint(10,30)*cos(self.vy)

class Instructions(Sprite):
    def __init__(self,instruct,position, wid):
        instruction = TextAsset(text = instruct, style ='18px Helvetica', width = wid)
        super().__init__(instruction, position)

class Blinkers(Sprite):
    size = 15*width/1000
    box = RectangleAsset(5.5*size,3*size, line, white)
    yes = CircleAsset(size, line, Bright_Green)
    no = CircleAsset(size, line, Bright_Red)
    yes_off = CircleAsset(size, line, Mute_Green)
    no_off = CircleAsset(size, line, Mute_Red)
    
    def __init__(self):
        self.BOX = Sprite(self.box, (0.85*width - self.size/2, 0.9*height - self.size/2))
        self.YES_off = Sprite(self.yes_off, (0.85*width, 0.9*height))
        self.NO_off = Sprite(self.no_off, (0.85*width + 2.5*self.size, 0.9*height))
        self.YES = Sprite(self.yes, (0.85*width, 0.9*height))
        self.NO = Sprite(self.no, (0.85*width + 2.5*self.size, 0.9*height))

    
    def invisible(self):
        self.YES.visible = False
        self.NO.visible = False
        self.YES_off.visible = False
        self.NO_off.visible = False
        self.BOX.visible = False
        
    def visible(self):
        self.BOX.visible = True
        self.YES_off.visible = True
        self.NO_off.visible = True

#------------    INSTRUCTIONS    --------------------------------------------------------------------------#
Gbox = RectangleAsset(350,0.08*height, line, Pink)
Gbox = Sprite(Gbox, (0,0.919*height))
Fbox = RectangleAsset(275,0.18*height, line, Pink)
Fbox = Sprite(Fbox, (0,0.819*height))
Cbox = RectangleAsset(305,0.18*height, line, Pink)
Cbox = Sprite(Cbox, (0,0.819*height))

findstate_i = "Press 'f' to play Find the State"
capitalQ_i = "Press 'c' to play the Capital Quiz"
instruct_findstate = """You are playing 'Find the State'!
- Click on the white dot
- To quit the game press 'f' again"""
instruct_capitalq = """You are playing capital quiz!
- For a new question press the spacebar
- To quit the game press 'c' again"""   
GF = Instructions(findstate_i, (0.01*width,0.94*height), 150)
GC = Instructions(capitalQ_i, (0.01*width+175,0.94*height), 150)
F = Instructions(instruct_findstate, (0.01*width,0.85*height), 250)
C = Instructions(instruct_capitalq, (0.01*width,0.85*height), 280)
F.visible = False
C.visible = False
Fbox.visible = False
Cbox.visible = False
    
#----------    MORE VARIABLES   -------------------------------------------------------------------------#
i = FACT(" ", no_line, white)
yay = Correct(0,0)
yay.invisible()
capitalQ = False
stateQ = False
Time = False
yesno = Blinkers()
yesno.invisible()

#----------   STATE DATA    -----------------------------------------------------------------------------#
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Lousiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states_facts = {'Alabama':["Montegomery", "4,888,000", "Yellowhammer"], 'Alaska':["Juneau", "740,000", "Last Frontier"], 'Arizona':["Phoenix", "7,123,000", "Grand Canyon"], 'Arkansas':["Little Rock", "3,020,000", "Natural"], 'California':["Sacramento", "39,776,000", "Golden"], 'Colorado':["Denver", "5,684,000", "Centennial"], 'Connecticut':["Hartford", "3,588,000", "Constitution"], 'Delaware':["Dover", "971,180", "First"], 'Florida':["Tallahassee", "21,312,000", "Sunshine"], 'Georgia':["Atlanta", "10,545,000", "Peach"], 'Hawaii':["Honolulu", "1,426,000", "Aloha"], 'Idaho':["Boise", "1,753,000", "Gem"], 'Illinois':["Springfield", "12,768,000", "Prairie"], 'Indiana':["Indianapolis", "6,699,000", "Hoosier"], 'Iowa':["Des Moines", "3,160,000", "Hawkeye"], 'Kansas':["Topeka", "2,918,000", "Sunflower"], 'Kentucky':["Frankfort", "4,472,000", "Bluegrass"], 'Lousiana':["Baton Rouge", "4,682,000", "Pelican"], 'Maine':["Augusta", "1,341,000", "Pine Tree"], 'Maryland':["Annapolis", "6,079,000", "Old Line"], 'Massachusetts':["Boston", "6,895,000", "Bay"], 'Michigan':["Lansing", "9,991,000", "Great Lakes"], 'Minnesota':["St. Paul", "5,628,000", "North Star"], 'Mississippi':["Jackson", "2,982,000", "Magnolia"], 'Missouri':["Jefferson City", "6,135,000", "Show Me"], 'Montana':["Helena", "1,062,000", "Treasure"], 'Nebraska':["Lincoln", "1,932,000", "Cornhusker"], 'Nevada':["Carson City", "3,056,000", "Silver"], 'New Hampshire':["Concord", "1,350,000", "Granite"], 'New Jersey':["Trenton", "9,032,000", "Garden"], 'New Mexico':["Santa Fe", "2,090,000", "Land of Enchantment"], 'New York':["Albany", "19,862,000", "Empire"], 'North Carolina':["Raleigh", "10,390,000", "Tar Heel"], 'North Dakota':["Bismarck", "755,000", "Peace Garden"], 'Ohio':["Columbus", "11,694,000", "Buckeye"], 'Oklahoma':["Oklahoma City", "3,940,000", "Sooner"], 'Oregon':["Salem", "4,199,593", "Beaver"], 'Pennsylvania':["Harrisburg", "12,823,000", "Keystone"], 'Rhode Island':["Providence", "1,061,000", "Ocean"], 'South Carolina':["Columbia", "5,088,000", "Palmetto"], 'South Dakota':["Pierre", "877,790", "Mount Rushmore"], 'Tennessee':["Nashville", "6,782,000", "Volunteer"], 'Texas':["Austin", "28,704,330", "Lone Star"], 'Utah':["Salt Lake City", "3,159,000", "Beehive"], 'Vermont':["Montpelier", "623,000", "Green Mountain"], 'Virginia':["Richmond", "8,525,000", "Old Dominion"], 'Washington':["Olympia", "7,530,000", "Evergreen"], 'West Virginia':["Charleston", "1,803,000", "Mountain"], 'Wisconsin':["Madison", "5,818,000", "Badger"], 'Wyoming':["Cheyenne", "573,000", "Equality"]}

#----------   UNIVERSAL FUNCTIONS    ---------------------------------------------------------------------#
def rand_state():
    global states, r_state, states_used, go, r, yay, q, stateQ, capitalQ, Time, correct_states
    r_state = random.choice(states)
    if len(states_used) < 50:
        while r_state in states_used:
            r_state = random.choice(states)
        states_used.append(r_state)
    elif len(states_used) == 50:
        states_used = []
    
    if len(correct_states) == 50:
        Time = False
        yay = Correct(width/2,height/2)
        go = True
        r = 0
        q = 0
        if stateQ == True:
            print("CONGRATS! You have found all 50 states")
            stateQ = False
        if capitalQ == True:
            print("CONGRATS! You named the capital of all 50 states")
            capitalQ = False

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
    global r_state, yay, go, r, t, o, time, yesno, c, count, correct_states
    rand_state()
    if stateQ == True:
        print("Where is {0}?".format(r_state))
        t = 10
        time.visible = False
        time = Timer(t)
        o = 0
    if capitalQ == True:
        answer = input("""What is the capital of {0}? 
        
        
        
        
        
        
         
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """.format(r_state))
        correct_answer = states_facts[r_state]
        correct_answer = correct_answer[0]
        if answer == correct_answer:
            yesno.NO.visible = False
            yesno.YES.visible = True
            c += 1
            count = Counter(c)
            correct_states.append(correct_answer)
        else:
            yesno.NO.visible = True
            yesno.YES.visible = False
            c = 0
            count = Counter(c)
            correct_states = []
            print ("Incorrect, the capital of {0} is {1}!".format(r_state, correct_answer))
            
def visible():
    i.invisible()
    yay.invisible()
    count.visible = False
    
    if stateQ == True or capitalQ == True:
        GF.visible = False
        GC.visible = False
        Gbox.visible = False
        yesno.visible()
    else: 
        GF.visible = True
        GC.visible = True
        F.visible = False
        C.visible = False
        Fbox.visible = False
        Cbox.visible = False
        Gbox.visible = True
        yesno.invisible()
    
    if stateQ == True:
        F.visible = True
        Fbox.visible = True
    elif capitalQ == True:
        C.visible = True
        Cbox.visible = True

def step():
    global go, r, t, o, stateQ, time, count, Time, q 
    if go == True:
        q += 1
        r += 1
        if r == 3:
            yay.action()
            r = 0
    if Time == True:
        if t == 0:
            time.visible = False
            count.visible = False
            count = Counter(0)
            print("You ran out of time. Press the space bar to start again")
            time = Timer(0)
            Time = False
        if o == 60:
            time.visible = False
            t -= 1
            time = Timer(t)
            o = 0
        else:
            o += 1
    
    if q == 300:
        go = False

#--------   KEY EVENTS    ------------------------------------------------------------------------------#
def capitalquiz(event):
    global capitalQ, i, states_used, count, c, correct_states
    capitalQ = not capitalQ
    states_used = []
    correct_states = []
    visible()
    if capitalQ == True:
        c = 0
        count = Counter(0)
        print("You are playing capital quiz")
    else:
        print("The capital quiz has ended")
    
def capitalQuiz(event):
    global go, yay, stateQ, capitalQ, count, Time
    if capitalQ == True:
        yay.invisible()
        visible()
        ask()
    if stateQ == True:
        ask()
        Time = True

    
def findstate(event):           
    global stateQ, i, c, count, Time, states_used, time, correct_states
    stateQ = not stateQ
    Time = not Time
    states_used = []
    correct_states = []
    visible()
    if stateQ == True:
        c = 0
        count = Counter(0)
        print("You are playing 'Find the State'")
    else:
        print("'Find the State' game has ended")
        time.visible = False

    ask()

def facts(event):
    global stateQ, capitalQ, states_facts, determinestate,  r_state, ask, i, box, c, count, Time, yesno, correct_states
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
    
    elif stateQ == True and Time == True:
        visible()
        if r_state == state:
            yesno.NO.visible = False
            yesno.YES.visible = True
            c += 1
            count = Counter(c)
            correct_states.append(r_state)
            ask()
        else:
            if state == 0:
                print("Please click on the white dot")
                count = Counter(c)
            else:
                print("Sorry that is {0}, please try again".format(state))
                yesno.NO.visible = True
                yesno.YES.visible = False
                c = 0
                count = Counter(c)
                correct_states = []
                


myapp.run(step)
myapp.listenKeyEvent('keydown','c', capitalquiz)
myapp.listenKeyEvent('keydown','f',findstate)
myapp.listenMouseEvent('click',facts)
myapp.listenKeyEvent('keydown','space', capitalQuiz)