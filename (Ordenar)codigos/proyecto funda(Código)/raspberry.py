import machine
from machine import ADC, Pin
import time
from random import randint
import serial

pin_A = machine.Pin(18, machine.Pin.OUT)  # Pin A y B del registro (conectado a GPIO 3)
pin_CLK = machine.Pin(19, machine.Pin.OUT)  # Pin CLK del registro (conectado a GPIO 2)
potenciometro = ADC(28)
paleta1=machine.Pin(12, machine.Pin.IN)
paleta2=machine.Pin(11, machine.Pin.IN)
paleta3=machine.Pin(10, machine.Pin.IN)
paleta4=machine.Pin(9, machine.Pin.IN)
paleta5=machine.Pin(8, machine.Pin.IN)
paleta6=machine.Pin(7, machine.Pin.IN)

pin_A.value(1) # Config de los pines de entrada  
"""
for i in range(8):  
    pin_CLK.value(1)  
    time.sleep(1)  
    pin_CLK.value(0)  
    print("apagado")
    time.sleep(1)  

    # Encender y apagar los LEDs
    pin_A.value(1)  
    time.sleep(0.5)  
    pin_A.value(0)  
    time.sleep(0.5)  
"""
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
    time.sleep(1)
    print(f'valor paleta 1:{paleta1.value()}')
    #print(f'valor paleta 2:{paleta2.value()}')
    #print(f'valor paleta 3:{paleta3.value()}')
    #print(f'valor paleta 4:{paleta4.value()}')
    #print(f'valor paleta 5:{paleta5.value()}')
    #print(f'valor paleta 6:{paleta6.value()}')
    numero=0
    if numero==1:
        eleccion=randint(0,6)
        #print(eleccion)
        turnOnLed(estadosChancha[eleccion])
        eleccion=randint(0,6)

    if numero==0:
        turnOnLed(apagarLed)
        
    #numero=0
    #time.sleep(0.2)
    #valor_potenciometro = potenciometro.read_u16()
    #print(valor_potenciometro)
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


