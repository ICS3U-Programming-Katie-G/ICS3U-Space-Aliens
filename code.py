# Created by: Katie Green
# Created: January 2023
# this is the wonderful jon's joyful jog video game :)

# importing some libraries to help build our game.
import stage
import ugame


# this is where all the game environment will be kept.
def game_scene():
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    while True:
        pass


if __name__ == "__main__":
    game_scene()
