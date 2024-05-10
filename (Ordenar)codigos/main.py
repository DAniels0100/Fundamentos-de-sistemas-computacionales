from machine import ADC, Pin
import time
from random import randint
import sys
import _thread


pin_A = machine.Pin(18, machine.Pin.OUT)  # Pin A y B del registro (conectado a GPIO 3)
pin_CLK = machine.Pin(19, machine.Pin.OUT)  # Pin CLK del registro (conectado a GPIO 2)
ledTorre1 = machine.Pin(26, machine.Pin.OUT)
ledTorre2 = machine.Pin(22, machine.Pin.OUT)
potenciometro = ADC(27)
boton= machine.Pin(5, machine.Pin.IN, Pin.PULL_DOWN)

paleta1=machine.Pin(12, machine.Pin.IN)
paleta2=machine.Pin(11, machine.Pin.IN)
paleta3=machine.Pin(10, machine.Pin.IN)
paleta4=machine.Pin(9, machine.Pin.IN)
paleta5=machine.Pin(8, machine.Pin.IN)
paleta6=machine.Pin(7, machine.Pin.IN)


visitante=False
local=False
 # Config de los pines de entrada  

def turnOnLed(status_led):
    pin_A.value(0)
    for led in status_led:
        
        pin_CLK.value(0)
        pin_A.value(led)
        pin_CLK.value(1)
    

eleccion=randint(0,6)
apagarLed=[0,0,0,0,0,0]
estadosChancha=[[1,1,0,0,0,0], [0,0,1,1,0,0], [0,0,0,0,1,1],[1,1,1,0,0,0], [0,0,0,1,1,1], [1,0,1,0,1,0], [0,1,0,1,0,1]]

run=True
while run:
    valorPotenciometro = potenciometro.read_u16()
    time.sleep(2)
    numero=1
    
    valorPotenciometroStr= str(valorPotenciometro)
    sys.stdout.write("#"+valorPotenciometroStr+'\n')
    
    botonStr=str(boton.value())
    sys.stdout.write("%"+botonStr+'\n')
    
    print('1 '+str(paleta1.value()))
    print("2 "+str(paleta2.value()))
    print("3 "+str(paleta3.value()))
    print("4 "+str(paleta4.value()))
    print("5 "+str(paleta5.value()))
    print("6 "+str(paleta6.value()))
    
    if numero:
        eleccion=randint(0,6)
        turnOnLed(estadosChancha[eleccion])

        if paleta1.value()==0 and estadosChancha[eleccion][0]==1:
            sys.stdout.write("A")
            
        if paleta2.value()==0 and estadosChancha[eleccion][1]==1:
           sys.stdout.write("B")
           
        if paleta3.value()==0 and estadosChancha[eleccion][2]==1:
            sys.stdout.write("C")
            
        if paleta4.value()==0 and estadosChancha[eleccion][3]==1:
            sys.stdout.write("D")
            
        if paleta5.value()==0 and estadosChancha[eleccion][4]==1:
            sys.stdout.write("E")
            
        if paleta6.value()==0 and estadosChancha[eleccion][5]==1:
            sys.stdout.write("F")

    if numero==0:
        turnOnLed(apagarLed)
    visitante, local= True, True
    if visitante:
        ledTorre1.value(1)
        
        
        #visitante=False
        
    if local:
        ledTorre2.value(1)
        
        
        #local=False
        #print(local)
    
    #if valor_potenciometro ==0:
 
     #   turnOnLed(estadosCancha[0])
    #elif valor_potenciometro >50000:
     #   lista_led=[0,0,0,1,1,0]
      #  turnOnLed(lista_led)
    #elif valor_potenciometro <50000 and valor_potenciometro >40000:
        
        #lista_led=[0,1,1,1,0,0]
        #turnOnLed(lista_led)
        
    #elif numero == 4:
        
        #lista_led=[0,1,1,1,1,0]
        #turnOnLed(lista_led)
        

pin_A.value(0)