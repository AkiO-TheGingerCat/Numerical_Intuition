import pygame

class MusicStorage:
    def __init__(self):
        self.background_music_path = 'Game Music/Game Background Music.wav'
        self.sound_effect1_path = 'Game Music/Button Sound.wav'
        self.sound_effect2_path = 'Game Music/Correct-Answer-Sound.wav'
        self.sound_effect3_path = 'Game Music/Wrong-answer-sound.wav'

    def play_button_sound(self):
        button_sound = pygame.mixer.Sound(self.sound_effect1_path)
        button_sound.play()

    def play_correct_sound(self):
        correct_sound = pygame.mixer.Sound(self.sound_effect2_path)
        correct_sound.play()

    def play_wrong_sound(self):
        wrong_sound = pygame.mixer.Sound(self.sound_effect3_path)
        wrong_sound.play()
