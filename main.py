from machine import ADC, Pin
import time
from random import randint
import sys
import _thread


pin_A = machine.Pin(18, machine.Pin.OUT)  #pin A y B del registro de corrimiento
pin_CLK = machine.Pin(19, machine.Pin.OUT)  #pin clock del registro de corrimiento
ledTorreLocal = machine.Pin(26, machine.Pin.OUT)
ledTorreVisitante = machine.Pin(22, machine.Pin.OUT)
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
        #asignar valor a los leds
        pin_CLK.value(0)
        pin_A.value(led)
        pin_CLK.value(1)
        #transmision de datos de los leds
        #sacar una letra segun estado del led (por hacer)
        
    
#variables generales
eleccionRandom=randint(0,6)
apagarLed=[0,0,0,0,0,0]
prenderLed=[1,1,1,1,1,1]
estadosChancha=[[1,1,0,0,0,0], [0,0,1,1,0,0], [0,0,0,0,1,1],[1,1,1,0,0,0], [0,0,0,1,1,1], [1,0,1,0,1,0], [0,1,0,1,0,1]]

contadorTirosHechos=0

run=True
while run:
    
    #print('boton', boton.value(), 'contador',contadorTirosHechos, eleccionRandom)
    time.sleep(0.3)
    
    #valor y transmicion datos potenciometro
    valorPotenciometro = potenciometro.read_u16()
    valorPotenciometroStr= str(valorPotenciometro//4350)
    sys.stdout.write("#"+valorPotenciometroStr+'\n')
    
    #valor y transmicion datos boton
    botonStr=str(boton.value())
    sys.stdout.write("%"+botonStr+'\n')
    
    #escogencia random de paletas y luces leds
    #eleccion=0#randint(0,6)
    turnOnLed(estadosChancha[eleccionRandom])


    #deteccion de paletas
    if paleta1.value()==0 and estadosChancha[eleccionRandom][0]==1:
        sys.stdout.write("A")
        
    if paleta2.value()==0 and estadosChancha[eleccionRandom][1]==1:
       sys.stdout.write("B")
       
    if paleta3.value()==0 and estadosChancha[eleccionRandom][2]==1:
        sys.stdout.write("C")
        
    if paleta4.value()==0 and estadosChancha[eleccionRandom][3]==1:
        sys.stdout.write("D")
        
    if paleta5.value()==0 and estadosChancha[eleccionRandom][4]==1:
        sys.stdout.write("E")
        
    if paleta6.value()==0 and estadosChancha[eleccionRandom][5]==1:
        sys.stdout.write("F")

    if boton.value():
        contadorTirosHechos+=1
        sys.stdout.write("G")
        if contadorTirosHechos>5:
            eleccionRandom=randint(0,6)
    
    #prender leds torres previo a comenzar el juego
    if contadorTirosHechos<=10:
        ledTorreLocal.value(1)
        ledTorreVisitante.value(1)
        turnOnLed([1,1,1,1,1,1])

        
        
    #prender leds torres segun local-visitante
    if contadorTirosHechos%2==0 and contadorTirosHechos>5:
        ledTorreLocal.value(1)
        sys.stdout.write("H")
        ledTorreVisitante.value(0)
        
        
    elif contadorTirosHechos%2!=0 and contadorTirosHechos>5:
        ledTorreLocal.value(0)
        sys.stdout.write("I")
        ledTorreVisitante.value(1)
    
        



pin_A.value(0)
