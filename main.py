import pygame
import sys

# pygame setup
pygame.init()
running = True

resolution = (128 * 8, 128 * 8)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

grid = [0 for _ in range(64)]

while running:
    mouse_position = pygame.mouse.get_pos()

    mouse_x = mouse_position[0]
    mouse_y = mouse_position[1]

    r_pos = (mouse_x // 128 * 128, mouse_y // 128 * 128)

    r_size = (128, 128)
    r = (r_pos, r_size)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            _x = mouse_x // 128
            _y = mouse_y // 128
            _i = (_y * 8) + _x
            grid[_i] = 1
            print(f"mouse left pressed: {_i}")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for i in range(64):
        _x = i % 8
        _y = i // 8
        _size = (128, 128)
        _color = (0, 127, 127)
        _pos = (_x * 128, _y * 128)

        if grid[i] == 0:
            pygame.draw.rect(screen, _color, (_pos, _size))
        elif grid[i] == 1:
            pygame.draw.rect(screen, (0, 255, 255), (_pos, _size))

    pygame.draw.rect(screen, (255, 255, 255), r, 4)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
