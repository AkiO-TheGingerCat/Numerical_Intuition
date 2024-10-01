import pygame
class PhotoStorage:
    def __init__(self):
        self.storage = []

    def load_photos(self):
        self.storage.append((pygame.image.load('Game Profiles/Profile 2.png'), 10))
        self.storage.append((pygame.image.load('Game Profiles/Profile 3.png'), 50))
        self.storage.append((pygame.image.load('Game Profiles/Profile 4.png'), 100))
        self.storage.append((pygame.image.load('Game Profiles/Profile 5.png'), 150))
        self.storage.append((pygame.image.load('Game Profiles/Profile 6.png'), 250))
        self.storage.append((pygame.image.load('Game Profiles/Profile 7.png'), 300))
        self.storage.append((pygame.image.load('Game Profiles/Profile 8.png'), 400))
        self.storage.append((pygame.image.load('Game Profiles/Profile 9.png'), 450))
        self.storage.append((pygame.image.load('Game Profiles/Profile 10.png'), 500))
        self.storage.append((pygame.image.load('Game Profiles/Profile 11.png'), 600))
        self.storage.append((pygame.image.load('Game Profiles/Profile 12.png'), 750))
        self.storage.append((pygame.image.load('Game Profiles/Profile 13.png'), 900))
        self.storage.append((pygame.image.load('Game Profiles/Profile 14.png'), 1000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 15.png'), 1100))
        self.storage.append((pygame.image.load('Game Profiles/Profile 17.png'), 1250))
        self.storage.append((pygame.image.load('Game Profiles/Profile 18.png'), 1300))
        self.storage.append((pygame.image.load('Game Profiles/Profile 19.png'), 1400))
        self.storage.append((pygame.image.load('Game Profiles/Profile 20.png'), 1500))
        self.storage.append((pygame.image.load('Game Profiles/Profile 21.png'), 1600))
        self.storage.append((pygame.image.load('Game Profiles/Profile 22.png'), 1700))
        self.storage.append((pygame.image.load('Game Profiles/Profile 23.png'), 1800))
        self.storage.append((pygame.image.load('Game Profiles/Profile 24.png'), 1900))
        self.storage.append((pygame.image.load('Game Profiles/Profile 25.png'), 2000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 26.png'), 2150))
        self.storage.append((pygame.image.load('Game Profiles/Profile 27.png'), 2300))
        self.storage.append((pygame.image.load('Game Profiles/Profile 28.png'), 2600))
        self.storage.append((pygame.image.load('Game Profiles/Profile 29.png'), 3000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 30.png'), 3200))
        self.storage.append((pygame.image.load('Game Profiles/Profile 31.png'), 3400))
        self.storage.append((pygame.image.load('Game Profiles/Profile 32.png'), 3800))
        self.storage.append((pygame.image.load('Game Profiles/Profile 33.png'), 4000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 34.png'), 4400))
        self.storage.append((pygame.image.load('Game Profiles/Profile 35.png'), 4800))
        self.storage.append((pygame.image.load('Game Profiles/Profile 36.png'), 5000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 37.png'), 5500))
        self.storage.append((pygame.image.load('Game Profiles/Profile 38.png'), 6000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 39.png'), 7000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 40.png'), 8000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 41.png'), 9000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 42.png'), 10000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 43.png'), 10500))
        self.storage.append((pygame.image.load('Game Profiles/Profile 44.png'), 11000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 45.png'), 12000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 46.png'), 12500))
        self.storage.append((pygame.image.load('Game Profiles/Profile 47.png'), 13000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 48.png'), 13500))
        self.storage.append((pygame.image.load('Game Profiles/Profile 49.png'), 14000))
        self.storage.append((pygame.image.load('Game Profiles/Profile 50.png'), 15000))

    def get_image(self, index):
        if 0 <= index < len(self.storage):
            return self.storage[index]
        else:
            print("Invalid index")
            return None

# Example usage
if __name__ == "__main__":
    photo_storage = PhotoStorage()
    photo_storage.load_photos()
