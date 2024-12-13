import os
import random
import shutil

# Directorio origen con todas las imágenes
source_dir = "Data_mejora/input_jpgs"
# Directorios destino
destination_90 = "/home/pdi-b06/Area de Trabalho/JoseR/FiveAPlus-Network/datafer/MPCR/train/input"
destination_10 = "/home/pdi-b06/Area de Trabalho/JoseR/FiveAPlus-Network/datafer/MPCR/test/input"

# Crear las carpetas destino si no existen
os.makedirs(destination_90, exist_ok=True)
os.makedirs(destination_10, exist_ok=True)

# Obtener todas las imágenes del directorio origen
images = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

# Barajar las imágenes y dividirlas en 90% y 10%
random.shuffle(images)
split_index = int(len(images) * 0.9)
images_90 = images[:split_index]
images_10 = images[split_index:]

# Función para copiar archivos
def copy_files(file_list, source, destination):
    for file_name in file_list:
        source_path = os.path.join(source, file_name)
        destination_path = os.path.join(destination, file_name)
        shutil.copy(source_path, destination_path)

# Copiar los archivos a las carpetas correspondientes
copy_files(images_90, source_dir, destination_90)
copy_files(images_10, source_dir, destination_10)

print(f"Proceso completado. {len(images_90)} imágenes en {destination_90}, {len(images_10)} imágenes en {destination_10}.")
