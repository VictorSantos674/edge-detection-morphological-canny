import cv2
import numpy as np

# ETAPA 1: SUAVIZAÇÃO COM FILTRO MORFOLÓGICO CUSTOMIZADO
def morphological_filter(img):
    """
    Aplica um filtro morfológico composto para suavização,
    utilizando operações de abertura e fechamento com dois kernels.
    """
    # B1 (cruz 3x3)
    B1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    
    # B2 (diamante 5x5)
    B2 = np.array([
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0]
    ], dtype=np.uint8)

    # Lógica do filtro composto
    A1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, B1)
    A1 = cv2.morphologyEx(A1, cv2.MORPH_CLOSE, B2)
    
    A2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, B2)
    A2 = cv2.morphologyEx(A2, cv2.MORPH_OPEN, B1)
    
    # Combinação ponderada dos resultados para a imagem final suavizada
    smoothed_image = cv2.addWeighted(A1, 0.1, A2, 0.9, 0)
    return smoothed_image

# ETAPA 2: CÁLCULO DO GRADIENTE EM 4 DIREÇÕES
def gradient_magnitude(img):
    """Calcula a magnitude do gradiente e retorna os componentes para o NMS."""
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    kernel45 = np.array([[-2, -1, 0], [-1,  0, 1], [ 0,  1, 2]], dtype=np.float32)
    kernel135 = np.array([[ 0, 1, 2], [-1, 0, 1], [-2,-1, 0]], dtype=np.float32)
    g45 = cv2.filter2D(img, cv2.CV_64F, kernel45)
    g135 = cv2.filter2D(img, cv2.CV_64F, kernel135)
    
    mag = np.sqrt(gx**2 + gy**2 + g45**2 + g135**2)
    mag8 = cv2.convertScaleAbs(mag)
    #mag_normalized = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    #mag8 = np.uint8(mag_normalized)
    
    return mag8, gx, gy

# ETAPA 3: SUPRESSÃO DE NÃO-MÁXIMOS (NMS)
def non_maximum_suppression(mag, gx, gy):
    """Afina as bordas espessas para uma largura de 1 pixel."""
    M, N = mag.shape
    Z = np.zeros((M, N), dtype=np.uint8)
    angle = np.arctan2(gy, gx) * 180. / np.pi
    angle[angle < 0] += 180
    
    for i in range(1, M-1):
        for j in range(1, N-1):
            q, r = 255, 255
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q, r = mag[i, j+1], mag[i, j-1]
            elif (22.5 <= angle[i,j] < 67.5):
                q, r = mag[i+1, j-1], mag[i-1, j+1]
            elif (67.5 <= angle[i,j] < 112.5):
                q, r = mag[i+1, j], mag[i-1, j]
            elif (112.5 <= angle[i,j] < 157.5):
                q, r = mag[i-1, j-1], mag[i+1, j+1]

            if (mag[i,j] >= q) and (mag[i,j] >= r):
                Z[i,j] = mag[i,j]
    return Z

# ETAPA 5: HISTERESE
def canny_histerese(img, low, high):
    """Usa duplo limiar para conectar e finalizar as bordas."""
    strong = 255
    weak = int(otsu_low_thresh) # Valor intermediário para pixels candidatos
    res = np.zeros_like(img, dtype=np.uint8)
    
    strong_i, strong_j = np.where(img >= high)
    weak_i, weak_j = np.where((img < high) & (img >= low))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    M, N = img.shape
    for i in range(1, M-1):
        for j in range(1, N-1):
            if res[i,j] == weak:
                if np.any(res[i-1:i+1, j-1:j+1] == strong):
                    res[i,j] = strong
                else:
                    res[i,j] = 0
    return res

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    img_path = "C:/Users/bielr/Downloads/codigoCanny/tomate.jpg"
    original_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if original_image is None:
        print(f"ERRO: A imagem não foi encontrada no caminho: {img_path}")
    else:
        # ETAPA 1: Suavização com Filtro Morfológico
        smoothed_image = morphological_filter(original_image)

        # ETAPA 2: Cálculo do Gradiente
        gradient_image, gx, gy = gradient_magnitude(smoothed_image)

        # ETAPA 3: Supressão de Não-Máximos
        nms_image = non_maximum_suppression(gradient_image, gx, gy)

        # ETAPA 4: Cálculo dos Limiares com Otsu
        otsu_high_thresh, _ = cv2.threshold(nms_image[nms_image > 0], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        otsu_low_thresh = int(0.5 * otsu_high_thresh)

        # ETAPA 5: Histerese
        final_edges = canny_histerese(nms_image, otsu_low_thresh, otsu_high_thresh)

        # --- EXIBIÇÃO DOS RESULTADOS ---
        cv2.imshow("1 - Filtro Morfologico", smoothed_image)
        cv2.imshow("2 - Magnitude do Gradiente", gradient_image)
        cv2.imshow("3 - Apos Supressao de Nao-Maximos (NMS)", nms_image)
        cv2.imshow("5 - Resultado Final com Histerese", final_edges)

        print(f"Limiar Alto (Otsu) calculado: {otsu_high_thresh}")
        print(f"Limiar Baixo (50% do Alto) usado: {otsu_low_thresh}")
        print("\nProcessamento concluído. Pressione qualquer tecla para sair.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
