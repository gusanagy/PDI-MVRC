import os

# Diccionario de asignación de categorías por nombre de carpeta
categorias = {
    'fish2': 0,
    'shark': 1,
    'octopus':2,
    'starfish':3,
    'ray':4,
    'turtle':5,
    'jellyfish':6,
    # Agrega más categorías según sea necesario
}

# Función para procesar los archivos .txt y actualizar el primer número
def actualizar_labels(ruta_label, nuevo_numero):
    for archivo in os.listdir(ruta_label):
        if archivo.endswith('.txt'):  # Procesar solo archivos .txt
            ruta_archivo = os.path.join(ruta_label, archivo)
            
            # Leer el archivo y modificar el primer número
            with open(ruta_archivo, 'r') as f:
                lineas = f.readlines()
            
            nuevas_lineas = []
            for linea in lineas:
                if linea.strip():  # Solo procesar líneas no vacías
                    partes = linea.split()
                    partes[0] = str(nuevo_numero)  # Cambiar el primer número
                    nuevas_lineas.append(' '.join(partes))
            
            # Sobrescribir el archivo con las líneas modificadas
            with open(ruta_archivo, 'w') as f:
                f.write('\n'.join(nuevas_lineas) + '\n')

# Función principal para recorrer las carpetas y actualizar los archivos
def procesar_carpetas(carpeta_base):
    for carpeta_principal in os.listdir(carpeta_base):
        ruta_principal = os.path.join(carpeta_base, carpeta_principal)
        if os.path.isdir(ruta_principal) and carpeta_principal in categorias:
            nuevo_numero = categorias[carpeta_principal]
            
            # Recorrer subcarpetas train y valid
            for subcarpeta in ['train', 'valid']:
                ruta_subcarpeta = os.path.join(ruta_principal, subcarpeta)
                
                # Verificar si existe la carpeta 'label'
                ruta_label = os.path.join(ruta_subcarpeta, 'labels')
                if os.path.exists(ruta_label) and os.path.isdir(ruta_label):
                    actualizar_labels(ruta_label, nuevo_numero)

# Ruta base donde están las carpetas principales (pez, pulpo, etc.)
carpeta_base = 'Data_yolos_extra'

# Ejecutar la función principal
procesar_carpetas(carpeta_base)

print("Actualización de labels completada.")
