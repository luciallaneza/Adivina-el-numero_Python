**Objetivo del ejercicio:**    
Vamos a crear un juego donde el programa elija un número aleatorio entre 1 y 100, y el usuario lo adivine recibiendo pistas.

- 1er paso: Generar un número aleatorio (1 - 100).   
- 2º paso: Solicitar al usuario un intento.   
- 3er paso: Comparar el número generado por el ordenador con el número facilitado por el usuario.   
- 4º paso: aportar tips, pistas: `<,>`   
- 5º paso: en caso de acierto, generar mensaje de enhorabuena con el número de intentos utilizado.   
- 6º paso: contador intentos hasta el éxito.   
<br>

**Lista de tareas** 📚  
1. Generar una variable que incluya el rango numérico del 0 a 100 var=(1,100)   
2. Guardar el número en una variable.   
3. Solicitamos un número al usuario (en bucle):    
	3.1. Validar que sea un número.   
	3.2. Comparar el número dentro del bucle.   
	3.3. Si el número no es el elegido, aportar pistas `> , <`   
	3.4. Contabilizar intentos   
4. Imprimir número de intentos   
<br>

**Estructuras**   
1. Bucles   
1.1. Solicitar intentos de usuario -> `while True`   
2. Condicionales    
2.1. Intento de *correcto*, *muy bajo*, *muy alto*: `if, elif, else`   
<br>

**Qué variables necesitamos** ❓  
Las variables sin tildes   
1. numero_secreto -> entero -> `int`  
2. intento -> entero -> `int`   
3. contador -> entero -> `int`  
<br>

**Pseudocódigo**  📝
1. Generar numero_secreto entre 1 y 100 y guardarlo como variable   
2. Crear un contador de intentos y lo inicializamos, le damos valor_inicial = 0   
3. Dar la bienvenida al usuario   
4. Crear un bucle mientras que el usuario no haya acertado el numero_secreto.   
	4.1.  Solicitar al usuario un número entre 1 y 100 input().
		4.1.1 Si el número del usuario está fuera de rango, solicitamos de nuevo el número.   
	4.2. Condición: repetimos el código mientras se cumpla o no se cumpla esa condición -> `if elif else`:    
		4.2.1. Si el usuario no escribe un número válido, se le solicita de nuevo.   
		4.2.2. SI intento < numero_secreto:   
					- Decir "Más alto"   
			SI NO, SI intento > numero_secreto:   
				- Decir "Más bajo".   
			SI NO:   
				- Decir "¡OLE, has acertado!"   
				SALIR del bucle   
<br>

**Traducción**  🖥️ 
 1. Necesitamos importar el modulo `random` para generar numero_secreto entre 1 y 100 | `numero_secreto = numero.randint(1,100)`.  
2. Crear un contador de intentos y lo inicializamos, le damos valor_inicial = 0 | `contador = 0`   
3. Dar la bienvenida al usuario | `print=("Bienvenido a la búsqueda del número secreto. ¡Buena suerte!")`   
4. Crear un bucle mientras que el usuario no haya acertado el numero_secreto | `while True`   
	4.1. Solicitar al usuario un número entre 1 y 100 input() | `intento = int(input("Por favor indíqueme un número entero entre 1 y 100: "))`   
	4.1.1. Si el número del usuario está fuera de rango, solicitamos de nuevo el número y continuamos. |`if`, `continue`
	4.2. Condición: repetimos el código mientras se cumpla o no se cumpla esa condición -> `if elif else`:   
        4.2.1. Si el usuario no escribe un número válido, se vuelve a pedir   
		4.2.2 - SI intento `<` numero_secreto:    
				 - Decir "Más alto"   
			SI NO, SI intento `>` numero_secreto:   
				- Decir "Más bajo".   
			SI NO:   
				- Decir "¡OLE, has acertado!"   
				SALIR del bucle  🔚 


	