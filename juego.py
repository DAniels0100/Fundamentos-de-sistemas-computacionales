import pygame


pygame.init()

#pantalla del juego
screen_Width=1000
screen_Height= 700
clock=pygame.time.Clock()
fps=60

screen=pygame.display.set_mode((screen_Width,screen_Height))


#pantalla inicial del juego

pantalla_Inicial=False
imagen_Inicial=pygame.image.load('assets/logo.png')
imagen_Inicial=pygame.transform.scale(imagen_Inicial,(screen_Width,screen_Height))






run=True

while run:

      clock.tick(fps)

      if pantalla_Inicial:
            screen.blit(imagen_Inicial,(0,0))
            


      
      for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                  run = False

      pygame.display.update()