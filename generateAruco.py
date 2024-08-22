import numpy as np
import cv2

# Inicialização do dicionário ArUco
ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50
}

aruco_type = "DICT_4X4_50"
id = 1  # ID do marcador que você quer gerar

# Obtém o dicionário ArUco pré-definido
arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])

print(f"ArUco type '{aruco_type}' with ID '{id}'")
tag_size = 1000  # Define o tamanho do marcador

# Usa a função generateImageMarker para criar o marcador
tag = cv2.aruco.generateImageMarker(arucoDict, id, tag_size)

# Salva o marcador gerado
tag_name = f"arucoMarkers/{aruco_type}_{id}.png"
cv2.imwrite(tag_name, tag)

# Mostra o marcador gerado
cv2.imshow("ArUco Tag", tag)
cv2.waitKey(0)
cv2.destroyAllWindows()

