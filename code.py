#!/usr/bin/env python3

# Created by: Katie Green
# Created: January 2023
# this is the wonderful jon's joyful jog video game :)

# importing some libraries to help build our game.
import stage
import ugame


# this is where all the game environment will be kept.
def game_scene():
    # the image bank for the background and sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # creates a grid that the background exists in.
    background = stage.Grid(image_bank_background, 10, 8)

    # this is the sprite of jon, who is the playable character
    jon = stage.Sprite(image_bank_sprites, 4, 75, 66)

    # actually displaying the game
    game = stage.Stage(ugame.display, 60)

    # the two different layers of the game
    game.layers = [jon] + [background]

    # rendering the background
    game.render_block()

    while True:
        # getting user input.
        keys = ugame.buttons.get_pressed()

        # X is a constant that represents A.
        if keys & ugame.K_X:
            print("A")

        # O is a constant that represents B.
        if keys & ugame.K_O:
            print("B")

        # the start button.
        if keys & ugame.K_START:
            print("Start")

        # the select button.
        if keys & ugame.K_SELECT:
            print("Select")

        # the right button on the d-pad.
        if keys & ugame.K_RIGHT:
            # moves one pixel right, leaves y as is.
            jon.move(jon.x + 1, jon.y)

        # the left button on the d-pad.
        if keys & ugame.K_LEFT:
            # moves one pixel left, leaves y as is.
            jon.move(jon.x - 1, jon.y)

        # the up button on the d-pad
        if keys & ugame.K_UP:
            # moves one pixel up, leaves x as is.
            jon.move(jon.x, jon.y - 1)

        # the down button on the d-pad.
        if keys & ugame.K_DOWN:
            # moves one pixel down, leaves y as is.
            jon.move(jon.x, jon.y + 1)

        # will be updating game logic

        # redrawing / updating sprites
        game.render_sprites([jon])
        game.tick()


if __name__ == "__main__":
    game_scene()
