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