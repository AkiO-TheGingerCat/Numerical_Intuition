import pygame

class Slider:
    def __init__(self, position, width, height, min_value, max_value, initial_value):
        self.position = position
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        self.slider_rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.slider_color = (100, 100, 100)
        self.slider_handle_color = (200, 200, 200)
        self.dragging = False

    def draw(self, surface, handle_image):
        pygame.draw.rect(surface, self.slider_color, self.slider_rect)
        handle_rect = handle_image.get_rect(center=(
        int(self.position[0] + (self.value - self.min_value) / (self.max_value - self.min_value) * self.width),
        self.position[1] + self.height // 2))
        surface.blit(handle_image, handle_rect)

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        if new_value < self.min_value:
            self.value = self.min_value
        elif new_value > self.max_value:
            self.value = self.max_value
        else:
            self.value = new_value

    def is_clicked(self, pos):
        x, y = pos
        if self.slider_rect.collidepoint(x, y):
            self.dragging = True
            return True
        return False

    def update_value(self, pos):
        if self.dragging:
            x, y = pos
            new_value = self.min_value + (x - self.position[0]) / self.width * (self.max_value - self.min_value)
            self.set_value(new_value)
