
// Se definen algunas constantes
#define ADC_VREF_mV    3300.0 // en milivoltios
#define ADC_RESOLUCION 4096.0 // Pines de entrada analógica = 12 bits = rango de lectura 0-4095.
#define LM35       36 // El pin GIOP36 (ADC0) del ESP32 está conectado al LM35
int ValorAnalogico = 0;
float milliVolt;
float TempC;
float TempF;

void setup() {
  // Se inicializa la comunicación serial a una velocidad de 115200 baudios
  Serial.begin(115200);
  pinMode(LM35,INPUT);
}

void loop() {
  // Se lee el valor ADC del sensor de temperatura
  ValorAnalogico = analogRead(LM35);

  // Se convierte el valor ADC a voltaje en milivoltios
  milliVolt = ValorAnalogico * (ADC_VREF_mV / ADC_RESOLUCION);

  // Se convierte el voltaje a temperatura en grados Celsius
  TempC = milliVolt / 10;

  // Se convierte la temperatura a grados Fahrenheit
  TempF = TempC * 9 / 5 + 32;

  // Se imprimen los valores de temperatura en el Monitor Serie
  Serial.print("Temperatura: ");
  Serial.print(TempC);   // Se imprime la temperatura en grados Celsius
  Serial.print("°C");
  Serial.print("  ~  "); // Separador entre grados Celsius y Fahrenheit
  Serial.print(TempF);   // Se imprime la temperatura en grados Fahrenheit
  Serial.println("°F");

  // Se agrega un retardo de 500 milisegundos antes de la siguiente iteración
  delay(500);
}
