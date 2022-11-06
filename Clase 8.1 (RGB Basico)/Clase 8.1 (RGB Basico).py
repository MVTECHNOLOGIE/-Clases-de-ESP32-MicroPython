#M&V_TECHNOLOGIE

#Clase N°8.1 "RGB"

# Importamos las siguentes librerias
#Machine: es un módulo específico de MicroPython que contiene funciones y clases que permiten obtener acceso directo y
#sin restricciones sobre el hardware del microcontrolador (CPU, pines, temporizadores, ADC,  buses –UART, SPI, I2C, etc.).

# Time: es una librería estándar de MicroPython proporciona un conjunto de funciones para indicar el tiempo que el microcontrolador
#lleva encendido, medir intervalos de tiempo e introducir retardos (esperas) en la ejecución de los programas

from machine import Pin, PWM
import time


frecuencia = 5000
# Declarar variables para los pines
Rojo  = PWM(Pin(23),frecuencia)     #Declaramos que la variable "Rojo" Perteneciente al pin 4 y quedara como salida "OUTPUT"
Verde = PWM(Pin(22),frecuencia)    #Declaramos que la variable "Verde" Perteneciente al pin 14 y quedara como salida "OUTPUT"
Azul  = PWM(Pin(1),frecuencia)     #Declaramos que la variable "Azul" Perteneciente al pin 15 y quedara como salida "OUTPUT"


def colour(G,B,R):
    
        Rojo.duty (R*4)      
        Verde.duty (G*4)
        Azul.duty (B*4)

while True:                #Declaramos el bucle infinito
    
     colour(255,0,0)     #Verde
     time.sleep(1)       #Colocamos un tiempo de espera de 1 segundo
    
     colour(0,255,0)     #Azul
     time.sleep(1)       #Colocamos un tiempo de espera de 1 segundo
    
     colour(0,0,255)     #Rojo
     time.sleep(1)       #Colocamos un tiempo de espera de 1 segundos
    
     colour(0,0,0)       #Apagado
     time.sleep(1)       #Colocamos un tiempo de espera de 3 segundos
     
     colour(0,255,148)   #Purpura 
     time.sleep(1)       #Colocamos un tiempo de espera de 4 segundos