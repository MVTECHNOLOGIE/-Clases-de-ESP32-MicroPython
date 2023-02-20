from machine import Pin
import time

# Definir los pines de los LED
rojo = Pin(23, Pin.OUT)
ambar = Pin(22, Pin.OUT)
verde = Pin(1, Pin.OUT)
rojo_peatonal = Pin(3, Pin.OUT)
verde_peatonal = Pin(21, Pin.OUT)
buzzer = Pin(19, Pin.OUT)


# Bucle infinito
while True:
    # Rojo encendido
    rojo.value(1)
    ambar.value(0)
    buzzer.value(0)
    verde_peatonal.value(1)
    time.sleep(4)

    # buzzer y ámbar encendidos
    ambar.value(1)
    buzzer.value(1)
    time.sleep(3)

    # Rojo apagado, verde encendido
    rojo.value(0)
    verde_peatonal.value(0)
    verde.value(1)
    rojo_peatonal.value(1)
    ambar.value(0)
    buzzer.value(0)
    time.sleep(2)

    # Verde y ámbar encendidos
    ambar.value(1)
    buzzer.value(1)
    time.sleep(2)

    # Verde apagado
    verde.value(0)
    rojo_peatonal.value(0)
