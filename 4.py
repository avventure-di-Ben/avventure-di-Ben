import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
AZZURRO = (0, 128, 255)
ROSSO = (255, 0, 0)
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
morte_list = pygame.sprite.Group()

todraw = pygame.sprite.Group()

class Block1(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 2

class Block2(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([30, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 2
        
class Player(pygame.sprite.Sprite):
    move_x = 0
    move_y = 0
    onground=False
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((7, 25))
        self.image.fill(AZZURRO)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 680
        todraw.add(self)
    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        screen.blit(self.image, (self.rect.x, self.rect.y))


pygame.init()

score = 0
player = Player()
all_sprites_list.add(player)

font = pygame.font.SysFont("brittanic", 25)
scritta = font.render("Prendi 30 blocchi prima che cadano, ma stai attento a quelli ROSSI!!", True, BLACK)


    

clock = pygame.time.Clock()

player.rect.y = 630

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                player.move_x =- 6
            if event.key == pygame.K_RIGHT:  
                player.move_x = 6
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT:
                player.move_x = 0
            if event.key == pygame.K_RIGHT:
                player.move_x = 0
    all_sprites_list.update()
    
    n = random.randrange(30)

    if n == 1:
        block = Block1(BLACK)
        block.rect.x = random.randrange(5, 875)
        block.rect.y = 0
        block_list.add(block)
        all_sprites_list.add(block)

    n = random.randrange(100)

    if n == 1:
        morte = Block2(ROSSO)
        morte.rect.x = random.randrange(5, 875)
        morte.rect.y = 0
        morte_list.add(morte)
        all_sprites_list.add(morte)



    for blocco in block_list:


        block_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        for giocatore in block_hit_list:
            block_list.remove(blocco)
            all_sprites_list.remove(blocco)
            score += 1
            print(score)  
        if blocco.rect.y > 640:
            block_list.remove(blocco)
            all_sprites_list.remove(blocco)            
    for blocco in morte_list:
        morte_hit_list = pygame.sprite.spritecollide(player, morte_list, True)
        for giocatore in morte_hit_list:
            all_sprites_list.remove(block_list, morte_list)
            score = 0
            print(score)  
            

    if score == 30:
        all_sprites_list.remove(player, block_list, morte_list)
        screen.fill(WHITE)
        exit()
        
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    screen.blit(scritta,(100, 20))
    pygame.display.flip()
    pygame.display.set_caption("Le avventure di Ben: livello 4")
    clock.tick(60)     