import pygame
import sys
pygame.init()

def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return(f"Winner is: {sign}")
    for col in range(3):
        if mas[0][col]  == sign and mas[0][col] == sign and mas[2][col] == sign:
            return(f"Winner is: {sign}")
        if mas[0][0]  == sign and mas[0][1] == sign and mas[2][2] == sign:
            return(f"Winner is: {sign}")
        if mas[0][2]  == sign and mas[1][1] == sign and mas[2][0] == sign:
            return(f"Winner is: {sign}")
        if zeroes == 0:
            return "Нічия"
        return False
                
size_block = 100
free_space = 7
width = height = (size_block * 3) + (free_space * 4)
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tac-Toe")

BLACK = (0, 0, 0)
YELLOW = (0, 204, 102)
GREEN = (255, 255, 102)
WHITE = (255, 255, 255)
query = 0
game_over = False

mas = [[0]*3 for i in range(3)]   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over: 
            x_mouse, y_mouse = pygame.mouse.get_pos() 
            col = x_mouse // (size_block + free_space)
            row = y_mouse // (size_block + free_space)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = "o"
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(BLACK)  
    for row in range(3):
        for col in range(3):
            if mas[row][col] == "x":
                color = YELLOW
            elif mas[row][col] == "o":
                color = GREEN
            else:
                color = WHITE  
            x = col * size_block + (col + 1) * free_space 
            y = row * size_block + (row + 1) * free_space  
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == YELLOW:
                pygame.draw.line(screen, WHITE, (x + 5,y + 5), (x + size_block - 5, y + size_block - 5), 3)
                pygame.draw.line(screen, WHITE, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
            elif color == GREEN:
                pygame.draw.circle(screen, WHITE, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, "x")
    else:
        game_over = check_win(mas, "o")

    if game_over:
        screen.fill(BLACK)
        font = pygame.font.SysFont("strxingkai", 80)
        text1 = font.render(game_over, True, WHITE)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])    
    pygame.display.update()