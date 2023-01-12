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
        # will be getting user input
        
        # will be updating game logic
        
        # redrawing / updating sprites
        game.render_sprites([jon])
        game.tick()


if __name__ == "__main__":
    game_scene()
