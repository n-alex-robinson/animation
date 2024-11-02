import pygame
import random

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bouncing DVD logo")
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((230, 190, 255))
    
    dvd_image = pygame.image.load("dvd.png")
    dvd = dvd_image.get_rect()
    dvd.topleft = (400, 100) 
    
    speed_x = 5
    speed_y = 5
    
    # main loop
    clock = pygame.time.Clock()
    keepGoing = True
    
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        dvd.x += speed_x
        dvd.y += speed_y

        # dvd x collision
        if dvd.left <= 0 or dvd.right >= screen.get_width():
            speed_x = -speed_x
            speed_y += random.randint(-2, 2)
            

        # dvd y collision
        if dvd.top <= 0 or dvd.bottom >= screen.get_height():
            speed_y = -speed_y
            speed_x += random.randint(-1, 1)

        # speed limits
        speed_x = max(-10, min(10, speed_x))
        speed_y = max(-10, min(10, speed_y))
        
        # screen refresh
        screen.blit(background, (0, 0))
        screen.blit(dvd_image, dvd)
        pygame.display.flip()
    
    pygame.quit()

main()