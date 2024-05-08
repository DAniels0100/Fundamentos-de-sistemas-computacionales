import pygame

import serial

pygame.init()

screen=pygame.display.set_mode((800,600))

screen.fill((25,255,255))
Rpi=serial.Serial(port="COM5", baudrate=115200)

try:
    Rpi.open()
except:
    if (Rpi.isOpen()):
        print("conectado")
    else:
        print('no conecto')


run=True
while run:

    if (Rpi.isOpen()):
        datos=Rpi.readline()
        decode=datos.decode('UTF-8')
        if decode[0]=="#":
            decode=decode[1:]
            if int(decode)<20000:
                print('equipo 1')
            elif int(decode)>20000 and int(decode)<50000:
                print("equipo 2")
            elif int(decode)>50000:
                print('equipo 3')
        if decode[0]=="%":
            decode=decode[1:]
            if int(decode)==1:
                print("selecionado")
        if decode[0]=="A":
            print('paleta 1 activa')
            screen.fill((100,100,200))
        if decode[0]=="B":
            print('paleta 2 activa')
            screen.fill((100,200,100))
        if decode[0]=="C":
            print('paleta 3 activa')
            screen.fill((200,100,100))
        if decode[0]=="D":
            print('paleta 4 activa')
            screen.fill((150,100,100))
        if decode[0]=="E":
            print('paleta 5 activa')
            screen.fill((100,100,150))
        if decode[0]=="F":
            print('paleta 6 activa')
            screen.fill((100,150,100))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Rpi.close()
            quit()
    pygame.display.update()