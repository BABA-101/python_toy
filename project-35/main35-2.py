# 게임 플레이어 만들기
import pygame
import sys

FPS=60
MAX_WIDTH=600
MAX_HEIGHT=400

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

class Player():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.isJump=False
        self.jumpCount=10
        
    def draw(self):
        #직사각형 그리기, 파란색 네모/x,y 좌표에 40x40 크기로 그림. 반환값은 좌표 크기
        return pygame.draw.rect(screen,(0,0,255),(self.x,self.y,40,40))
    
    # 플레이어 점프 구현
    def jump(self):
        if self.isJump:
            if self.jumpCount >=-10:
                neg=1
                if self.jumpCount < 0:
                    neg=1
                self.y=self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10
            
# player 라는 이름으로 객체 생성, x=50, y=바닥. 바닥면으로 붙이기 위해, 높이에서 자신의 y좌표만큼 빼준다.
player = Player(50,MAX_HEIGHT-40)

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    player.isJump = True
                    
        clock.tick(FPS)
        screen.fill((255,255,255))
        
        # 플레이어 그리기, 반환값은 좌표 크기
        player_rect = player.draw()
        player.jump()
        
        print(player_rect)
        
        pygame.display.update()
        
if __name__ == '__main__':
    main()