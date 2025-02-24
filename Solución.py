import csv # Módulo que maneja los archivos csv (valores separados por comas)

def numero_de_ventas(nombre_archivo, columna, valor_buscado): # Función que permite sumar las ventas mediante conteo de ocurrencias
    contador = 0 # Se inicializa el contador en cero
    valor_buscado = valor_buscado.strip().lower() # Se eliminan los espacios innecesarios y se convierte a minúscula para un mejor manejo
    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo: # Se abre un archivo en modo lectura especificando que tiene como juego de carácteres la codificación utf-8
        leer = csv.reader(archivo) # Es una función del módulo csv que se usa para leer archivos y delvolver cada fila como una lista de valores
        titulos = next(leer)  # Lee y guarda la primera fila en la variable titulos
        indice_titulo = titulos.index(columna)  # Obtiene el índice de la columna deseada

        for fila in leer: # Comienza desde la segunda fila
            if fila[indice_titulo].strip().lower() == valor_buscado: # Si el valor encontrado en el índice y fila coincide con el ingresado, se suma 1 al contador
                contador += 1
                
    return contador # Se retorna el total de la suma

def paises(nombre_archivo,columna): # Función para buscar cuáles países están en el archivo
    with open(nombre_archivo, "r", encoding="utf-8") as archivo: # Se abre el archivo
        leer = csv.reader(archivo) # Se configura para ser leído con el método csv.reader
        titulos = next(leer) # Se va a leer solo la primera fila con el next
        indice_titulo = titulos.index(columna) # Se busca el índice en la primera fila de la columna deseada, que en este caso tiene el nombre de country
        paises = {fila[indice_titulo].strip().lower() for fila in leer} # Se crea un diccionario (que no permite repeticiones) que tiene como elemento el país encontrado al recorrer cada fila con el índice antes definido
    return sorted(paises) # Se retorna la variable ordenada alfabéticamente


archivo_csv = r"C:\Users\danim\OneDrive\Escritorio\Primer semestre\Programación I\Entrega2_2025-1\SalesJan2009.csv" # Ruta del archivo

# Menú de países disponibles
print("\n---------------------------------------------------------------------------------------")
print("------------------------Países en los que se registraron ventas------------------------\n")
paises_disponibles = paises(archivo_csv,"Country") # Se llama a la función con los parámetros correspondientes

for pais in paises_disponibles: # Se va a imprimir cada resultado encontrado en el diccionario
    print(f"- {pais.capitalize()}")

print("\n---------------------------------------------------------------------------------------")
while True: # Ciclo para manejar errores
    try:
        pais = input("Ingrese el país del que desea información: ").strip().lower() # El usuario ingresa el país
        
        if pais not in paises_disponibles: # Si la opción no es correcta, es decir, no se encuentra entre los valores que se obtuvieron en el diccionario
            raise ValueError("El país ingresado no está en la lista. Intente de nuevo.") # Se va a imprimir ese mensaje personalizado

        resultado = numero_de_ventas(archivo_csv, "Country", pais) # Fuera del condicional, se establece lo que pasa si el valor ingresado si se encuentra en las opciones
        print(f"\nEl país '{pais.capitalize()}' ha registrado {resultado} ventas en el mes.") 
        break  # Salimos del loop si la entrada es correcta

    except ValueError as e: 
        print(e)  # Muestra el mensaje de error personalizado
print("\n")