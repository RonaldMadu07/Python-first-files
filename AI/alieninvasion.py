import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import gamefunctions as gf

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for this game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets) 
        ship.update()
        gf.update_bullets(bullets)
        bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in bullets.copy():
            if bullets.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)            

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible. 
        pygame.display.flip()

run_game()