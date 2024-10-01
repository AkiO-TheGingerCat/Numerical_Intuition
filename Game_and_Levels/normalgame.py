import pygame
from Game_assets.button import load_buttons
import time
from Game_assets.question import MathQuestions
import random
from Game_assets.music import MusicStorage
from Game_database.normalgame_highscore_db import NormalGameHighScoreDB

class NormalGame:
    def __init__(self, display, gamestatemanager):
        self.display = display
        self.gamestatemanager = gamestatemanager

        # Load background and design images
        self.background_image = pygame.image.load('Game Images/Updated Background.png')
        self.designleft_image = pygame.image.load('Game Images/Game Paw Orange.png')
        self.designright_image = pygame.image.load('Game Images/Game Paw 1 Orange.png')

        self.designleft_image = pygame.transform.scale(self.designleft_image, (500, 450))
        self.designleft_rect = self.designleft_image.get_rect()
        self.designleft_rect.center = (self.display.get_width() // 3.50, self.display.get_height() // 2.5)

        self.designright_image = pygame.transform.scale(self.designright_image, (500, 450))
        self.designright_rect = self.designright_image.get_rect()
        self.designright_rect.center = (3 * self.display.get_width() // 4.10, self.display.get_height() // 2.5)

        # Time and Scoring
        self.start_time = None
        self.countdown_duration = 90
        self.start_message = True
        self.score = 0

        # Load Questions
        self.math_questions = MathQuestions()
        self.questions_category_1 = self.math_questions.questions_by_category[1]
        random.shuffle(self.questions_category_1)

        self.current_question_index = -1

        # Input and Music setup
        self.input_box = pygame.Rect(360, 500, 140, 32)
        self.color_inactive = pygame.Color('white')
        self.color_active = pygame.Color('black ')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.music_storage = MusicStorage()
        self.feedback_message = ''

        # High score database
        self.normalgame_highscore_db = NormalGameHighScoreDB()

    def run(self):
        self.display.blit(self.background_image, (0, 0))
        self.home_button = load_buttons('home')[0]

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.home_button.is_clicked(pos):
                    self.reset_game()
                    self.gamestatemanager.set_state('normalplay')
                if self.input_box.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False

                self.color = self.color_active if self.active else self.color_inactive

            if event.type == pygame.KEYDOWN and self.start_time is not None and time.time() - self.start_time < self.countdown_duration:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        if self.text.strip():
                            if 0 <= self.current_question_index < len(self.questions_category_1):
                                _, correct_answer = self.questions_category_1[self.current_question_index]
                                user_answer = int(self.text.strip())
                                if user_answer == correct_answer:
                                    self.score += 1
                                    self.start_time += 10
                                    self.music_storage.play_correct_sound()
                                    self.text = ''
                                    self.feedback_message = ''
                                    if not self.feedback_message:
                                        self.next_question()
                                else:
                                    if user_answer < correct_answer:
                                        self.feedback_message = 'Higher'
                                    else:
                                        self.feedback_message = 'Lower'
                                    self.music_storage.play_wrong_sound()

                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.start_time is None:
                    self.start_time = time.time()
                    self.start_message = False

                    self.designleft_rect.center = (5, self.display.get_height() // 2.5)
                    self.designright_rect.center = (
                    3 * self.display.get_width() // 2.97, self.display.get_height() // 2.5)

        if self.start_message:
            font = pygame.font.Font('Fonts/SuperSalad-qZgvV.ttf', 36)
            text_surface = font.render("Press SPACE to start", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.topright = (self.display.get_width() - 10, 10)
            self.display.blit(text_surface, text_rect)
        else:
            if self.start_time is not None:
                if self.current_question_index == -1:
                    self.next_question()

                if self.current_question_index < len(self.questions_category_1):
                    self.display_question()

            elapse_time = int(time.time() - self.start_time)
            remaining_time = max(self.countdown_duration - elapse_time, 0)
            if remaining_time == 0:
                font = pygame.font.Font('Fonts/SuperSalad-qZgvV.ttf', 50)
                game_over_surface = font.render("Game Over", True, (255, 0, 0))
                game_over_rect = game_over_surface.get_rect()
                game_over_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)
                self.display.blit(game_over_surface, game_over_rect)

                current_score = self.score
                high_score = self.normalgame_highscore_db.get_highscore()

                if current_score > high_score:
                    self.normalgame_highscore_db.insert_score(current_score)
                    high_score = current_score

                high_score_surface = font.render("Highscore: {}".format(self.score), True, (255, 255, 255))
                high_score_rect = high_score_surface.get_rect()
                high_score_rect.center = (self.display.get_width() // 2, self.input_box.y + 50)
                self.display.blit(high_score_surface, high_score_rect)

            else:
                minutes = remaining_time // 60
                seconds = remaining_time % 60
                font = pygame.font.Font('Fonts/SuperSalad-qZgvV.ttf', 36)
                text_surface = font.render("Time: {:02d}:{:02d}".format(minutes, seconds), True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topright = (self.display.get_width() - 10, 10)
                self.display.blit(text_surface, text_rect)

                font = pygame.font.Font('Fonts/SuperSalad-qZgvV.ttf', 36)
                score_surface = font.render("Score: {}".format(self.score), True, (255, 255, 255))
                score_rect = score_surface.get_rect()
                score_rect.topleft = (10, 10)
                self.display.blit(score_surface, score_rect)

                pygame.draw.rect(self.display, (255, 255, 255), self.input_box)

                pygame.draw.rect(self.display, self.color, self.input_box, 2)
                font = pygame.font.Font(None, 32)
                txt_surface = font.render(self.text, True, self.color)

        if self.feedback_message:
            font = pygame.font.Font('Fonts/SuperSalad-qZgvV.ttf', 24)
            feedback_surface = font.render(self.feedback_message, True, (255, 0, 0))
            feedback_rect = feedback_surface.get_rect()
            feedback_rect.midbottom = (self.display.get_width() // 2, self.input_box.top - 5)
            self.display.blit(feedback_surface, feedback_rect)

        self.display.blit(self.designleft_image, self.designleft_rect)
        self.display.blit(self.designright_image, self.designright_rect)

        txt_surface = font.render(self.text, True, self.color)
        width = max(150, txt_surface.get_width() + 1)
        self.input_box.w = width
        self.display.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))

        self.home_button.draw(self.display)

    def reset_game(self):
        self.start_time = None
        self.start_message = True
        self.score = 0
        self.current_question_index = -1
        self.text = ''
        self.feedback_message = ''

        self.designleft_rect.center = (self.display.get_width() // 3.50, self.display.get_height() // 2.5)
        self.designright_rect.center = (3 * self.display.get_width() // 4.10, self.display.get_height() // 2.5)

        self.normalgame_highscore_db.close()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index >= len(self.questions_category_1):
            self.current_question_index = 0

    def display_question(self):
        if self.start_time is not None and time.time() - self.start_time < self.countdown_duration:
            if self.current_question_index >= 0 and self.current_question_index < len(self.questions_category_1):
                font = pygame.font.Font('Fonts/SuperSalad-qZgvV.ttf', 25)
                question, _ = self.questions_category_1[self.current_question_index]
                question_surface = font.render(question, True, (255, 255, 255))
                question_rect = question_surface.get_rect()
                question_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)
                self.display.blit(question_surface, question_rect)


if __name__ == '__main__':
    pygame.init()
    pygame.quit()
