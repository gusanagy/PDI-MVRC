import cv2
import os
from tqdm import tqdm


def pad_image_with_black(image, target_width, target_height):
    """
    Redimensiona uma imagem para um tamanho alvo usando preenchimento preto.
    
    Args:
        image: Array numpy representando a imagem
        target_width: Largura desejada
        target_height: Altura desejada
    
    Returns:
        Imagem redimensionada com padding preto
    """
    height, width = image.shape[:2]
    
    # Calcula o padding para cada lado
    top_pad = (target_height - height) // 2
    bottom_pad = target_height - height - top_pad
    left_pad = (target_width - width) // 2
    right_pad = target_width - width - left_pad
    
    # Aplica o padding preto
    padded_image = cv2.copyMakeBorder(
        image,
        top_pad,
        bottom_pad,
        left_pad,
        right_pad,
        cv2.BORDER_CONSTANT,
        value=(0, 0, 0)  # Cor preta
    )
    
    return padded_image

def process_dataset(input_folder, output_folder, target_width, target_height):
    """
    Processa todas as imagens em um diretório, padronizando seus tamanhos.
    
    Args:
        input_folder: Caminho para a pasta com as imagens originais
        output_folder: Caminho para salvar as imagens processadas
        target_width: Largura desejada para as imagens processadas
        target_height: Altura desejada para as imagens processadas
    """
    os.makedirs(output_folder, exist_ok=True)
    
    # Processa as imagens
    for filename in tqdm(os.listdir(input_folder)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            
            if image is not None:
                # Aplica o padding preto
                padded_image = pad_image_with_black(image, target_width, target_height)
                
                # Salva a imagem processada
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, padded_image)
                #print(f"Processada: {filename} -> {output_path}")

def process_multiple_directories(base_directories, dimensions):
    for base_dir in base_directories:
        for root, dirs, _ in os.walk(base_dir):
            for dir_name in dirs:
                input_folder = os.path.join(root, dir_name)
                output_folder = input_folder + "_borda_preta"
                
                # Caminho relativo a partir do diretório base
                relative_path = os.path.relpath(input_folder, start=os.getcwd())
                
                if relative_path in dimensions:
                    target_width, target_height = dimensions[relative_path]
                    print(f"Processando: {input_folder} com dimensões {target_width}x{target_height}")
                    process_dataset(input_folder, output_folder, target_width, target_height)
                else:
                    print(f"Dimensões não definidas para {relative_path}, ignorando...")

# Exemplo de uso
if __name__ == "__main__":
    base_directories = [
        "mvrc_train/train",
        "validation_input_jpgs"
    ]
    # Defina as dimensões alvo para cada pasta relevante

    dimensions = {
        "mvrc_train/train/gt_images": (8192, 8192),
        "mvrc_train/train/input_jpgs": (8192, 8192),
        "validation_input_jpgs/input_jpgs": (6720, 6000)
        }
    
    process_multiple_directories(base_directories, dimensions)
