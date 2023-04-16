# Importar módulos necesarios
import machine  
import time

# Definir el pin al que está conectado el LM35
LM35_pin = machine.Pin(36)

# Crear un objeto ADC
adc = machine.ADC(LM35_pin)

# Configurar el rango de lectura del ADC
adc.atten(machine.ADC.ATTN_11DB)

# Función para convertir el valor ADC en temperatura en grados Celsius
def adc_a_temperatura_celsius(adc_valor):
    return (adc_valor * 3.3 / 4095) * 100

# Función para convertir la temperatura en grados Celsius a grados Fahrenheit
def celsius_a_fahrenheit(temp_celsius):
    return temp_celsius * 9/5 + 32

# Bucle principal
while True:
    # Leer el valor ADC del LM35
    adc_valor = adc.read()

    # Convertir el valor ADC en temperatura en grados Celsius
    temp_celsius = adc_a_temperatura_celsius(adc_valor)

    # Convertir la temperatura en grados Celsius a grados Fahrenheit
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

    # Imprimir las temperaturas
    print("Temperatura: {:.2f} °C  ~  {:.2f} °F".format(temp_celsius, temp_fahrenheit))

    # Esperar un segundo antes de leer de nuevo
    time.sleep(1)

