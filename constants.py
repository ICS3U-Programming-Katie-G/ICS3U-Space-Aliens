#!/usr/bin/env python3

# Created by: Katie
# Created on: January 2023
# This file contains all the constants for code.py

# The PyBadge screen size is 160x128, and sprites are 16x16.
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
# the frames per second is 60, and the sprites move 1 pixel each time they move.
FPS = 60
SPRITE_MOVEMENT_SPEED = 1
# this is the value we're adding to the bottom of the sprite margin,
# just so I can add a little more
ADDED_BOTTOM = 8

# dictionary with all the constants required for anything to do with button states.
# this is important because we want the sound to function right - we only want to play the sound
# when the button has just been pressed.
button_state = {
    "button_up": "up",
    "button_just_pressed" : "just pressed",
    "button_still_pressed" : "still pressed",
    "button_released" : "released"
}

# nice new shiny pallet for red filled text :)
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
