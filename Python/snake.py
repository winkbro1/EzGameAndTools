import pygame,sys
import random
import time
 
caption_width = 300 
caption_height = 300
white_color = (255, 255, 255)
black_color = (0, 0, 0)
game_title = '贪吃蛇'
cell = 10 
snake_init_pos = [[150,150], [140,150], [130,150], [120,150]] # 蛇的初始位置
food_pos = [random.randrange(1, 30) * 10, random.randrange(1, 30) * 10] # 食物初始随机位置
head_pos = [150, 150]
 
pygame.init()
clock = pygame.time.Clock()
 
caption = pygame.display.set_mode((caption_width, caption_height))
pygame.display.set_caption(game_title)
 
def draw_rect(color, position):
    pygame.draw.rect(caption, color, pygame.Rect(position[0], position[1], cell, cell))
 
def hit_the_self():
    if snake_init_pos[0] in snake_init_pos[1:]:
        return True 
    else:
        return False
 
def hit_the_wall(head_pos):
    if head_pos[0] >= caption_width or head_pos[0]<0 or head_pos[1] >= caption_height or head_pos[1] < 0:
        return True
    else:
        return False
 
def change_direction(head_pos):
    global food_pos
    snake_init_pos.insert(0, list(head_pos))
 
    if head_pos != food_pos:
        snake_init_pos.pop()
    else:
        food_pos = [random.randrange(1, 30) * 10, random.randrange(1, 30) * 10]
 
    if hit_the_self() or hit_the_wall(head_pos):
        pygame.quit()
 
 
def main():
    for pos in snake_init_pos:
        draw_rect(white_color, pos)
 
    draw_rect(white_color, food_pos)
    pygame.display.update()
 
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    head_pos[0] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_RIGHT:
                    head_pos[0] += cell
                    change_direction(head_pos)
                    for i in range(10):
                        time.sleep(0.5)
                        head_pos[0] += cell
                        change_direction(head_pos)
                elif event.key == pygame.K_UP:
                    head_pos[1] -= cell
                    change_direction(head_pos)
                elif event.key == pygame.K_DOWN:
                    head_pos[1] += cell
                    change_direction(head_pos)
 
        caption.fill(black_color)
        draw_rect(white_color, food_pos)
 
        for pos in snake_init_pos:
            draw_rect(white_color, pos)
 
        pygame.display.update()
        clock.tick(10)
 
 
 
if __name__ == '__main__':
    main()
