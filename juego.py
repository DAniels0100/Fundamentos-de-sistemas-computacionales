import pygame
import time
import serial
from random import randint
pygame.init()

#pantalla del juego
screen_Width=1000
screen_Height= 700
clock=pygame.time.Clock()
fps=60

screen=pygame.display.set_mode((screen_Width,screen_Height))

#coneccion serial con la raspberry
Rpi=serial.Serial(port="COM4", baudrate=115200)

try:
    Rpi.open()
except:
    if (Rpi.isOpen()):
        print("conectado")
    else:
        print('no conecto')



#variables generales del juego
game_Playing=False
teams_Shields=['assets/escudoBrasil.jpg', 'assets/escudoArgentina.jpg', 'assets/escudoCostaRica.jpg']
teams_List=['assets/Brasil_team.jpeg','assets/Argentina_team.jpeg','assets/Costa_Rica_team.jpg']
player_List=['assets/jugadorBrasil1.jpg','assets/jugadorBrasil2.jpg','assets/jugadorBrasil3.jpg','assets/porteroBrasil1.jpg', 'assets/porteroBrasil2.jpg', 'assets/porteroBrasil3.jpg',
            'assets/jugadorArgentina1.jpg','assets/jugadorArgentina2.jpg', 'assets/jugadorArgentina3.jpg','assets/porteroArgentina1.jpg', 'assets/porteroArgentina2.jpg', 'assets/porteroArgentina3.jpg',
            'assets/jugadorCR1.jpg','assets/jugadorCR2.jpg','assets/jugadorCR3.jpg', 'assets/porteroCR1.jpg','assets/porteroCR2.jpg','assets/porteroCR3.jpg']
match_players1=[]
match_goalkeepers1=[]
match_players2=[]
match_goalkeepers2=[]
match_players3=[]
match_goalkeepers3=[]
moneda_List=['assets/moneda.jpg', 'assets/monedadelante.png', 'assets/monedadetras.png']

#pantalla inicial del juego
pantalla_Inicial=True
imagen_Inicial=pygame.transform.scale(pygame.image.load('assets/logo.png'),(screen_Width,screen_Height+200))

#fondo pantalla de partido
imagen_Fondo=pygame.transform.scale(pygame.image.load('assets/estadio.jpg'),(screen_Width,screen_Height+200))

#pantallas
pantalla_Info=False
pantalla_Seleccion=False
pantalla_Moneda=False
monedaLanzada=0
brasil_Team=False
argentina_Team=False
costarica_Team=False
pantalla_Penales=False

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
info_text1="AUTORES: Sergio Alvarez, Anthony"
info_text2="Información general: Estudiantes del Tecnológico de Costa Rica, 2024." 
info_text2_="Primer ingreso en la carrera \"Ingeniería en computadores\"." 
info_text3="Este proyecto se desarrolló utilizando python 3.11, apoyandose" 
info_text4="en la librería especializada para crear juegos llamada Pygame"
info_text5="Profesor: Leonardo Araya Año: 2024"



#deteccion de mouse
def Mouse():
      mouse = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse
      click = pygame.mouse.get_pressed()  # Obtiene el estado actual de los botones del mouse
      return mouse, click


#crear equipos 
def teams(x, y, image_index):

      team_Image = pygame.transform.scale(pygame.image.load(teams_Shields[image_index]), (200,200))
      team_Rect = team_Image.get_rect()
      team_Rect.x = x
      team_Rect.y = y
      return team_Image, team_Rect


def player(x, y,lista, image_index):
      player_Image = pygame.transform.scale(pygame.image.load(lista[image_index]), (200,200))
      player_Rect = player_Image.get_rect()
      player_Rect.x = x
      player_Rect.y = y
      return player_Image, player_Rect


def anotaciones(x, y, valor):
      # fallo=pygame.draw.rect(screen, (255,0,0), (110,110,x,y))
      # anotacion=pygame.draw.rect(screen, (0,255,0), (110,110,x,y))
      print(valor[0])
      if valor[0]=='A' or valor=='B' or valor=='C' or valor=='D' or valor=='E' or valor=='F':
            fallo=pygame.draw.rect(screen, (255,0,0), (110,110,x,y))
            #print(valor[0])
      # else:
      #       anotacion=pygame.draw.rect(screen, (0,255,0), (110,110,x,y))

