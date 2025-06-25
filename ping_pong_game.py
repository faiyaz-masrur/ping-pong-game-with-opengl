import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED = 5
PADDLE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the game window
window = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Ping Pong")

# Set up OpenGL
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Game variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice((1, -1)) * BALL_SPEED
ball_dy = random.choice((1, -1)) * BALL_SPEED

paddle1_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_y = (HEIGHT - PADDLE_HEIGHT) // 2

score1 = 0
score2 = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[K_s] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[K_UP] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED
    if keys[K_DOWN] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions with walls
    if ball_y > HEIGHT - BALL_RADIUS or ball_y < BALL_RADIUS:
        ball_dy = -ball_dy

    # Ball collisions with paddles
    if ball_x <= PADDLE_WIDTH + BALL_RADIUS and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx
    elif ball_x >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx
    elif ball_x < 0:
        # Player 2 scores
        score2 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = random.choice((1, -1)) * BALL_SPEED
        ball_dy = random.choice((1, -1)) * BALL_SPEED

    elif ball_x > WIDTH:
        # Player 1 scores
        score1 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = random.choice((1, -1)) * BALL_SPEED
        ball_dy = random.choice((1, -1)) * BALL_SPEED

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw paddles and ball
    glColor3fv(GREEN)
    glBegin(GL_QUADS)
    glVertex2f(0, paddle1_y)
    glVertex2f(PADDLE_WIDTH, paddle1_y)
    glVertex2f(PADDLE_WIDTH, paddle1_y + PADDLE_HEIGHT)
    glVertex2f(0, paddle1_y + PADDLE_HEIGHT)

    glVertex2f(WIDTH - PADDLE_WIDTH, paddle2_y)
    glVertex2f(WIDTH, paddle2_y)
    glVertex2f(WIDTH, paddle2_y + PADDLE_HEIGHT)
    glVertex2f(WIDTH - PADDLE_WIDTH, paddle2_y + PADDLE_HEIGHT)

    glEnd()

    glColor3fv(WHITE)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        x = ball_x + BALL_RADIUS * cos(i)
        y = ball_y + BALL_RADIUS * sin(i)
        glVertex2f(x, y)
    glEnd()

    # Draw the score
    font = pygame.font.Font(None, 36)
    score_display = font.render(f"{score1} - {score2}", True, WHITE)
    pygame.draw.rect(window, (0, 0, 0), (WIDTH // 2 - 50, 10, 100, 40))
    window.blit(score_display, (WIDTH // 2 - 35, 20))

    pygame.display.flip()

# Quit the game
pygame.quit()
