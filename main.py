#Funcion que convierte de C a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Funcion que convierte a fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
#Realizamos pruebas de conversion
celsius = float(input('Proporcione su valor en celcius: '))
resultado = celsius_fahrenheit(celsius)
#Imprimimos el resultado
print(f'{celsius} C a F: {resultado:.2f}')
#RealizaMOS la prueba de fahrenheit a celsius
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
#Imprimimos el resultado
print(f'{fahrenheit} F a C : {resultado:0.2f}')