run=True

while run:
      

      if (Rpi.isOpen()):
            datos=Rpi.readline()
            decode=datos.decode('UTF-8')
            # print(decode[0])
            
            clock.tick(fps)

            mouse, click=Mouse()


            if pantalla_Inicial:
                  brasil_Team=False
                  argentina_Team=False
                  costarica_Team=False
                  game_Playing=False
                  screen.blit(imagen_Inicial,(0,0))
                  screen.blit(button_Info_Image, button_Info_Rect)
                  selection=pygame.draw.rect(screen, (55,55,55), (10,525,350,100))
                  draw_text("Team selection",pygame.font.SysFont('Algerian',40),(255,255,255), 20, 550)
                  play=pygame.draw.rect(screen, (55,55,55), (610,525,350,100))
                  draw_text("Play",pygame.font.SysFont('Algerian',70),(255,255,255), 700, 535)
                  draw_text("Press Space to start",pygame.font.SysFont('Algerian',40),(255,255,255), 275, 625) 


                  if button_Info_Rect.collidepoint(mouse):
                              if click[0]:
                                    pantalla_Info=True
                                    screen.fill((150,150,150))
                                    pantalla_Inicial=False
                                    screen.blit(button_Back_Image, button_Back_Rect)

                  if selection.collidepoint(mouse):
                              if click[0]:
                                    pantalla_Seleccion=True
                                    screen.fill((0,0,0))
                                    pantalla_Inicial=False
                                    screen.blit(button_Back_Image, button_Back_Rect)
                  if play.collidepoint(mouse):
                              if click[0]:
                                    game_Playing=True
                                    screen.fill((0,0,0))
                                    pantalla_Inicial=False

                  


            if pantalla_Info:
                  draw_text(info_text1,text_font,(0,0,0), 100, 50)
                  draw_text(info_text2,text_font,(0,0,0), 100, 100)
                  draw_text(info_text2_,text_font,(0,0,0), 100, 150)
                  draw_text(info_text3,text_font,(0,0,0), 100, 200)
                  draw_text(info_text4,text_font,(0,0,0), 100, 250)
                  draw_text(info_text5,text_font,(0,0,0), 100, 300)
                  if button_Back_Rect.collidepoint(mouse):
                        if click[0]:
                              pantalla_Info=False
                              pantalla_Inicial=True
                              
            if decode[0]=="#":
                        decode_potenciometro=int(decode[1:])


            if pantalla_Seleccion:
                  
                  screen.fill((0,0,0))
                  team_Image, team1_Rect=teams(100, 150, 0)
                  screen.blit(team_Image, team1_Rect)
                  team_Image, team2_Rect=teams(400,150, 1)
                  screen.blit(team_Image, team2_Rect)
                  team_Image, team3_Rect=teams(700 ,150, 2)
                  screen.blit(team_Image, team3_Rect) 
                  if decode_potenciometro<=5:
                        pygame.draw.rect(screen, (255,255,0), team1_Rect, 8)

                  if decode_potenciometro>5 and decode_potenciometro<=10:
                        pygame.draw.rect(screen, (255,255,0), team2_Rect, 8)

                  if decode_potenciometro>10:
                        pygame.draw.rect(screen, (255,255,0), team3_Rect, 8)

                  if decode[0]=="G":
                        if decode_potenciometro<=5:
                              brasil_Team=True
                              pantalla_Seleccion=False
                        if decode_potenciometro>5 and decode_potenciometro<=10:
                              argentina_Team=True
                              pantalla_Seleccion=False
                        if decode_potenciometro>10:
                              costarica_Team=True
                              pantalla_Seleccion=False



            if brasil_Team:
                  screen.fill((155,155,30))
                  draw_text(f"Jugadores seleccionados:{len(match_players1)//2+len(match_goalkeepers1)//2}",pygame.font.SysFont('Algerian',30),(0,0,0), 175, 25)
                  draw_text("Presionar \"T\" para escoger otro equipo",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 650)
                  playerBrasil1_Image, playerBrasil1_Rect=player(100, 100,player_List, 0)
                  playerBrasil2_Image, playerBrasil2_Rect=player(425, 100,player_List, 1)
                  playerBrasil3_Image, playerBrasil3_Rect=player(700, 100,player_List, 2)
                  porteroBrasil1_Imagen, porteroBrasil1_Rect=player(100, 400,player_List, 3)
                  porteroBrasil2_Imagen, porteroBrasil2_Rect=player(425, 400,player_List, 4)
                  porteroBrasil3_Imagen, porteroBrasil3_Rect=player(700, 400,player_List, 5)
                  screen.blit(playerBrasil1_Image, playerBrasil1_Rect)
                  screen.blit(playerBrasil2_Image, playerBrasil2_Rect)
                  screen.blit(playerBrasil3_Image, playerBrasil3_Rect)
                  screen.blit(porteroBrasil1_Imagen, porteroBrasil1_Rect)
                  screen.blit(porteroBrasil2_Imagen, porteroBrasil2_Rect)
                  screen.blit(porteroBrasil3_Imagen, porteroBrasil3_Rect)

                  if decode_potenciometro<=2:
                        pygame.draw.rect(screen, (255,255,0), playerBrasil1_Rect, 8)
                        draw_text("Neymar",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 300)
                        if decode[0]=="G":
                              
                              match_players1.append(playerBrasil1_Image)
                              match_players1.append((100,100))

                             
                              if len(match_players1)>2:
                                    match_players1=match_players1[1:3:-1]
                              

                  if decode_potenciometro>2 and decode_potenciometro<=5:
                        pygame.draw.rect(screen, (255,255,0), playerBrasil2_Rect, 8)
                        draw_text("Ronaldinho",pygame.font.SysFont('Algerian',30),(0,0,0), 425, 300)
                        if decode[0]=="G":
                              
                              match_players1.append(playerBrasil2_Image)
                              match_players1.append((100,100))

                              
                              if len(match_players1)>2:
                                    match_players1=match_players1[1:3:-1]
                              

                  if decode_potenciometro>5 and decode_potenciometro<=7:
                        pygame.draw.rect(screen, (255,255,0), playerBrasil3_Rect, 8)
                        draw_text("Fabricio",pygame.font.SysFont('Algerian',30),(0,0,0), 700, 300)
                        if decode[0]=="G":
                              
                              match_players1.append(playerBrasil3_Image)
                              match_players1.append((100,100))


                              if len(match_players1)>2:
                                    match_players1=match_players1[1:3:-1]
                              

                  if decode_potenciometro>7 and decode_potenciometro<=10:
                        pygame.draw.rect(screen, (255,255,0), porteroBrasil1_Rect, 8)
                        draw_text("Alisson",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers1.append(porteroBrasil1_Imagen)
                              match_goalkeepers1.append((100,400))

                              if len(match_goalkeepers1)>2:
                                    match_goalkeepers1=match_goalkeepers1[1:3:-1]
                              

                  if decode_potenciometro>10 and decode_potenciometro<=12:
                        pygame.draw.rect(screen, (255,255,0), porteroBrasil2_Rect, 8)
                        draw_text("Edderson",pygame.font.SysFont('Algerian',30),(0,0,0), 425, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers1.append(porteroBrasil2_Imagen)
                              match_goalkeepers1.append((100,400))


                              if len(match_goalkeepers1)>2:
                                    match_goalkeepers1=match_goalkeepers1[1:3:-1]
                              

                  if decode_potenciometro>12 and decode_potenciometro<=15:
                        pygame.draw.rect(screen, (255,255,0), porteroBrasil3_Rect, 8)
                        draw_text("Taffarel",pygame.font.SysFont('Algerian',30),(0,0,0), 700, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers1.append(porteroBrasil2_Imagen)
                              match_goalkeepers1.append((100,400))

                              if len(match_goalkeepers1)>2:
                                    match_goalkeepers1=match_goalkeepers1[1:3:-1]
                              
                  
                        if decode_potenciometro<=5:
                              brasil_Team=True
                        if decode_potenciometro>5 and decode_potenciometro<=10:
                              argentina_Team=True
                        if decode_potenciometro>10:
                              costarica_Team=True


            if argentina_Team:
                  screen.fill((100,155,250))
                  draw_text(f"Jugadores seleccionados:{len(match_players2)//2+len(match_goalkeepers2)//2}",pygame.font.SysFont('Algerian',30),(0,0,0), 175, 25)
                  draw_text("Presionar \"T\" para escoger otro equipo",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 650)
                  playerArgentina1_Image, playerArgentina1_Rect=player(100, 100,player_List, 6)
                  playerArgentina2_Image, playerArgentina2_Rect=player(425, 100,player_List, 7)
                  playerArgentina3_Image, playerArgentina3_Rect=player(700, 100,player_List, 8)
                  porteroArgentina1_Imagen, porteroArgentina1_Rect=player(100, 400,player_List, 9)
                  porteroArgentina2_Imagen, porteroArgentina2_Rect=player(425, 400,player_List, 10)
                  porteroArgentina3_Imagen, porteroArgentina3_Rect=player(700, 400,player_List, 11)
                  screen.blit(playerArgentina1_Image, playerArgentina1_Rect)
                  screen.blit(playerArgentina2_Image, playerArgentina2_Rect)
                  screen.blit(playerArgentina3_Image, playerArgentina3_Rect)
                  screen.blit(porteroArgentina1_Imagen, porteroArgentina1_Rect)
                  screen.blit(porteroArgentina2_Imagen, porteroArgentina2_Rect)
                  screen.blit(porteroArgentina3_Imagen, porteroArgentina3_Rect)
                  if decode_potenciometro<=2:
                        pygame.draw.rect(screen, (255,255,0), playerArgentina1_Rect, 8)
                        draw_text("Messi",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 300)
                        if decode[0]=="G":
                              
                              match_players2.append(playerArgentina1_Image)
                              match_players2.append((600,100))

                              
                              if len(match_players2)>2:
                                    match_players2=match_players2[1:3:-1]
                              

                  if decode_potenciometro>2 and decode_potenciometro<=5:
                        pygame.draw.rect(screen, (255,255,0), playerArgentina2_Rect, 8)
                        draw_text("Dimaria",pygame.font.SysFont('Algerian',30),(0,0,0), 425, 300)
                        if decode[0]=="G":
                              
                              match_players2.append(playerArgentina2_Image)
                              match_players2.append((600,100))

                              if len(match_players2)>2:
                                    match_players2=match_players2[1:3:-1]
                              

                  if decode_potenciometro>5 and decode_potenciometro<=7:
                        pygame.draw.rect(screen, (255,255,0), playerArgentina3_Rect, 8)
                        draw_text("Kun Aguero",pygame.font.SysFont('Algerian',30),(0,0,0), 700, 300)
                        if decode[0]=="G":
                              
                              match_players2.append(playerArgentina3_Image)
                              match_players2.append((600,100))

                              if len(match_players2)>2:
                                    match_players2=match_players2[1:3:-1]
                              

                  if decode_potenciometro>7 and decode_potenciometro<=10:
                        pygame.draw.rect(screen, (255,255,0), porteroArgentina1_Rect, 8)
                        draw_text("Dibu",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers2.append(porteroArgentina1_Imagen)
                              match_goalkeepers2.append((600,400))

                              
                              if len(match_goalkeepers2)>2:
                                    match_goalkeepers2=match_goalkeepers2[1:3:-1]
                              

                  if decode_potenciometro>10 and decode_potenciometro<=12:
                        pygame.draw.rect(screen, (255,255,0), porteroArgentina2_Rect, 8)
                        draw_text("Marchesin",pygame.font.SysFont('Algerian',30),(0,0,0), 425, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers2.append(porteroArgentina2_Imagen)
                              match_goalkeepers2.append((600,400))


                              if len(match_goalkeepers2)>2:
                                    match_goalkeepers2=match_goalkeepers2[1:3:-1]
                              

                  if decode_potenciometro>12 and decode_potenciometro<=15:
                        pygame.draw.rect(screen, (255,255,0), porteroArgentina3_Rect, 8)
                        draw_text("Rulli",pygame.font.SysFont('Algerian',30),(0,0,0), 700, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers2.append(porteroArgentina3_Imagen)
                              match_goalkeepers2.append((600,400))

                              if len(match_goalkeepers2)>2:
                                    match_goalkeepers2=match_goalkeepers2[1:3:-1]
                              

            if costarica_Team:
                  screen.fill((250,105,100))
                  draw_text(f"Jugadores seleccionados:{len(match_players3)//2+len(match_goalkeepers3)//2}",pygame.font.SysFont('Algerian',30),(0,0,0), 175, 25)
                  draw_text("Presionar \"T\" para escoger otro equipo",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 650)
                  playerCR1_Image, playerCR1_Rect=player(100, 100,player_List, 12)
                  playerCR2_Image, playerCR2_Rect=player(425, 100,player_List, 13)
                  playerCR3_Image, playerCR3_Rect=player(700, 100,player_List, 14)
                  porteroCR1_Imagen, porteroCR1_Rect=player(100, 400,player_List, 15)
                  porteroCR2_Imagen, porteroCR2_Rect=player(425, 400,player_List, 16)
                  porteroCR3_Imagen, porteroCR3_Rect=player(700, 400,player_List, 17)
                  screen.blit(playerCR1_Image, playerCR1_Rect)
                  screen.blit(playerCR2_Image, playerCR2_Rect)
                  screen.blit(playerCR3_Image, playerCR3_Rect)
                  screen.blit(porteroCR1_Imagen, porteroCR1_Rect)
                  screen.blit(porteroCR2_Imagen, porteroCR2_Rect)
                  screen.blit(porteroCR3_Imagen, porteroCR3_Rect)
                  if decode_potenciometro<=2:
                        pygame.draw.rect(screen, (255,255,0), playerCR1_Rect, 8)
                        draw_text("Brayan",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 300)
                        if decode[0]=="G":
                              
                              match_players2.append(playerCR1_Image)
                              match_players2.append((100,100))

                              
                              if len(match_players2)>2:
                                    match_players2=match_players2[1:3:-1]
                  if decode_potenciometro>2 and decode_potenciometro<=5:
                        pygame.draw.rect(screen, (255,255,0), playerCR2_Rect, 8)
                        draw_text("Celso",pygame.font.SysFont('Algerian',30),(0,0,0), 425, 300)
                        if decode[0]=="G":
                              
                              match_players3.append(playerCR2_Image)
                              match_players3.append((100,100))

                              
                              if len(match_players3)>2:
                                    match_players3=match_players3[1:3:-1]

                  if decode_potenciometro>5 and decode_potenciometro<=7:
                        pygame.draw.rect(screen, (255,255,0), playerCR3_Rect, 8)
                        draw_text("Cambell",pygame.font.SysFont('Algerian',30),(0,0,0), 700, 300)
                        if decode[0]=="G":
                              
                              match_players3.append(playerCR3_Image)
                              match_players3.append((100,100))

                              
                              if len(match_players3)>2:
                                    match_players3=match_players3[1:3:-1]

                  if decode_potenciometro>7 and decode_potenciometro<=10:
                        pygame.draw.rect(screen, (255,255,0), porteroCR1_Rect, 8)
                        draw_text("Keylor",pygame.font.SysFont('Algerian',30),(0,0,0), 100, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers3.append(porteroCR1_Imagen)
                              match_goalkeepers3.append((100,400))

                              
                              if len(match_goalkeepers3)>2:
                                    match_goalkeepers3=match_goalkeepers3[1:3:-1]

                  if decode_potenciometro>10 and decode_potenciometro<=12:
                        pygame.draw.rect(screen, (255,255,0), porteroCR2_Rect, 8)
                        draw_text("Moreira",pygame.font.SysFont('Algerian',30),(0,0,0), 425, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers3.append(porteroCR2_Imagen)
                              match_goalkeepers3.append((100,400))

                              
                              if len(match_goalkeepers3)>2:
                                    match_goalkeepers3=match_goalkeepers3[1:3:-1]

                  if decode_potenciometro>12 and decode_potenciometro<=15:
                        pygame.draw.rect(screen, (255,255,0), porteroCR3_Rect, 8)
                        draw_text("Alvarado",pygame.font.SysFont('Algerian',30),(0,0,0), 700, 600)
                        if decode[0]=="G":
                              
                              match_goalkeepers3.append(porteroCR3_Imagen)
                              match_goalkeepers3.append((100,400))

                              
                              if len(match_goalkeepers3)>2:
                                    match_goalkeepers3=match_goalkeepers3[1:3:-1]
                               
                              
            if game_Playing:
                  pantalla_Moneda=True
                  if pantalla_Moneda==True and monedaLanzada<4:
                        screen.blit(imagen_Fondo, (0,0))
                        moneda_Imagen, moneda_Rect = player(100,100, moneda_List, 0)
                        screen.blit(moneda_Imagen,moneda_Rect)
                        lanzar=pygame.draw.rect(screen, (55,55,55), (10,525,350,100))
                        draw_text("lanzar moneda",pygame.font.SysFont('Algerian',40),(255,255,255), 20, 550)
                        random=2
                        if lanzar.collidepoint(mouse):
                              if click[0]:
                                    monedaLanzada+=1
                                    random=randint(0,1)
                                    pantalla_Penales=True
                        if random==0:
                              moneda1_Imagen, moneda1_Rect = player(500,100, moneda_List, 1)
                              screen.blit(moneda1_Imagen, moneda1_Rect)
                              cuadro=pygame.draw.rect(screen, (55,55,55), (410,525,350,100))
                              draw_text("equipo 1 local",pygame.font.SysFont('Algerian',40),(255,255,255), 420, 550)
                        elif random==1:
                              moneda2_Imagen, moneda2_Rect = player(500,100, moneda_List, 2)
                              screen.blit(moneda2_Imagen, moneda2_Rect)
                              draw_text("lanzar moneda",pygame.font.SysFont('Algerian',40),(255,255,255), 20, 550)
                              cuadro=pygame.draw.rect(screen, (55,55,55), (410,525,350,100))
                              draw_text("equipo 2 local",pygame.font.SysFont('Algerian',40),(255,255,255), 420, 550)
                        




                  if pantalla_Penales == True and monedaLanzada>=4:
                        screen.blit(imagen_Fondo, (0,0))
                        anotaciones(100,100, decode)
                        anotaciones(200,200, decode)
                        try:  
                              if len(match_players1)//2+len(match_goalkeepers1)//2==2:
                                    screen.blit(match_players1[0], match_players1[1])
                                    screen.blit(match_goalkeepers1[0], match_goalkeepers1[1])
                                    draw_text("Local   Anotaciones",pygame.font.SysFont('Algerian',40),(255,255,255), 70, 50)
                              if len(match_players2)//2+len(match_goalkeepers2)//2==2:
                                    screen.blit(match_players2[0], match_players2[1])
                                    screen.blit(match_goalkeepers2[0], match_goalkeepers2[1])
                                    draw_text("Visitante   Anotaciones",pygame.font.SysFont('Algerian',40),(255,255,255), 550, 50)
                              if len(match_players1)//2+len(match_goalkeepers1)//2==2 and len(match_players3)//2+len(match_goalkeepers3)//2==2:
                                    screen.blit(match_players3[0], (600,100))
                                    screen.blit(match_goalkeepers3[0], (600,400))
                                    draw_text("Visitante   Anotaciones",pygame.font.SysFont('Algerian',40),(255,255,255), 550, 50)
                              else:
                                    screen.blit(match_players3[0], match_players3[1])
                                    screen.blit(match_goalkeepers3[0], match_goalkeepers3[1])
                                    draw_text("Local   Anotaciones",pygame.font.SysFont('Algerian',40),(255,255,255), 70, 50)
                        except:
                              pass
                  
                        

            
            for event in pygame.event.get():
                  key = pygame.key.get_pressed()
                  if key[pygame.K_SPACE]:
                        game_Playing=True
                  if key[pygame.K_t] and (brasil_Team==True or argentina_Team==True or costarica_Team==True or game_Playing==True):
                        pantalla_Inicial=True

                  if event.type == pygame.QUIT:
                        run = False

            pygame.display.update()