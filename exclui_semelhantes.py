import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Função para redimensionar imagens mantendo proporções
def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    resized = cv2.resize(image, dim, interpolation=inter)
    
    return resized

# Função para adicionar bordas e garantir o mesmo tamanho
def add_padding(image, target_size=(300, 300)):
    h, w = image.shape[:2]
    target_h, target_w = target_size

    # Só adiciona padding se a imagem for menor que o tamanho alvo
    if h > target_h or w > target_w:
        # Redimensionar sem distorção
        return image
    
    # Calcula a diferença de tamanho para adicionar as bordas
    top = max(0, (target_h - h) // 2)
    bottom = max(0, target_h - h - top)
    left = max(0, (target_w - w) // 2)
    right = max(0, target_w - w - left)

    # Adiciona bordas pretas para manter o tamanho 300x300
    padded_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    
    return padded_image

# Função para calcular a similaridade entre duas imagens
def compare_images(imageA, imageB):
    # Redimensionar imagens mantendo proporção
    imageA = resize_with_aspect_ratio(imageA, width=300, height=300)
    imageB = resize_with_aspect_ratio(imageB, width=300, height=300)
    
    # Adicionar bordas para garantir tamanho 300x300
    imageA = add_padding(imageA, target_size=(300, 300))
    imageB = add_padding(imageB, target_size=(300, 300))
    
    # Garantir que as imagens tenham exatamente o mesmo tamanho
    imageA = cv2.resize(imageA, (300, 300))
    imageB = cv2.resize(imageB, (300, 300))
    
    # Converter para escala de cinza
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # Calcular a similaridade estrutural (SSIM)
    score, _ = ssim(grayA, grayB, full=True)
    return score

# Função para excluir imagens similares
def delete_similar_images(directory, threshold=0.8):
    images = []
    file_names = []
    
    print(f"Carregando imagens do diretório: {directory}")
    
    # Carregar as imagens do diretório
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            file_path = os.path.join(directory, filename)
            image = cv2.imread(file_path)
            if image is not None:
                images.append(image)
                file_names.append(file_path)
                print(f"Imagem {filename} carregada com sucesso.")
    
    print(f"{len(images)} imagens carregadas.")
    
    # Comparar imagens e excluir as similares
    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            print(f"Comparando {file_names[i]} com {file_names[j]}...")
            similarity_score = compare_images(images[i], images[j])
            print(f"Similaridade entre {file_names[i]} e {file_names[j]}: {similarity_score:.4f}")
            
            if similarity_score > threshold:
                print(f"Imagem {file_names[j]} é similar a {file_names[i]} com similaridade {similarity_score:.2f}. Excluindo {file_names[j]}.")
                os.remove(file_names[j])
                file_names[j] = None  # Marcar como excluída para evitar repetição
            else:
                print(f"Imagem {file_names[j]} não foi excluída. Similaridade abaixo do threshold ({threshold}).")

# Diretório com as imagens
image_directory = 'imagens'
delete_similar_images(image_directory)
