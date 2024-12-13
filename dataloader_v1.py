import os
from collections import Counter

# Función para contar las categorías en todos los archivos .txt de una carpeta
def contar_categorias_en_carpeta(carpeta):
    conteo_total = Counter()

    # Iterar sobre todos los archivos en la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.txt'):  # Filtrar solo los archivos .txt
            ruta_archivo = os.path.join(carpeta, archivo)
            
            with open(ruta_archivo, 'r') as archivo_txt:
                # Leer líneas del archivo y extraer las categorías
                lineas = archivo_txt.readlines()
                categorias = [linea.split()[0] for linea in lineas if linea.strip()]
                
                # Actualizar el conteo total
                conteo_total.update(categorias)
    
    return conteo_total

# Ruta de la carpeta con los archivos .txt
carpeta = 'Data_yolos_extra/fish/train/labels'

# Ejecutar la función y mostrar resultados
conteo_categorias = contar_categorias_en_carpeta(carpeta)
print("Conteo de categorías (en todos los archivos):")
for categoria, cantidad in conteo_categorias.items():
    print(f"Categoría {categoria}: {cantidad}")
