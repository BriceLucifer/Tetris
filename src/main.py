from setting import *
from sys import exit

class Main:
    def __init__(self):
        #general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        # while loop 
        while True:
            #event capture 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #display
            self.display_surface.fill(GRAY)
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()