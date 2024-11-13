import pygame

# pygame setup
pygame.init()

# Tamaño de ventana
WIN_WIDTH = 1280
WIN_HEIGHT = 720
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Mensaje e icono de la ventana
pygame.display.set_caption("Pong")
ico = pygame.image.load("PongIco.png")
pygame.display.set_icon(ico)

clock = pygame.time.Clock()
running = True

# Definición de tamaño de barras de jugadores y posición inicial
STICK_WIDTH = 30
STICK_HEIGHT = 120
STICK_SPEED = 5

STICK_X = 50
STICK_Y = (WIN_HEIGHT // 2) - (STICK_HEIGHT // 2)

# Creamos jugadores
p1 = pygame.Rect(STICK_X, STICK_Y, STICK_WIDTH, STICK_HEIGHT)
p2 = pygame.Rect(WIN_WIDTH - STICK_X, STICK_Y, STICK_WIDTH, STICK_HEIGHT)

# Puntuaciones
p1_score = 0
p2_score = 0
fuente = pygame.font.Font(None, 36)

# Definición características de la pelota
BALL_RAD = 20
BALL_X = (WIN_WIDTH // 2) - (BALL_RAD // 2)
BALL_Y = (WIN_HEIGHT // 2) - (BALL_RAD // 2)
ball_speed_x = 7
ball_speed_y = 7

while running:
    # pygame.QUIT es el evento de cerrar ventana cuando se clicka en la "x"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # rellena la pantalla de un color. O se pasa una tupla o nombres
    screen.fill("black")

    # Zona de dibujo

    pygame.draw.rect(screen, "white", p1)
    pygame.draw.rect(screen, "white", p2)
    ball = pygame.draw.circle(screen, "white", (BALL_X, BALL_Y), BALL_RAD)
    middle = pygame.draw.line(screen, "grey", (WIN_WIDTH // 2 - 5, 0), (WIN_WIDTH // 2 - 5, WIN_HEIGHT), 10)

    # Lógica del juego
    keys = pygame.key.get_pressed()

    # Control jugador 1
    if keys[pygame.K_w] and p1.top > 0:
        p1.y -= STICK_SPEED
    if keys[pygame.K_s] and p1.bottom < 720:
        p1.y += STICK_SPEED

    # Control jugador 2
    if keys[pygame.K_UP] and p2.top > 0:
        p2.y -= STICK_SPEED
    if keys[pygame.K_DOWN] and p2.bottom < 720:
        p2.y += STICK_SPEED

    # Animación pelota
    if BALL_Y > (WIN_HEIGHT - 10) or BALL_Y < 10:
        ball_speed_y *= -1

    # Anotación puntos y reinicio. Cuando un jugador puntúe 10, el juego se cierra

    if BALL_X > WIN_WIDTH:
        BALL_X = (WIN_WIDTH // 2) - (BALL_RAD // 2)
        BALL_Y = (WIN_HEIGHT // 2) - (BALL_RAD // 2)
        # Si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1
        p1_score += 1
        if p1_score == 10:
            running = False

    if BALL_X < 0:
        BALL_X = (WIN_WIDTH // 2) - (BALL_RAD // 2)
        BALL_Y = (WIN_HEIGHT // 2) - (BALL_RAD // 2)
        # Si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1
        p2_score += 1
        if p2_score == 10:
            running = False

    BALL_X += ball_speed_x
    BALL_Y += ball_speed_y

    # Colisiones
    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_speed_x *= -1

    # Mostrar puntuación. El antialias es para que sea más suave
    score_text_p1 = fuente.render(f"Player 1 points: {p1_score}", True, "white")
    screen.blit(score_text_p1, (10, 10))

    score_text_p2 = fuente.render(f"Player 2 points: {p2_score}", True, "white")
    screen.blit(score_text_p2, (WIN_WIDTH - 0, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
