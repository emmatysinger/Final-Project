# Interactive Map


## Functional Specification

This document should become the functional specification of the project you are working on.

A functional specification describes in great detail how a device or program will appear to an
outside user. That is, it treats all hardware as a "black box", the contents of which are completely
unknown to the user. The functional specification should include sections with the following information:

Your specification **should include** the following types of information:

* A title. Replace the title at the beginning of this document.
* Summary or introduction. In general, in a few lines or less, what is your program about or what is it about?
* How does the user access your program? Is it shared via https://runpython.org? Is a web site? Embedded in 
  a single board computer? 
* If there are graphics screens involved, describe every screen that the user will experience: what is it for? 
  What did the user have to do to get there and how does she move on to the next?
* For each graphics screen, describe every active control input and what it does. What elements on the screen will
  change in response to user input?
* Does the program respond to mouse input? What, exactly, does the mouse do?
* Does the program respond to keyboard input? How?
* What graphical assets will be used?
* Does the user have to do anything to install the program?

Your specification should **not** include the following types of information:

* The language you will use to create it.
* Names of any specific files in the project.
* How you will structure the classes, functions and code in your program.
* The name of any files or tools that you will use to design the program.


This program is an interactive map of the United States. There are 3 main features the user can use. The user can click on any state to learn more about the state. The user can play a capital game where they have to name of capital of a given state. Finally, the user can play find the state game, where they must locate a given state. 

The interactive map is accessible via https://runpython.org. 

The base graphic of this interactive map is a map of the United States with white dots on each state. In the bottom left corner are instructions on how to play the two availble games. 

Informational Mode: This is the default mode. Whenever the user quits either the capital quiz or the find the state game, the program returns to this mode.  
The user can click on a state by clicking on a white dot and a box in the graphics screen will pop up with information about the state. This includes the capital, the population and the nickname. 

Capital Quiz: The user can press the 'f' key to start and stop the quiz. When the quiz is started, the instructions box in the bottom left corner will change to be instructions about this quiz specifically. 
The user needs to press the spacebar to generate a new question. When the spacebar is pressed an input window will appear asking "What is the capital of STATE?" When the user answers the program will determine if they are correct or incorrect and tell the user on the console.  

Find the State Game: The user can press the 'c' key to start and stop the quiz. When the game is started, the instructions box in the bottom left corner will change to be instructions about this game specifically. 
Right away the user will be asked "Where is STATE?", this will appear in the console. The user has 10 seconds, which appears as a timer in the top right corner of the graphics screen, to answer by clicking on a state and the program will determine if the are correct or incorrect. If the user is correct, they will gain one point, which appears in the top left corner of the graphics screen and the program will ask a new question. If the user is incorrect, the program will reset the counter to 0 and will ask a new question. If the user clicked somewhere that is not a white dot, the user will be told in the console to click on a white dot. 
