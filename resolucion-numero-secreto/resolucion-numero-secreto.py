import random  # ← Esta línea es necesaria, se importa la librería

numero_secreto = random.randint(1, 100) # Generar numero_secreto entre 1 y 100
# print(numero_secreto) # Para confirmar que la función anterior está funcionando 
contador = 0

print("\n Bienvenido a la búsqueda del número secreto. ¡Buena suerte!")
print("=" * 50) # Imprime 50 signos de igual seguidos, crea una línea separadora.

while True:
    intento_usuario = int(input("Por favor indíqueme un número entero entre 1 y 100: "))
    contador += 1
    
    if intento_usuario < numero_secreto:
        print("Más alto")
    elif intento_usuario > numero_secreto:
        print("Más bajo")
    else:
        print(f"\n🎉 ¡OLE, has acertado! Lo lograste en {contador} intentos.")
        break



