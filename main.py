import sys
import pygame
from State_manager.gamestatemanager import GameStateManager
from Game_and_Levels.play import Play
from start import Start
from Game_assets.profile import Profile
from Game_assets.settings import Setting
from Game_and_Levels.game import MainGame
from Game_and_Levels.level import Levels
from Game_and_Levels.normalgame import NormalGame
from Game_and_Levels.normalplay import NormalPlay
from Game_and_Levels.hardgame import HardGame
from Game_and_Levels.hardplay import HardPlay

SCREENWIDTH, SCREENHEIGHT = 850, 650
FPS = 90
pygame.display.set_caption("Numerical Intuition")
icon = pygame.image.load("Game Images/Logo.png")
pygame.display.set_icon(icon)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        self.gamestatemanager = GameStateManager('start')
        self.gamestatemanager.add_state('start', Start(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('play', Play(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('profile', Profile(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('settings', Setting(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('game', MainGame(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('level', Levels(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('normalgame', NormalGame(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('normalplay', NormalPlay(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('hardgame', HardGame(self.screen, self.gamestatemanager))
        self.gamestatemanager.add_state('hardplay', HardPlay(self.screen, self.gamestatemanager))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.gamestatemanager.run_current_state(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
