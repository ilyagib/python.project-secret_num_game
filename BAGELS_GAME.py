import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bagels - Pygame Edition")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
GRAY = (200, 200, 200)

FONT_SIZE_TITLE = 72
FONT_SIZE_GUESS = 48
FONT_SIZE_HISTORY = 36
FONT_TITLE = pygame.font.Font(None, FONT_SIZE_TITLE)
FONT_GUESS = pygame.font.Font(None, FONT_SIZE_GUESS)
FONT_HISTORY = pygame.font.Font(None, FONT_SIZE_HISTORY)

MAX_TRIES = 10
NUM_DIGITS = 3


def generate_secret_number():
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return "".join(digits[:NUM_DIGITS])


def get_clues(guess, secret_num):
    if guess == secret_num:
        return ["You Won!"]

    clues = []

    for i in range(NUM_DIGITS):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return ["Bagels"]

    clues.sort()
    return clues


def reset_game():
    return {
        'secret_num': generate_secret_number(),
        'guesses_left': MAX_TRIES,
        'history': [],
        'current_input': "",
        'game_over': False,
        'win': False
    }


def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, rect)


def draw_game_state(state):
    SCREEN.fill(BLACK)

    draw_text(SCREEN, "B A G E L S", FONT_TITLE, WHITE, SCREEN_WIDTH // 2, 50)

    input_box_rect = pygame.Rect(SCREEN_WIDTH // 4, 150, SCREEN_WIDTH // 2, 60)
    pygame.draw.rect(SCREEN, GRAY, input_box_rect)
    pygame.draw.rect(SCREEN, WHITE, input_box_rect, 3)

    draw_text(
        SCREEN,
        state['current_input'],
        FONT_GUESS,
        BLACK,
        SCREEN_WIDTH // 2,
        150 + 30
    )

    draw_text(
        SCREEN,
        f"Tries Left: {state['guesses_left']}",
        FONT_HISTORY,
        WHITE,
        SCREEN_WIDTH // 2,
        230
    )

    history_y_start = 280
    for i, (guess, clues) in enumerate(state['history']):
        clue_text = " ".join(clues)
        y_pos = history_y_start + i * 35

        draw_text(SCREEN, guess, FONT_HISTORY, BLUE, SCREEN_WIDTH // 4, y_pos)

        clue_color = GREEN if "You Won!" in clues else RED if "Bagels" in clues else WHITE
        draw_text(SCREEN, clue_text, FONT_HISTORY, clue_color, 3 * SCREEN_WIDTH // 4, y_pos)

    if state['game_over']:
        message_color = GREEN if state['win'] else RED
        message = "You WON!" if state['win'] else f"You LOST! The number was {state['secret_num']}"
        draw_text(SCREEN, message, FONT_GUESS, message_color, SCREEN_WIDTH // 2, 500)
        draw_text(SCREEN, "Press SPACE to Play Again", FONT_HISTORY, GRAY, SCREEN_WIDTH // 2, 550)

    pygame.display.flip()


game_state = reset_game()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_state['game_over']:
            if event.type == pygame.KEYDOWN:
                key = event.key

                if pygame.K_0 <= key <= pygame.K_9:
                    digit = str(key - pygame.K_0)
                    if len(game_state['current_input']) < NUM_DIGITS:
                        game_state['current_input'] += digit

                elif key == pygame.K_BACKSPACE:
                    game_state['current_input'] = game_state['current_input'][:-1]

                elif key == pygame.K_RETURN:
                    guess = game_state['current_input']
                    if len(guess) == NUM_DIGITS:
                        secret_num = game_state['secret_num']
                        clues = get_clues(guess, secret_num)

                        game_state['history'].append((guess, clues))
                        game_state['current_input'] = ""
                        game_state['guesses_left'] -= 1

                        if "You Won!" in clues:
                            game_state['game_over'] = True
                            game_state['win'] = True
                        elif game_state['guesses_left'] == 0:
                            game_state['game_over'] = True
                            game_state['win'] = False

        elif game_state['game_over']:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = reset_game()

    draw_game_state(game_state)

pygame.quit()
sys.exit()