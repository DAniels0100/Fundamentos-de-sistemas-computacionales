import pygame
import time

pygame.init()

#pantalla del juego
screen_Width=1000
screen_Height= 700
clock=pygame.time.Clock()
fps=60

screen=pygame.display.set_mode((screen_Width,screen_Height))



#variables generales del juego
game_playing=False
teams_list=['assets/Brazil_team.jpeg','assets/Argentina_team.jpeg','assets/Costa_Rica_team.jpg']
team_1= pygame.transform.scale(pygame.image.load('assets/Brazil_team.jpeg'), (200,200))
team_2= pygame.transform.scale(pygame.image.load('assets/Argentina_team.jpeg'), (200,200))
team_3= pygame.transform.scale(pygame.image.load('assets/Costa_Rica_team.jpg'), (200,200))


#pantalla inicial del juego
pantalla_Inicial=True
imagen_Inicial=pygame.image.load('assets/logo.png')
imagen_Inicial=pygame.transform.scale(imagen_Inicial,(screen_Width,screen_Height+200))

#pantalla de informacion
pantalla_Info=False


#boton info
def Button_info(x,y):
      button_info_image = pygame.transform.scale(pygame.image.load('assets/Info_button.png'), (100,100))
      button_info_rect = button_info_image.get_rect()
      button_info_widht = button_info_image.get_width()
      button_info_height = button_info_image.get_height()
      button_info_rect.x = x
      button_info_rect.y = y
      return button_info_image, button_info_rect
button_Info_Image, button_Info_Rect=Button_info(900,0)


def Button_back(x,y):
      Button_back_image = pygame.transform.scale(pygame.image.load('assets/Back_button.png'), (250,125))
      Button_back_rect = Button_back_image.get_rect()
      Button_back_widht=Button_back_image.get_width()
      Button_back_height=Button_back_image.get_height()
      Button_back_rect.x = x
      Button_back_rect.y = y
      return Button_back_image, Button_back_rect
button_Back_Image, button_Back_Rect=Button_back(375,500)


def Button_play(x,y):
      button_play_image = pygame.transform.scale(pygame.image.load('assets/Play_button.png'), (300,100))
      button_play_rect = button_play_image.get_rect()
      button_play_widht=button_play_image.get_width()
      button_play_height=button_play_image.get_height()
      button_play_rect.x = x
      button_play_rect.y = y
      return button_play_image, button_play_rect
button_Play_Image, button_Play_Rect=Button_play(350,550)


#dibujar texto en la pantalla
def draw_text(text, font, text_color, x, y):
      text = font.render(text, True, text_color)
      screen.blit(text,(x,y))



#texto de las pantallas
text_font=pygame.font.SysFont('Arial',20)


#texto de pantalla de informacion
info_text1="AUTOR: "
info_text2="Información general: Estudiante del Tecnológico de Costa Rica, 2024." 
info_text2_="Primer ingreso en la carrera \"Ingeniería en computadores\"." 
info_text3="Este proyecto se desarrolló utilizando python 3.11, apoyandose" 
info_text4="en la librería especializada para crear juegos llamada Pygame"
info_text5="Profesor: Leonardo Araya Año: 2024"
info_text6="blabla"
info_text7="blabla"


#deteccion de mouse
def Mouse():
      mouse = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse
      click = pygame.mouse.get_pressed()  # Obtiene el estado actual de los botones del mouse
      return mouse, click


#crear equipos 
def teams(x, y, image_num):

      team_Image = pygame.transform.scale(pygame.image.load(teams_list[image_num]), (200,200))
      team_Rect = team_Image.get_rect()
      team_Rect.x = x
      team_Rect.y = y
      return team_Image, team_Rect



run=True

while run:

      clock.tick(fps)

      mouse, click=Mouse()


      if pantalla_Inicial:
            screen.blit(imagen_Inicial,(0,0))
            screen.blit(button_Info_Image, button_Info_Rect)
            draw_text("Press Space to start",pygame.font.SysFont('Arial',40),(255,255,255), 350, 625) 


            if button_Info_Rect.collidepoint(mouse):
                        if click[0]:
                              pantalla_Info=True
                              screen.fill((150,150,150))
                              pantalla_Inicial=False
                              screen.blit(button_Back_Image, button_Back_Rect)


      if pantalla_Info:
            draw_text(info_text1,text_font,(0,0,0), 100, 50)
            draw_text(info_text2,text_font,(0,0,0), 100, 100)
            draw_text(info_text2_,text_font,(0,0,0), 100, 150)
            draw_text(info_text3,text_font,(0,0,0), 100, 200)
            draw_text(info_text4,text_font,(0,0,0), 100, 250)
            draw_text(info_text5,text_font,(0,0,0), 100, 300)
            draw_text(info_text6,text_font,(0,0,0), 100, 350)
            draw_text(info_text7,text_font,(0,0,0), 100, 400) 
            if button_Back_Rect.collidepoint(mouse):
                  if click[0]:
                        pantalla_Info=False
                        pantalla_Inicial=True
                        
      
      if game_playing:
            screen.fill((0,0,0))
            team_Image, team_Rect=teams(100, 150, 0)
            screen.blit(team_Image, team_Rect)
            if team_Rect.collidepoint(mouse):
                  pygame.draw.rect(screen, (255,255,0), team_Rect, 3)

            team_Image, team_Rect=teams(400,150, 1)
            screen.blit(team_Image, team_Rect)
            if team_Rect.collidepoint(mouse):
                  pygame.draw.rect(screen, (255,255,0), team_Rect, 3)

            team_Image, team_Rect=teams(700 ,150, 2)
            screen.blit(team_Image, team_Rect)
            if team_Rect.collidepoint(mouse):
                  pygame.draw.rect(screen, (255,255,0), team_Rect, 3)



      
      for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                  game_playing=True

            if event.type == pygame.QUIT:
                  run = False

      pygame.display.update()