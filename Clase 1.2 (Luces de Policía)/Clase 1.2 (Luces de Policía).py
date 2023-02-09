# Importar las librerías necesarias
from machine import Pin # Importamos la librería machine
import time # Importamos la librería time, la cual contiene la función sleep que usaremos
#para controlar el tiempo de encendido y apagado de los LED

# Definir una lista de pines para los LED
leds = [Pin(i, Pin.OUT) for i in (23, 22, 01, 03, 21, 19)] # Creamos una lista con los pines que usaremos para los LED

def secuencia_policia(leds):
    """
    Simula una secuencia de luces de policía.
    :param leds: Lista de objetos Pin para los LED.
    """
    while True:
        for led in leds: #Iteramos sobre cada uno de los elementos de la lista de LED
            led.on()
            time.sleep(0.05)
            led.off()
        for led in leds[::-1]: # Iteramos sobre los LED en orden inverso
            led.on()
            time.sleep(0.05)
            led.off()

# Ejecutar la función secuencia_policia
secuencia_policia(leds)# Llamamos a la función secuencia_policia y le pasamos la lista de LED
# como argumento. La función será ejecutada y los LED comenzarán a parpadear en una secuencia
# de luces de policía.
