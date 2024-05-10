#Comprobar los pines en este código:

from machine import ADC, Pin
import time
import sys

pin_A = Pin(18, Pin.OUT)  # Pin A y B del registro (conectado a GPIO 3)
pin_CLK = Pin(19, Pin.OUT)  # Pin CLK del registro (conectado a GPIO 2)

# Leds torres
ledTorre1 = Pin(26, Pin.OUT)
ledTorre2 = Pin(22, Pin.OUT)

# Potenciómetro
potenciometro = ADC(26)

# Botón de la maqueta
boton = Pin(5, Pin.IN, Pin.PULL_DOWN)

# Definimos las variables de los pines en la Raspberry
paleta1 = Pin(10, Pin.IN)
paleta2 = Pin(11, Pin.IN)
paleta3 = Pin(12, Pin.IN)
paleta4 = Pin(7, Pin.IN)
paleta5 = Pin(8, Pin.IN)
paleta6 = Pin(9, Pin.IN)

# Estados de los Leds (listas)
apagarLed = [0, 0, 0, 0, 0, 0]

def turnOnLed(status_led):
    pin_CLK.value(0)  # Asegurarse de que el CLK está en estado bajo antes de cambiar los LEDs
    for led in status_led:
        pin_A.value(led)
        pin_CLK.value(1)
        pin_CLK.value(0)  # Cambiar a estado bajo después de cambiar cada LED

while True:
    valorPotenciometro = potenciometro.read_u16()  # Lectura del potenciómetro
    time.sleep(0.5)  # Delay para ver mejor los resultados

    sys.stdout.write("#" + str(valorPotenciometro) + '\n')  # Escribir por pantalla el valor del potenciómetro con un #
    sys.stdout.write("%" + str(boton.value()) + '\n')  # Escribir por pantalla el valor del botón con %

    # Printear por pantalla el valor de cada paleta, ya sea 0 o 1
    print('Paleta 1 ' + str(paleta1.value()))
    print("Paleta 2 " + str(paleta2.value()))
    print("Paleta 3 " + str(paleta3.value()))
    print("Paleta 4 " + str(paleta4.value()))
    print("Paleta 5 " + str(paleta5.value()))
    print("Paleta 6 " + str(paleta6.value()))

    # Verificar el estado de cada paleta y encender el LED correspondiente
    if paleta1.value()==0:
        turnOnLed([0, 0, 0, 0, 0, 1])  # Encender solo el LED F si la paleta 1 está activa
        print("A - Paleta 1 Activa")
    elif paleta2.value()==0:
        turnOnLed([0, 0, 0, 0, 1, 0])  # Encender solo el LED E si la paleta 2 está activa
        print("B - Paleta 2 Activa")
    elif paleta3.value()==0:
        turnOnLed([0, 0, 0, 1, 0, 0])  # Encender solo el LED D si la paleta 3 está activa
        print("C - Paleta 3 Activa")
    elif paleta4.value()==0:
        turnOnLed([0, 0, 1, 0, 0, 0])  # Encender solo el LED C si la paleta 4 está activa
        print("D - Paleta 4 Activa")
    elif paleta5.value()==0:
        turnOnLed([0, 1, 0, 0, 0, 0])  # Encender solo el LED B si la paleta 5 está activa
        print("E - Paleta 5 Activa")
    elif paleta6.value()==0:
        turnOnLed([1, 0, 0, 0, 0, 0])  # Encender solo el LED A si la paleta 6 está activa
        print("F - Paleta 6 Activa")
    else:
        turnOnLed(apagarLed)  # Si ninguna paleta está activa, apagar todos los LEDs
    
    ledTorre1.value(1)  # Activar LED de torre 1
    ledTorre2.value(1)  # Activar LED de torre 2
