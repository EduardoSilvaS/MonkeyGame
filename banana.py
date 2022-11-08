import pygame as pg
import os
class banana:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.img_size = (200,200)
        self.bn_img = pg.transform.scale(pg.image.load(os.path.join("assets","banana.png")), self.img_size)
        self.mask = pg.mask.from_surface(self.bn_img)

        self.rect = pg.Rect(self.x, self.y, 200, 200)
        
    def draw(self, window):
        self.bn_img = pg.transform.scale(pg.image.load(os.path.join("assets","banana.png")), self.img_size)
        window.blit(self.bn_img, (self.x, self.y))

    def is_over(self, mouse):
        y_n = False # sim ou nao
        if self.rect.collidepoint(mouse):
            y_n = True
        return y_n