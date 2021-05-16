#импорты
from pygame import *
#окно
back = (200,255,255)
window = display.set_mode((600, 500))
display.set_caption("понг")
window.fill(back)
#фпс
clock = time.Clock()
FPS = 60
#игровой цикл
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
