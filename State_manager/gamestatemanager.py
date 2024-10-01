import pygame.time
from Game_assets.music import MusicStorage
class GameStateManager:
    def __init__(self, initial_state):
        self.states = {}
        self.current_state = initial_state
        self.clock = pygame.time.Clock()
        self.running = True

        self.music_storage = MusicStorage()

        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.mixer.init()

        pygame.mixer.music.load(self.music_storage.background_music_path)
        pygame.mixer.music.play(-1)

    def add_state(self, state_name, state):
        self.states[state_name] = state

    def set_state(self, state_name):
        self.current_state = state_name

    def get_state(self):
        return self.current_state

    def run_current_state(self, display):
        self.states[self.current_state].run()
