#EJERCICIO 1 (PRIMER EJERCICIO)

def encontrar_letra_h(palabra):
    # Convertimos la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas
    palabra = palabra.lower()
    
    # Buscamos la letra 'h' en la palabra
    posiciones = [i for i, letra in enumerate(palabra) if letra == 'h']
    
    if posiciones:
        print(f"La letra 'H' se encuentra en las posiciones: {posiciones}")
    else:
        print("La letra 'H' no se encontró en la palabra.")

# Solicitar al usuario que ingrese una palabra
palabra_usuario = input("Escribe la palabra: ")
encontrar_letra_h(palabra_usuario)











#EJERCICIO 2 (SEGUNDO EJERCICIO) EL SEGUNDO TAMBIEN ESTA LOS CODIGOS SEPARADOS EN OTRA CARPETA DE MI GITHUP.

import numpy as np
import matplotlib.pyplot as plt

# Definir el rango de valores para x
x = np.linspace(0, 2 * np.pi, 100)  # 100 puntos entre 0 y 2π

# Calcular los valores de seno y coseno
seno = np.sin(x)
coseno = np.cos(x)

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.plot(x, seno, color='red', label='Seno')
plt.plot(x, coseno, color='blue', label='Coseno')

# Añadir título y etiquetas
plt.title('Funciones Seno y Coseno')
plt.xlabel('x (radianes)')
plt.ylabel('Valor')
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Línea horizontal en y=0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Línea vertical en x=0
plt.grid()
plt.legend()
plt.show()
