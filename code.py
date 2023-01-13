# Created by: Katie Green
# Created: January 2023
# this is the wonderful jon's joyful jog video game :)

# importing some libraries to help build our game.
import stage
import ugame


# importing the constants file so we can use it in here.
import constants

# this is where all the game environment will be kept.
def game_scene():
    # the image bank for the background and sprites
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that we are going to check to see what state they are in
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # loading in the song and getting it all ready :)
    meow_sound = open("meow_sound.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # creates a grid that the background exists in.
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # this is the sprite of jon, who is the playable character
    # this locks the sprite's y position at the near-bottom of the screen.
    jon = stage.Sprite(image_bank_sprites, 4, 75, constants.SCREEN_Y - (constants.ADDED_BOTTOM + constants.SPRITE_SIZE))

    # this is the sprite of the enemy in the game: lasagna
    lasagna = stage.Sprite(image_bank_sprites, 9,
                    int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                    18)

    # actually displaying the game
    game = stage.Stage(ugame.display, constants.FPS)

    # the two different layers of the game - background and sprites
    game.layers = [jon] + [lasagna] + [background]

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
            print("Start")

        # the select button.
        if keys & ugame.K_SELECT != 0:
            print("Select")

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
            sound.play(meow_sound)

        # redrawing / updating sprites
        game.render_sprites([jon] + [lasagna])
        game.tick()


if __name__ == "__main__":
    game_scene()
