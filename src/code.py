import cv2
import numpy as np

def morphological_filter(img):
    """Filtro morfológico composto com B1 e B2 definidos no artigo."""

    # B1 (cross 3x3)
    B1 = np.array([[0,1,0],
                   [1,1,1],
                   [0,1,0]], dtype=np.uint8)

    # B2 (diamond 5x5)
    B2 = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]], dtype=np.uint8)

    # Operação 1: (F ∘ B1) · B2
    A1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, B1)
    A1 = cv2.morphologyEx(A1, cv2.MORPH_CLOSE, B2)

    # Operação 2: (F · B2) ∘ B1
    A2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, B2)
    A2 = cv2.morphologyEx(A2, cv2.MORPH_OPEN, B1)

    # Filtro composto
    A3 = cv2.addWeighted(A1, 0.1, A2, 0.9, 0)

    return A3

def gradient_magnitude(img):
    """Calcula gradiente em 4 direções: 0, 90, 45 e 135 graus."""
    # Sobel tradicional
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    # Filtros para 45° e 135°
    kernel45 = np.array([[-2, -1, 0],
                         [-1,  0, 1],
                         [ 0,  1, 2]], dtype=np.float32)
    kernel135 = np.array([[ 0, 1, 2],
                          [-1, 0, 1],
                          [-2,-1, 0]], dtype=np.float32)

    g45 = cv2.filter2D(img, cv2.CV_64F, kernel45)
    g135 = cv2.filter2D(img, cv2.CV_64F, kernel135)

    # Magnitude combinada
    mag = np.sqrt(gx**2 + gy**2 + g45**2 + g135**2)

    # Converte para 8 bits
    mag8 = cv2.convertScaleAbs(mag)

    return mag8, gx, gy, g45, g135

def non_maximum_suppression(mag, gx, gy):
    """Supressão de não-máximos com base no ângulo do gradiente (usando magnitude 4 direções)."""
    M, N = mag.shape
    Z = np.zeros((M, N), dtype=np.uint8)

    # Ângulo em graus
    angle = np.arctan2(gy, gx) * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, M-1):
        for j in range(1, N-1):
            q = 255
            r = 255

            # direção 0° (horizontal)
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q = mag[i, j+1]
                r = mag[i, j-1]
            # direção 45°
            elif (22.5 <= angle[i,j] < 67.5):
                q = mag[i+1, j-1]
                r = mag[i-1, j+1]
            # direção 90° (vertical)
            elif (67.5 <= angle[i,j] < 112.5):
                q = mag[i+1, j]
                r = mag[i-1, j]
            # direção 135°
            elif (112.5 <= angle[i,j] < 157.5):
                q = mag[i-1, j-1]
                r = mag[i+1, j+1]

            # Mantém apenas se for máximo local
            if (mag[i,j] >= q) and (mag[i,j] >= r):
                Z[i,j] = mag[i,j]
            else:
                Z[i,j] = 0

    return Z

def hysteresis(img, low, high):
    """Duplo limiar + histerese."""
    strong = 255
    weak = int(low)

    res = np.zeros_like(img, dtype=np.uint8)

    strong_i, strong_j = np.where(img >= high)
    weak_i, weak_j = np.where((img <= high) & (img >= low))

    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak

    # Histerese: conectar fracos aos fortes
    M, N = img.shape
    for i in range(1, M-1):
        for j in range(1, N-1):
            if res[i,j] == weak:
                if ((res[i+1, j-1] == strong) or (res[i+1, j] == strong) or (res[i+1, j+1] == strong)
                    or (res[i, j-1] == strong) or (res[i, j+1] == strong)
                    or (res[i-1, j-1] == strong) or (res[i-1, j] == strong) or (res[i-1, j+1] == strong)):
                    res[i,j] = strong
                else:
                    res[i,j] = 0
    return res

def improved_canny(img):
    """Implementa o Canny morfologicamente melhorado."""
    # Passo 1: filtro morfológico
    denoised = morphological_filter(img)

    # Passo 2: gradiente em 4 direções
    mag, gx, gy, g45, g135 = gradient_magnitude(denoised)

    # Passo 3: supressão de não-máximos
    nms = non_maximum_suppression(mag, gx, gy)

    # Passo 4: Otsu para definir thresholds
    otsu_val, otsu_img = cv2.threshold(mag, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    high = int(otsu_val)
    low = int(0.5 * otsu_val)

    # Passo 5: duplo limiar + histerese
    edges = hysteresis(nms, low, high)

    return edges

# Exemplo de uso
if __name__ == "_main_":
    img = cv2.imread("Users/home/maiara/Pictures/tomate.jpg", cv2.IMREAD_GRAYSCALE)
    edges = improved_canny(img)

    cv2.imshow("Original", img)
    cv2.imshow("Improved Canny", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()