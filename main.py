import pygame
import game_conts
from grid import Grid

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((game_conts.SCREEN_WIDTH, game_conts.SCREEN_HEIGHT))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
running = True
dt = 0

game_grid = Grid()

game_grid.grid[0][0] = 1
game_grid.grid[2][4] = 4
game_grid.grid[11][7] = 7




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    screen.fill(dark_blue)
    game_grid.draw(screen)
    pygame.display.update()

    dt = clock.tick(60) / 1000

pygame.quit()



