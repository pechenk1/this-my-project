from pygame import *

FPS = 90
clock = time.Clock()

window = display.set_mode((700,700))
display.set_caption('PP Betka')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move_player(self):
        if key_pressed[K_s] and self.rect.y <= 599:
            self.rect.y += self.speed
        if key_pressed [K_w] and self.rect.y >= 1:
            self.rect.y -= self.speed
    def move_player2(self):
        if key_pressed[K_DOWN] and self.rect.y <= 699:
            self.rect.y += self.speed
        if key_pressed [K_UP] and self.rect.y >= 1:
            self.rect.y -= self.speed

game = True

police_station = GameSprite('police-station.png',0,0,700,700,0)
player1 = GameSprite('s.webp', 30, 20, 160, 160, 3)
player2 = GameSprite('s.webp', 500, 20, 160, 160, 3)
ball = GameSprite('ttt.webp', 350,350, 50,50,5)
while game:

    police_station.reset()
    key_pressed = key.get_pressed()
    player1.reset()
    player2.reset()
    ball.reset()


    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.move_player()
    player2.move_player2()
    display.update()
    clock.tick(FPS)