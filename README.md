# PSEUDOCODE

import pygame<br/>
import random<br/>

set up screen with 800x600 window<br/>
set title as "Bouncing DVD logo"<br/>

create surface as background<br/>
fill with colour (230, 190, 255)<br/>

load dvd.png<br/>
set position to 400x, 100y<br/>

start with a speed of 5 for both x and y directions<br/>

main game loop keeps running while keepGoing is true<br/>
set to 30fps<br/>
    
check for events<br/>
if user clicks the quit button, end the loop<br/>

move the DVD logo based on its speed (add speed to x and y coordinates)<br/>

collisions:<br/>
  if dvd hits left or right of screen:<br/>
    reverse x-direction<br/>
      add randomness to y-speed (-2 to 2)<br/>
  if dvd hits top or bottom of screen:<br/>
    reverse y-direction<br/>
      add randomness to x-speed (-1 to 1)<br/>

limit speed values (IMPORTANT)<br/>

refresh screen<br/>
draw background and dvd logo in updated position<br/>
update the display<br/>

quit when the game loop ends<br/>
