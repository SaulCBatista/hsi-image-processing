import cv2
import numpy as np

def rgb_to_hsi(image):
    image = image.astype(np.float32) / 255
    R, G, B = image[..., 2], image[..., 1], image[..., 0]
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-8
    theta = np.arccos(np.clip(num / den, -1, 1))

    H = np.where(B <= G, theta, 2*np.pi - theta)
    H = H / (2 * np.pi)

    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 * min_rgb) / (R + G + B + 1e-8)
    I = (R + G + B) / 3

    return H, S, I

def hsi_to_rgb(H, S, I):
    H = H * 2 * np.pi
    R = np.zeros_like(H)
    G = np.zeros_like(H)
    B = np.zeros_like(H)

    cond1 = (H >= 0) & (H < 2*np.pi/3)
    cond2 = (H >= 2*np.pi/3) & (H < 4*np.pi/3)
    cond3 = (H >= 4*np.pi/3) & (H <= 2*np.pi)

    B[cond1] = I[cond1] * (1 - S[cond1])
    R[cond1] = I[cond1] * (1 + S[cond1] * np.cos(H[cond1]) / np.cos(np.pi/3 - H[cond1]))
    G[cond1] = 3 * I[cond1] - (R[cond1] + B[cond1])

    H2 = H - 2*np.pi/3
    R[cond2] = I[cond2] * (1 - S[cond2])
    G[cond2] = I[cond2] * (1 + S[cond2] * np.cos(H2[cond2]) / np.cos(np.pi/3 - H2[cond2]))
    B[cond2] = 3 * I[cond2] - (R[cond2] + G[cond2])

    H3 = H - 4*np.pi/3
    G[cond3] = I[cond3] * (1 - S[cond3])
    B[cond3] = I[cond3] * (1 + S[cond3] * np.cos(H3[cond3]) / np.cos(np.pi/3 - H3[cond3]))
    R[cond3] = 3 * I[cond3] - (G[cond3] + B[cond3])

    rgb = np.stack([B, G, R], axis=-1)
    return np.clip(rgb * 255, 0, 255).astype(np.uint8)

def ajustar_brilho(I, fator):
    return np.clip(I + fator, 0, 1)

def ajustar_contraste(I, fator):
    return np.clip((I - 0.5) * fator + 0.5, 0, 1)

def equalizar_histograma(I):
    I_scaled = (I * 255).astype(np.uint8)
    I_eq = cv2.equalizeHist(I_scaled)
    return I_eq.astype(np.float32) / 255
