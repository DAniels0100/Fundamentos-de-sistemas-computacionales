import pygame


pygame.init()


#pantalla del juego
Screen_width=1000
Screen_height= 700
clock=pygame.time.Clock()
fps=60

Screen=pygame.display.set_mode((Screen_width,Screen_height))

run=True

while run:
      clock.tick(fps)
      for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                  run = False

      pygame.display.update()