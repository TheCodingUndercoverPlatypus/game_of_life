import pygame as p
import sys
import random


width = height = 400
dimension = 10
sq_size = height // dimension
max_fps = 15


def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))

    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()




        draw_board(screen)
        clock.tick(max_fps)
        p.display.flip()

def draw_game_state(screen):
    draw_board(screen)


def draw_board(screen):
    color = 'white'
    for r in range(20):
        for c in range(20):
            l = random.randint(0,1000)
            if l == 4:
                p.draw.rect(screen, color, p.Rect(c*20, r*20, 20, 20))



if __name__ == "__main__":
    main()


main()
