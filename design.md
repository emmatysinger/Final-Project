# Interactive Map

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

The design specification should include information like:

* What tools or frameworks will you use to build the project (e.g. https://runpython.org or ggame)?
* What language will you use for coding (usually Python 3)?
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?

For this project I will use https://runpython.org for coding the game and I will use ggame framework for graphics
For this project I will use Python 3

The bulk of the data for this program is about the states. The coordinates of each state is stored as the coordinates of a white dot in the center of each state. These coordinates are stored alphabetically in a list. There is a second list with the names of all the states in alphabetical order. All the information for each state is stored in a dictionary formated like: 
'state': ["capital","population size","nickname"]

I wrote an algorithm to determine which state the user is clicking on. The limitation of this algorithm is that the user but click on the white dot in each state for the algorithm to recognize the state.
A list of the coordinates of each state (the coordinates of the white dot on each state) in alphabetical order is created based on the screen size. 
When the screen is clicked a function named determinestate(x,y) is run. The x and y coordinates of where the user clicked are the puts. The algorithm looks to see if the difference between the x-coordinate of the click and the x-coordinate of the state is less than twice the radius of the white dot (which is dependent on the screen size). The same is done with the y-coordinates and if both are true then the algorithm stores that state as "state" and stops. If the preceding conditions are false the algorithm runs through every state until it either reaches a match or has compared the clicked coordinates to every state. 

Informational Mode:

Capital Quiz:

Find the State Game: 

