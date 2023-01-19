# Created by: Katie Green
# Created: January 2023
# this is the wonderful jon's joyful jog video game :)

import random
import time

# importing the constants file so we can use it in here.
import constants

# importing some libraries to help build our game.
import stage
import ugame

# this is the splash scene
def splash_scene():

    # this is the noise that will play during the splash scene
    # initializing sound
    bass_sound = open("bass_sound.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(bass_sound)

    # the image bank for the background and sprites
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # this will set the background to image 0 in our image bank,
    # and it will make the size 16x16, tiles of 10x8.
    background = stage.Grid(image_bank_mt_background, 10, 8)

    # creates a grid that the background exists in.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # used this program to split the image into tile: 
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # actually displaying the game
    game = stage.Stage(ugame.display, constants.FPS)

    # the two different layers of the game - background and sprites.
    # contains the text for the menu scene overtop the background.
    game.layers = [background]

    # rendering the background
    game.render_block()

    # this will allow the splash scene to remain for 2 seconds.
    while True:
        # 2 second timer
        time.sleep(2.0)
        menu_scene()


# this is the menu scene
def menu_scene():
    # the image bank for the background and sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # adding text objects
    text = []

    # this allows us to actually print out the text
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # this is where the text will appear
    text1.move(20, 10)

    # this is what text will show up. hank anderson game studios :)
    text1.text("Hank Anderson\nGame Studios:\n\nJon's Joyful\nJog!")

    # adding to end of list.
    text.append(text1)

    # this is the secondary text, to tell the user to press start!
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )

    # this positions the text
    text2.move(20, 100)

    # press start text!
    text2.text("PRESS START!\nDO IT! PRESS!\n")

    # append the text to the list
    text.append(text2)

    # this will set the background to image 0 in our image bank,
    # and it will make the size 16x16, tiles of 10x8.
    background = stage.Grid(image_bank_background, 10, 8)

    # creates a grid that the background exists in.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    
    # actually displaying the game
    game = stage.Stage(ugame.display, constants.FPS)

    # the two different layers of the game - background and sprites.
    # contains the text for the menu scene overtop the background.
    game.layers = text + [background]

    # rendering the background
    game.render_block()

    while True:
        # getting user input.
        keys = ugame.buttons.get_pressed()

        # the start button.
        if keys & ugame.K_START != 0:
            game_scene()

        # redrawing
        game.tick()


# this is where all the game environment will be kept.
def game_scene():
    # the function to place our lasagna at the top of the screen
    def show_lasagna():
        for lasagna_number in range(len(lasagnas)):
            if lasagnas[lasagna_number].x < 0:
                lasagnas[lasagna_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                break

    # the image bank for the background and sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that we are going to check to see what state they are in
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # loading in the song and getting it all ready :)
    meow_sound = open("meow_sound.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # creates a grid that the background exists in.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # random tiles for the background woooo!!!
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location, y_location, tile_picked)

    # this is the sprite of jon, who is the playable character
    # this locks the sprite's y position at the near-bottom of the screen.
    jon = stage.Sprite(
        image_bank_sprites,
        4,
        75,
        constants.SCREEN_Y - (constants.ADDED_BOTTOM + constants.SPRITE_SIZE),
    )

    # this is the sprite of the enemy in the game: lasagna
    lasagnas = []
    for lasagna_number in range(constants.TOTAL_NUMBER_OF_LASAGNA):
        a_single_lasagna = stage.Sprite(
            image_bank_sprites,
            9,
            int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
            18,
        )
        # add the lasagna to the list of lasagna's
        lasagnas.append(a_single_lasagna)
    
    # placing our lasagna at the top of the screen
    show_lasagna()

    # create a nice list for when we launch garfield like catapult :)
    garfields = []
    for garfield_number in range(constants.TOTAL_NUMBER_OF_GARFIELD):
        a_single_garfield = stage.Sprite(
            image_bank_sprites, 10,
            constants.OFF_SCREEN_X,
            constants.OFF_SCREEN_Y,
        )
        # adds each new single garfield to the list of garfields.
        garfields.append(a_single_garfield)

    # actually displaying the game
    game = stage.Stage(ugame.display, constants.FPS)

    # the two different layers of the game - background and sprites
    game.layers = garfields + [jon] + lasagnas + [background]

    # rendering the background
    game.render_block()

    while True:
        # getting user input.
        keys = ugame.buttons.get_pressed()

        # the a button
        if keys & ugame.K_X != 0:
            # this will allow the a button to fire through a series of checks.
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # the b button
        if keys & ugame.K_O != 0:
            # passing because we don't need it right now (for the future though)
            pass

        # the start button.
        if keys & ugame.K_START != 0:
            # yass
            pass

        # the select button.
        if keys & ugame.K_SELECT != 0:
            # yass
            pass

        # the right button on the d-pad.
        if keys & ugame.K_RIGHT:
            # check to make sure it's not going off screen
            if jon.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                # moves one pixel right, leaves y as is.
                jon.move(jon.x + 1, jon.y)
            else:
                # if the x position is greater than screen limit, moves back to screen limit.
                jon.move(constants.SCREEN_X - constants.SPRITE_SIZE, jon.y)

        # the left button on the d-pad.
        if keys & ugame.K_LEFT:
            # check to make sure it's not going off screen
            if jon.x >= 0:
                # moves one pixel left, leaves y as is.
                jon.move(jon.x - 1, jon.y)
            else:
                # if the x position is less than 0, then moves jon back to 0.
                jon.move(0, jon.y)

        # the up button on the d-pad
        if keys & ugame.K_UP:
            # we don't want the character to move up or down, so we pass.
            pass

        # the down button on the d-pad.
        if keys & ugame.K_DOWN:
            # don't want character moving up or down, so pass
            pass

        # the logic of the game, controls when the sound plays
        if a_button == constants.button_state["button_just_pressed"]:
            # throw garfield but only if there are still garfields left to be thrown
            for garfield_number in range(len(garfields)):
                if garfields[garfield_number].x < 0:
                    garfields[garfield_number].move(jon.x, jon.y)
                    sound.play(meow_sound)
                    break

        # move garfield for each frame he's on the screen
        for garfield_number in range(len(garfields)):
            if garfields[garfield_number].x > 0:
                garfields[garfield_number].move(garfields[garfield_number].x, garfields[garfield_number].y - constants.GARFIELD_SPEED)
                if garfields[garfield_number].y < constants.OFF_TOP_SCREEN:
                    garfields[garfield_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # move the lasagna down the screen
        for lasagna_number in range(len(lasagnas)):
            if lasagnas[lasagna_number].x > 0:
                lasagnas[lasagna_number].move(lasagnas[lasagna_number].x, lasagnas[lasagna_number].y + constants.LASAGNA_SPEED)
                if lasagnas[lasagna_number].y > constants.SCREEN_Y:
                    lasagnas[lasagna_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_lasagna()

        # redrawing / updating sprites
        game.render_sprites(garfields + [jon] + lasagnas)
        game.tick()


if __name__ == "__main__":
    splash_scene()
