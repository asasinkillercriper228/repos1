from pygame import*
window = display.set_mode((700, 500))
display.set_caption("пинг понг")
background = transform.scale(image.load('background.jpg'), (700, 500))
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, img, xx, yy, x, y, speed):
        super().__init__()

        self.image = transform.scale(
            image.load(img),
            (xx,yy)
        )
        self.x = xx
        self.y = yy
        self.rect = self.image.get_rect()
        self.Speed = speed

        self.x = x
        self.y = y

        self.rect.x = self.x
        self.rect.y = self.y

    def show(self):
        window.blit(self.image, (self.x, self.y))

class Player(GameSprite):
    def Control(self, keys):
        if keys[pygame.K_a] and self.rect.y - self.speed >= 0:
            self.y -= self.speed
        if keys[pygame.K_d] and self.rect.y + self.speed <= SIZE[0] - SHIP_SIZE[0]:
            self.y += self.speed
    def Control(self, keys):
        if keys[pygame.K_left] and self.rect.y - self.speed >= 0:
            self.y -= self.speed
        if keys[pygame.K_right] and self.rect.y + self.speed <= SIZE[0] - SHIP_SIZE[0]:
            self.y += self.speed
p1 = Player('sprite1.png', 30, 150, 10, 50, 5)       
p2 = Player('sprite2.png', 25, 150, 660, 50, 5) 
p3 = GameSprite('ball.png', 80, 80, 350, 50, 5)                    
game = True
while game:
    window.blit(background,(0, 0))
    p1.show()
    p2.show()
    p3.show()
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    clock.tick(60)
    display.update()

sprite1 = transform.scale(
    image.load('sprite1.png'),
    (100, 100)
)

window.blit(sprite1, (x1, y1))





    