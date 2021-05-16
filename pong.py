#импорты
from pygame import *
#окно
back = (200,255,255)
window = display.set_mode((600, 500))
display.set_caption("понг")
window.fill(back)
#классы
class GameSprite(sprite.Sprite): 
    def __init__(self, img, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.speed = speed
    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
class raketka(GameSprite):
    def update_l():
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 6:
            self.rect.y += 5
        if keys_pressed[K_s] and self.rect.y < 494:
            self.rect.y -= 5
class ball(GameSprite):
    def __init__(self, img, x, y, width, height, speed_x, speed_y):
        super().init(img, x, y, 0, width, height)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def update_speeds(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
#фпс
clock = time.Clock()
FPS = 60
#игровой цикл
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
