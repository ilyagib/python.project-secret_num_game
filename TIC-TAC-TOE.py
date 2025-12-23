

import random
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 50, 50), (50, 50, 255)
FONT = pygame.font.SysFont(None, 200)
MSG_FONT = pygame.font.SysFont(None, 80)


board = [["", "", ""], ["", "", ""], ["", "", ""]]
cell_size = WIDTH // 3
current_player = "X"
game_over = False
winner = None
waiting_for_computer = False
turn_start_time = 0


def check_winner(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != "": return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != "": return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != "": return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != "": return b[0][2]
    return None


def is_tie(b):
    return all(cell != "" for row in b for cell in row)


def computer_turn(b):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if b[r][c] == ""]


    for r, c in empty_cells:
        b[r][c] = "o"
        if check_winner(b) == "o":
            return
        b[r][c] = ""


    for r, c in empty_cells:
        b[r][c] = "X"
        if check_winner(b) == "X":
            b[r][c] = "o"
            return
        b[r][c] = ""


    if empty_cells:
        r, c = random.choice(empty_cells)
        b[r][c] = "o"


def reset_game():
    global board, current_player, game_over, winner, waiting_for_computer
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = "X"
    game_over = False
    winner = None
    waiting_for_computer = False


run = True
while run:
    screen.fill(WHITE)
    current_time = pygame.time.get_ticks()


    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (cell_size * i, 0), (cell_size * i, HEIGHT), 8)
        pygame.draw.line(screen, BLACK, (0, cell_size * i), (WIDTH, cell_size * i), 8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()


        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_player == "X":
            x, y = event.pos
            row, col = y // cell_size, x // cell_size
            if board[row][col] == "":
                board[row][col] = "X"
                winner = check_winner(board)
                if winner or is_tie(board):
                    game_over = True
                else:
                    current_player = "o"
                    waiting_for_computer = True
                    turn_start_time = current_time


    if not game_over and current_player == "o" and waiting_for_computer:
        if current_time - turn_start_time >= 800:
            computer_turn(board)
            winner = check_winner(board)
            if winner or is_tie(board):
                game_over = True
            current_player = "X"
            waiting_for_computer = False


    for r in range(3):
        for c in range(3):
            if board[r][c] != "":
                color = BLACK if board[r][c] == "X" else BLUE
                text = FONT.render(board[r][c].upper(), True, color)
                screen.blit(text, (c * cell_size + (cell_size - text.get_width()) // 2,
                                   r * cell_size + (cell_size - text.get_height()) // 2))


    if game_over:
        msg = f"{winner.upper()} Wins!" if winner else "It's a Tie!"
        sub_msg = "Press 'R' to Restart"

        txt_surf = MSG_FONT.render(msg, True, RED)
        sub_surf = pygame.font.SysFont(None, 40).render(sub_msg, True, BLACK)

        # Display Box
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 200, HEIGHT // 2 - 60, 400, 120))
        pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 200, HEIGHT // 2 - 60, 400, 120), 3)

        screen.blit(txt_surf, (WIDTH // 2 - txt_surf.get_width() // 2, HEIGHT // 2 - 45))
        screen.blit(sub_surf, (WIDTH // 2 - sub_surf.get_width() // 2, HEIGHT // 2 + 25))

    pygame.display.flip()

pygame.quit()


