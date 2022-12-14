# pygame 라이브러리 통해 게임 화면 구성. 
import pygame
import sys

FPS = 60 # 초당 프레임. Frame Per Second
MAX_WIDTH=600
MAX_HEIGHT=400

pygame.init()
# Clock(): 1초당 프레임 조절
clock=pygame.time.Clock()
#게임화면 사이즈
screen=pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print("space")
        clock.tick(FPS)
        screen.fill((255,255,255))
        
        #update(): 화면 일부를 업데이트. 인자 없으면 화면 전체 업데이트
        pygame.display.update()
                    
if __name__=="__main__":
    main()