import cv2
import numpy as np

def detect_aruco_markers(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    if image is None:
        print("Erro: Imagem não encontrada.")
        return

    # Configuração ini
    aruco_dict_type = cv2.aruco.DICT_6X6_250
    arucoDict = cv2.aruco.getPredefinedDictionary(aruco_dict_type)
    arucoParams = cv2.aruco.DetectorParameters_create()

    # Detectar marcadores na imagem
    corners, ids, rejected = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

    if ids is not None:
        # Desenhar os contornos dos marcadores detectados na imagem
        cv2.aruco.drawDetectedMarkers(image, corners, ids)

        for i, corner in enumerate(corners):
            # corner[0] são os pontos dos cantos para o i-ésimo marcador detectado
            print(f"Cantos do Marcador ID {ids[i][0]}: {corner[0]}")
            # Cálculo de distâncias entre cantos>>>>>>>>>>>>>>>>>>>>>>

        # Mostra a imagem com marcadores
        cv2.imshow('Detected ArUco markers', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Nenhum marcador ArUco detectado.")


detect_aruco_markers("path_to_your_image.png")
