import pygame

class Botao(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, botao):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(f'{botao}'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]