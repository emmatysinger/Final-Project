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

I wrote an algorithm to determine which state the user is clicking on. The limitation of this algorithm is that the user but click on the white dot in each state for the algorithm to recognize the state.
A list of the coordinates of each state (the coordinates of the white dot on each state) in alphabetical order is created based on the screen size. 
When the screen is clicked a function named determinestate() is run. 

