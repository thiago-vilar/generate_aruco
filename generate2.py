import numpy as np
import cv2

# Definindo o dicionário de dicionários ArUco
ARUCO_DICT = {
    "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
    "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000  # Adicionando a chave correta, se necessário
}

aruco_type = "DICT_4X4_1000"  # Corrigindo o nome
id = 1

# Verificando se o tipo de ArUco existe antes de acessá-lo
if aruco_type in ARUCO_DICT:
    arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])
    tag_size = 1000
    tag = np.zeros((tag_size, tag_size, 1), dtype="uint8")
    cv2.aruco.drawMarker(arucoDict, id, tag_size, tag, 1)

    # Salvar o marcador gerado
    tag_name = "arucoMarkers/" + aruco_type + "_" + str(id) + ".png"
    cv2.imwrite(tag_name, tag)
    cv2.imshow("ArUco Tag", tag)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"ArUco type '{aruco_type}' not defined in ARUCO_DICT.")
