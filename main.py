import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
from logger import log_state,log_event
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    c=pygame.time.Clock()
    dt=0
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    Asteroid.containers=(updatable,drawable,asteroids)
    AsteroidField.containers=updatable
    Shot.containers=(updatable,drawable,shots)
    p=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    af=AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            if (a.collides_with(p)):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for s in shots:
                if (a.collides_with(s)):
                    log_event("asteroid_shot")
                    a.kill()
                    s.kill()
        pygame.display.flip()
        dt=c.tick(60)/1000

if __name__ == "__main__":
    main()
