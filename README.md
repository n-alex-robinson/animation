# PSEUDOCODE

import pygame
import random

set up screen with 800x600 window
set title as "Bouncing DVD logo"

create surface as background
fill with colour (230, 190, 255)

load dvd.png
set position to 400x, 100y

start with a speed of 5 for both x and y directions

main game loop keeps running while keepGoing is true
set to 30fps
    
check for events
if user clicks the quit button, end the loop

move the DVD logo based on its speed (add speed to x and y coordinates)

collisions:
  if dvd hits left or right of screen:
    reverse x-direction
      add randomness to y-speed (-2 to 2)
  if dvd hits top or bottom of screen:
    reverse y-direction
      add randomness to x-speed (-1 to 1)

limit speed values (IMPORTANT)

refresh screen
draw background and dvd logo in updated position
update the display

quit when the game loop ends
