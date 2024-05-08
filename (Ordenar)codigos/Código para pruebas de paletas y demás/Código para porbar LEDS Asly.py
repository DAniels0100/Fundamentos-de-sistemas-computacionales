import machine
import time

pin_A = machine.Pin(19, machine.Pin.OUT)  # Pin A y B del registro (conectado a GPIO 3)
pin_CLK = machine.Pin(20, machine.Pin.OUT)  # Pin CLK del registro (conectado a GPIO 2)

pin_A.value(1) # Config de los pines de entrada  

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

pin_A.value(0)
