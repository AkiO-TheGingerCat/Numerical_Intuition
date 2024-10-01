import pygame
from Game_assets.music import MusicStorage

class Button():
    def __init__(self, x, y, image, scale, sound_effect_path):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.sound_effect = pygame.mixer.Sound(sound_effect_path)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, pos):
        if self.rect.collidepoint(pos):
            self.sound_effect.play()
            return True
        return False

def load_buttons(*buttons):
    music_storage = MusicStorage()
    loaded_buttons = []
    for button_name in buttons:
        if button_name == 'start':
            img = pygame.image.load('Game Images/Cat Paw White.png').convert_alpha()
            button = Button(25, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'exit':
            img = pygame.image.load('Game Images/Cat Paw White.png').convert_alpha()
            button = Button(425, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'play':
            img = pygame.image.load('Game Images/Cat Paw White.png').convert_alpha()
            button = Button(25, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'level':
            img = pygame.image.load('Game Images/Cat Paw White.png').convert_alpha()
            button = Button(425, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'orangeplay':
            img = pygame.image.load('Game Images/Cat Paw Orange.png').convert_alpha()
            button = Button(25, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'orangelevel':
            img = pygame.image.load('Game Images/Cat Paw Orange.png').convert_alpha()
            button = Button(425, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'blackplay':
            img = pygame.image.load('Game Images/Cat Paw Black.png').convert_alpha()
            button = Button(25, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'blacklevel':
            img = pygame.image.load('Game Images/Cat Paw Black.png').convert_alpha()
            button = Button(425, 300, img, 0.39, music_storage.sound_effect1_path)
        elif button_name == 'back':
            img = pygame.image.load('Game Images/Back Button.png').convert_alpha()
            button = Button(760, 560, img, 0.080, music_storage.sound_effect1_path)
        elif button_name == 'settings':
            img = pygame.image.load('Game Images/Setting Icon.png').convert_alpha()
            button = Button(765, 560, img, 0.070, music_storage.sound_effect1_path)
        elif button_name == 'home':
            img = pygame.image.load('Game Images/Home Button.png').convert_alpha()
            button = Button(760, 450, img, 0.070, music_storage.sound_effect1_path)
        elif button_name == 'profile':
            img = pygame.image.load('Game Images/Profile Cat 3.png').convert_alpha()
            button = Button(340, 510, img, 0.18, music_storage.sound_effect1_path)
        elif button_name == 'easy':
            img = pygame.image.load('Game Images/Cat Paw easy.png').convert_alpha()
            button = Button(5, 350, img, 0.30, music_storage.sound_effect1_path)
        elif button_name == 'normal':
            img = pygame.image.load('Game Images/Cat Paw Orange.png').convert_alpha()
            button = Button(280, 350, img, 0.30, music_storage.sound_effect1_path)
        elif button_name == 'hard':
            img = pygame.image.load('Game Images/Cat Paw Black.png').convert_alpha()
            button = Button(550, 350, img, 0.30, music_storage.sound_effect1_path)
        elif button_name == 'Vup':
            img = pygame.image.load('Game Images/Vup.png').convert_alpha()
            button = Button(710, 198, img, 0.10, music_storage.sound_effect1_path)
        elif button_name == 'Vdown':
            img = pygame.image.load('Game Images/Vdown.png').convert_alpha()
            button = Button(415, 198, img, 0.10, music_storage.sound_effect1_path)
        loaded_buttons.append(button)
    return loaded_buttons
