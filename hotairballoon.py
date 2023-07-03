import pygame
import random
from pygame import mixer

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.display.set_caption('Hot Air Balloon')
icon = pygame.image.load('data/air-hot-balloon.png')
pygame.display.set_icon(icon)

screenwid = 400
screenhigh = 500

screen = pygame.display.set_mode((screenwid, screenhigh))

bg = pygame.image.load('E:/bgparacute.jpg')

skybg = pygame.image.load('data/sky.png')

mainbg = pygame.image.load('data/mainmenu.png')

endscreen = pygame.image.load('data/endscreen (2).png')

playbtn = pygame.image.load('data/playbtn.png')

replay = pygame.image.load('data/replay.png')

scorefont = pygame.font.Font('data/Pixellari.ttf', 20)

black = (0, 0, 0)

spike_image = pygame.image.load('data/spikesfinal.png')

mixer.music.load("data/hotair balloon musicccc.wav")
mixer.music.play(-1)

selection = mixer.Sound('data/selection.wav')

movement = mixer.Sound('data/movement.wav')

collision = mixer.Sound('data/collision1.wav')


class Balloon(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/hotairballonpng.png').convert()
        self.image.set_colorkey(black)
        self.size = self.image.get_size()
        self.bigger_img = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left and self.rect.left > -35:
            self.rect.x -= 4
        if self.moving_right and self.rect.right < 365:
            self.rect.x += 4
        if self.moving_up and self.rect.top > -25:
            self.rect.y -= 4
        if self.moving_down and self.rect.bottom < 445:
            self.rect.y += 4

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.moving_left = True
                movement.play()
            elif event.key == pygame.K_RIGHT:
                self.moving_right = True
                movement.play()
            elif event.key == pygame.K_UP:
                self.moving_up = True
                movement.play()
            elif event.key == pygame.K_DOWN:
                self.moving_down = True
                movement.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.moving_right = False
            elif event.key == pygame.K_UP:
                self.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.moving_down = False

    def draw(self, screen):
        screen.blit(self.bigger_img, self.rect)


class Spike(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/spikesfinal.png').convert()
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-100, 200)
        self.rect.y = -self.rect.height
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= screenhigh:
            self.kill()


#balloon = Balloon(145, 250, 'E:/HOTair Balloon/hotairballonpng.png')
#spike_group = pygame.sprite.Group()


def main():
    while True:
        screen.blit(mainbg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                    selection.play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if 320 > my > 260 and 135 < mx < 270:
                    gameloop()
                    selection.play()

        fontsponsor = pygame.font.Font('data/upheavtt.ttf', 15)
        sponsor = fontsponsor.render("ALLI", True, (0, 0, 0))
        screen.blit(sponsor, (175, 485))
        
        with open("data/hiscore!.txt", "r") as f:
            hiscore = f.read()
        highscore = scorefont.render('highscore : ' + str(hiscore), True, (0,0,0))
        screen.blit(highscore, [135, 370])

        screen.blit(playbtn, (0, 75))
        clock.tick(100)
        pygame.display.update()


def gameloop():
    gameover = False
    gameclose = False
    
    with open("data/hiscore!.txt", "r") as f:
        hiscore = f.read()
    
    balloon = Balloon(145, 250, 'data/hotairballonpng.png')
    spike_group = pygame.sprite.Group()
    
    score = 0
    clock_started = False
    start_time = 0
    
    def showscore(x, y,):
        score_text = scorefont.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (x, y))

    last_spike_time = pygame.time.get_ticks()
    spike_speed = 2
    spike_delay = 1200

    while not gameover:

        while gameclose:
            while True:
                screen.blit(endscreen, (0, 0))
                fontsponsor = pygame.font.Font('data/upheavtt.ttf', 15)
                sponsor = fontsponsor.render("ALLI", True, (0, 0, 0))
                screen.blit(sponsor, (175, 485))

                screen.blit(replay, (0, 75))
                
                with open("data/hiscore!.txt", "w") as f:
                    f.write(str(hiscore))
                
                showscore(160, 350)
                highscore = scorefont.render('highscore : ' + str(hiscore), True, (0,0,0))
                screen.blit(highscore, [135, 370])
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameover = True
                            gameclose = False
                            pygame.quit()
                        if event.key == pygame.K_p:
                            gameloop()
                            selection.play()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if 320 > my > 260 and 135 < mx < 270:
                            gameclose = False
                            gameloop()
                            selection.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameover = True

            balloon.handle_event(event)
        screen.blit(skybg, (0, 0))


        current_time = pygame.time.get_ticks()
        if current_time - last_spike_time >= spike_delay:
            spike = Spike(spike_speed)
            spike_group.add(spike)
            last_spike_time = current_time
            
        balloon.update()
        balloon.draw(screen)
        spike_group.update()
        spike_group.draw(screen)

        # Collision detection
        for spike in spike_group:
            balloon_mask = pygame.mask.from_surface(balloon.bigger_img)
            spike_mask = pygame.mask.from_surface(spike.image)

            offset = (spike.rect.x - balloon.rect.x, spike.rect.y - balloon.rect.y)

            if balloon_mask.overlap(spike_mask, offset):
                print("Game Over")
                gameclose = True
                gameover = False
                collision.play()
            else:
                if not clock_started:
                    clock_started = True
                    start_time = pygame.time.get_ticks()
                else:
                    elapsed_time = (current_time - start_time) // 1000
                    score = elapsed_time
        if score > int(hiscore):
            hiscore = score
            print(hiscore)

        showscore(10, 10)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
