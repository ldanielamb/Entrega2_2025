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

archivo_csv = r"C:\Users\danim\OneDrive\Escritorio\Primer semestre\Programación I\Entrega2_2025-1\SalesJan2009.csv" # Ruta del archivo
pais = input("Ingrese el país del que desea información: ").strip() # Se le pide la información al usuario

# Corriendo el programa 
resultado = numero_de_ventas(archivo_csv, "Country", pais) # Se definen los parámetros
print(f"El país '{pais}' ha registrado {resultado} ventas en el mes.") # Se imprime el resultado
