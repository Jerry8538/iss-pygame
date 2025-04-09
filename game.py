import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

p_l = pygame.image.load("assets/images/phineas_l.png")
p_r = pygame.image.load("assets/images/phineas_r.png")
phineas_image = p_r
i_r = pygame.image.load("assets/images/isabella_r.png")
i_l = pygame.image.load("assets/images/isabella_l.png")
isabella_image = i_r

p_x = 0
p_y = 0

i_x = 0
i_y = 0

p_vx = 20
p_vy = 0

i_vx = 40
i_vy = 0

gravity = 500

p_width = phineas_image.get_width()
p_height = phineas_image.get_height()

i_width = isabella_image.get_width()
i_height = isabella_image.get_height()

clock = pygame.time.Clock()

p_rects = []
i_rects = []

score = 0

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        p_vy = -400
    if keys[pygame.K_COMMA]:
        i_vy = -400

    if keys[pygame.K_RIGHT]:
        p_x += p_vx
        phineas_image = p_r
    if keys[pygame.K_LEFT]:
        p_x -= p_vx
        phineas_image = p_l
    if keys[pygame.K_DOWN]:
        p_y += 100
    if keys[pygame.K_e]:
        i_x += i_vx
        isabella_image = i_l
    if keys[pygame.K_a]:
        i_x -= i_vx
        isabella_image = i_r
    if keys[pygame.K_o]:
        i_y += 100

    screen.fill((0, 0, 0))

    if random.randint(0, 2000) > 1900:
        p_rects.append(pygame.rect.Rect(WIDTH, random.randint(0, HEIGHT), 10, 100))
    if random.randint(0, 2000) > 1900:
        i_rects.append(pygame.rect.Rect(WIDTH, random.randint(0, HEIGHT), 10, 100))

    for rect in p_rects[:]:
        pygame.draw.rect(screen, (0, 255, 0), rect)
    for rect in i_rects[:]:
        pygame.draw.rect(screen, (255, 192, 203), rect)

    p_rect = pygame.rect.Rect(p_x, p_y, p_width, p_height)
    i_rect = pygame.rect.Rect(i_x, i_y, i_width, i_height)

    for rect in p_rects:
        if p_rect.colliderect(rect):
            p_rects.remove(rect)
            score += 1
        rect.x -= 5
    
    for rect in i_rects:
        if i_rect.colliderect(rect):
            i_rects.remove(rect)
            score += 1

        rect.x -= 5

    screen.blit(phineas_image, (p_x, p_y))
    screen.blit(isabella_image, (i_x, i_y))

    p_vy += gravity * dt
    i_vy += gravity * dt

    p_y += p_vy * dt
    i_y += i_vy * dt

    if p_y < 0:
        p_y = 0
        p_vy = 100
    if i_y < 0:
        i_y = 0
        i_vy = 100

    if p_y > HEIGHT - p_height:
        p_y = HEIGHT - p_height
        p_vy = 0
    if i_y > HEIGHT - i_height:
        i_y = HEIGHT - i_height
        i_vy = 0

    if p_x < 0:
        p_x = 0
    if i_x < 0:
        i_x = 0

    if p_x > WIDTH - p_width:
        p_x = WIDTH - p_width
    if i_x > WIDTH - i_width:
        i_x = WIDTH - i_width

    pygame.display.flip()

print(f"Your score: {score}")

pygame.quit()
