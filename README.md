### CONSOLE LABYRINTH

##### Goal
I just wanted to build a small project. I want you to help me grow the project as it is
an open source project if you are a beginner on open sources projects.

Here is a list that I haven't implemented, you can add these options:
1. The player can enter "r 3" for example to move 3 steps to the right and for the
    other directions too.
    In the Playground.move_player function, the step by default is set to one

2. What about a multi player game ?
    Socket are really easy to use in python, maybe you can help me there. :) :)
    
3. Add a functionality you think will make the game the best ever to be created

4. A level designer

#### How does it work ?
It's easy.<br />
When you launch the game, the level manager will load the last level played which is
registered to the "levels/data.ld" file (yes you can cheat if you want to finish the game),
it will then load the corresponding file in the "levels" folder. Each level is represented
by a file ending by ".cll". <br />
The level manager will then read its content and will pass it to the map which is going
to build a game field with the received data. A game field is just a 2 dimensional list.<br />
What's next ?<br>
We then need to listen to the player controls and checking that he doesn't want to go
outside of the field. Each time he chooses a direction we update the map by setting
the new player's position and replacing the last one by an empty space.<br />

###### Et voilà.
()[]