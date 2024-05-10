from machine import ADC, Pin
import time
from random import randint
import sys
import _thread


pin_A = machine.Pin(18, machine.Pin.OUT)  #pin A y B del registro de corrimiento
pin_CLK = machine.Pin(19, machine.Pin.OUT)  #pin clock del registro de corrimiento
ledTorre1 = machine.Pin(26, machine.Pin.OUT)
ledTorre2 = machine.Pin(22, machine.Pin.OUT)
potenciometro = ADC(27)
boton= machine.Pin(4, machine.Pin.IN, Pin.PULL_DOWN)

#pines de las paletas
paleta1 = Pin(9, Pin.IN)
paleta2=machine.Pin(8, machine.Pin.IN)
paleta3=machine.Pin(7, machine.Pin.IN)
paleta4=machine.Pin(12, machine.Pin.IN)
paleta5=machine.Pin(11, machine.Pin.IN)
paleta6=machine.Pin(10, machine.Pin.IN)





#prender los led segun la configuracion del portero
def turnOnLed(status_led):
    pin_A.value(0)
    for led in status_led:
        
        pin_CLK.value(0)
        pin_A.value(led)
        pin_CLK.value(1)
    
#variables generales
eleccion=randint(0,6)
apagarLed=[0,0,0,0,0,0]
prenderLed=[1,1,1,1,1,1]
estadosChancha=[[1,1,0,0,0,0], [0,0,1,1,0,0], [0,0,0,0,1,1],[1,1,1,0,0,0], [0,0,0,1,1,1], [1,0,1,0,1,0], [0,1,0,1,0,1]]

contadorTirosHechos=0

run=True
while run:
    #print("contador", contadorTirosHechos)
    
    
    valorPotenciometro = potenciometro.read_u16()
    time.sleep(2)
    
    valorPotenciometroStr= str(valorPotenciometro)
    sys.stdout.write("#"+valorPotenciometroStr+'\n')
    
    botonStr=str(boton.value())
    sys.stdout.write("%"+botonStr+'\n')
    
    
    eleccion=0#randint(0,6)
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

    if boton.value():
        contadorTirosHechos+=1
    
    if contadorTirosHechos%2==0:
        ledTorre1.value(1)
        ledTorre2.value(0)
    else:
        ledTorre1.value(0)
        ledTorre2.value(1)
        



pin_A.value(0)