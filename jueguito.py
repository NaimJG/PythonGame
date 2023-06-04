import pygame;
import random;
from player import Player;
from fruits import Apple;
from fruits import Banana;
from obstacles import Bee;

pygame.init()

# Definir las dimensiones de la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 590

# Definir los colores
WHITE = (255, 255, 255)

# Inicializar la ventana de inicio
start_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Catcher")
start_bg_image = pygame.image.load("start_bg.jpg")
title_font = pygame.font.SysFont(None, 70)
start_font = pygame.font.SysFont(None, 30)
title_text = title_font.render("Fruit Catcher", True, WHITE)
start_text = start_font.render("Press SPACE to Start", True, WHITE)

scoreboard = []

# Función para mostrar la ventana de inicio
def show_start_screen():

    start_screen.blit(start_bg_image, (0, 0))
    start_screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2, SCREEN_HEIGHT/3))
    start_screen.blit(start_text, (SCREEN_WIDTH/2 - start_text.get_width()/2, SCREEN_HEIGHT/2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

# Función para leer el archivo de puntuaciones más altas
def load_high_scores():

    global scoreboard

    try:
        with open("high_scores.txt", "r") as file:
            scoreboard = []
            for line in file:
                data = line.strip().split(",")
                if len(data) == 2:
                    score = {
                        "nombre": data[0],
                        "puntuacion": int(data[1])
                    }
                    scoreboard.append(score)
    except (IOError, ValueError):
        # Si ocurre algún error, establecer puntuaciones predeterminadas
        scoreboard = []

# Función para actualizar la lista de las puntuaciones más altas
def update_high_scores(nombre, puntuacion):
    
    global scoreboard

    score = {
        "nombre": nombre,
        "puntuacion": puntuacion
    }

    scoreboard.append(score)
    scoreboard.sort(key=lambda x: x["puntuacion"], reverse=True)
    scoreboard = scoreboard[:10]

    try:
        with open("high_scores.txt", "w") as file:
            for score in scoreboard:
                line = f"{score['nombre']},{score['puntuacion']}\n"
                file.write(line)
    except IOError:
        print("Error al guardar las puntuaciones.")

# Funcion para obtener el nombre del jugador
def get_player_name():

    input_font = pygame.font.SysFont(None, 30)
    input_text = input_font.render("Enter your name and press ENTER to continue:", True, WHITE)
    screen.blit(input_text, (SCREEN_WIDTH/2 - input_text.get_width()/2, SCREEN_HEIGHT/2))
    pygame.display.flip()
    input_string = ""
    name_entered = False  # Variable para verificar si se ha ingresado un nombre válido
    while not name_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_string.strip() != "":
                        name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                else:
                    input_string += event.unicode

        screen.fill((0, 0, 0))  # Limpiar la pantalla antes de mostrar el texto actualizado
        start_screen.blit(start_bg_image, (0, 0))  # Volver a dibujar la imagen de fondo de inicio
        input_display = input_font.render(input_string, True, WHITE)
        screen.blit(input_text, (SCREEN_WIDTH/2 - input_text.get_width()/2, SCREEN_HEIGHT/2 - 30))
        screen.blit(input_display, (SCREEN_WIDTH/2 - input_display.get_width()/2, SCREEN_HEIGHT/2))
        pygame.display.flip()
        
    return input_string.strip()

# Función para reiniciar el juego
def reset_game():
    global score, lives
    score = 0
    lives = 3
    player.rect.centerx = SCREEN_WIDTH/2
    player.rect.bottom = SCREEN_HEIGHT - 10

# Función para mostrar la pantalla de Game Over
def show_game_over_screen():
    global player_name
    screen.blit(background_image, (0, 0))
    font = pygame.font.SysFont(None, 70)
    text = font.render("Game Over", True, WHITE)
    text_restart = font.render("Press R to restart", True, WHITE)
    text_menu = font.render("Press M for main menu", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, SCREEN_HEIGHT/12))
    screen.blit(text_restart, (SCREEN_WIDTH/2 - text_restart.get_width()/2, SCREEN_HEIGHT/2 + 180))
    screen.blit(text_menu, (SCREEN_WIDTH/2 - text_menu.get_width()/2, SCREEN_HEIGHT/2 + 240))
    score_font = pygame.font.SysFont(None, 30)
    score_text = score_font.render("High Scores:", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/5))
    for i, score in enumerate(scoreboard):
        score_text = score_font.render(
            f"{i+1}. {score['nombre']}: {score['puntuacion']}",
            True,
            WHITE
        )
        screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/5 + (i+1)*30))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    reset_game()
                elif event.key == pygame.K_m:
                    waiting = False
                    reset_game()
                    show_start_screen()
                    player_name = get_player_name()


pygame.display.set_caption("Fruit Catcher")
screen = pygame.display.set_mode((1000, 590))
background_image = pygame.image.load("fantasywoods.jpg")
pygame.mixer.music.load("musica2.mp3")
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound("pop.mp3")
soundWrong = pygame.mixer.Sound("wrong.mp3")

# Crea un objeto jugador
player = Player()

score = 0
lives = 3

# Crea un grupo de sprites para el jugador y el piso
player_group = pygame.sprite.Group()
player_group.add(player)

# Creamos un grupo de sprites para las manzanas
apple_group = pygame.sprite.Group()
banana_group = pygame.sprite.Group()
bee_group = pygame.sprite.Group()

# Define las fuentes de los textos
score_font = pygame.font.SysFont(None, 25)

# Mostrar la ventana de inicio y cargar la lista de puntuaciones
show_start_screen()
player_name = get_player_name()
load_high_scores()

# Bucle principal del juego
running = True
while running:
    # Maneja eventos del teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.move_up()

    # Verifica el estado del teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    if random.randrange(0, 1000) < 1:
        # Crea un objeto y lo agrega al grupo de sprites
        apple = Apple()
        apple_group.add(apple)

    if random.randrange(0, 3000) < 1:
        # Crea un objeto y lo agrega al grupo de sprites
        banana = Banana()
        banana_group.add(banana)

    if random.randrange(0, 4000) < 1:
        # Crea un objeto y lo agrega al grupo de sprites
        bee = Bee()
        bee_group.add(bee)    

    # Verifica si el jugador ha pasado un obstáculo
    for apple in apple_group:
        if player.rect.colliderect(apple.rect):
            sound.play()
            score += 1
            apple.kill()
    
    for bee in bee_group:
        if player.rect.colliderect(bee.rect):
            soundWrong.play()
            lives -= 1
            bee.kill()

    for banana in banana_group:
        if player.rect.colliderect(banana.rect):
            sound.play()
            score += 3
            banana.kill()

    if lives == 0:
        update_high_scores(player_name, score)
        show_game_over_screen()

    else:       
        # Actualiza todos los sprites
        player_group.update()
        apple_group.update()
        banana_group.update()
        bee_group.update()

        # Limpia la pantalla
        screen.blit(background_image, (0, 0))

        # Score Board
        text = score_font.render("Score: " + str(score), True, WHITE)
        screen.blit(text, (50, 50))

        # Lives Board
        text = score_font.render("Lives: " + str(lives), True, WHITE)
        screen.blit(text, (50, 80))

        # Dibuja todos los sprites
        player_group.draw(screen)
        apple_group.draw(screen)
        banana_group.draw(screen)
        bee_group.draw(screen)

        # Actualiza la pantalla
        pygame.display.flip()

# Sale de pygame
pygame.quit()