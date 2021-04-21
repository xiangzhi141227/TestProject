import pygame
from pygame.locals import *  # 导入pygame的常量

screen_width = 800  # 设置屏幕宽度
screen_height = 260  # 设置屏幕高度

fps = 30  # 更新页面的时间


def main_game():
    score = 0  # 记录等分
    over = False
    global screen, fps_locks
    pygame.init()
    fps_locks = pygame.time.Clock()  # 刷新屏幕的时间锁
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("小恐龙")  # 设置窗体标题
    while True:
        # 判断是否单击了关闭窗口
        for event in pygame.event.get():
            if event.type == QUIT:
                over = True
                exit()  # 关闭窗体
        pygame.display.update()  # 更新整个窗口
        fps_locks.tick(fps)


if __name__ == '__main__':
    main_game()