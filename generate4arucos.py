import cv2
from fpdf import FPDF

# Verificar os métodos disponíveis no módulo aruco (descomente a linha abaixo para executar uma vez e verifique a saída)
# print(dir(cv2.aruco))

# Configuração inicial para os marcadores ArUco
aruco_dict_type = cv2.aruco.DICT_6X6_250

# Criar um documento PDF A4
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

# Tamanho dos marcadores e margens para o PDF
marker_size = 50  # Tamanho do marcador em mm
margin = 10       # Margem em mm

# Coordenadas iniciais no PDF para colocação dos marcadores
positions = [(margin, margin), (210 - margin - marker_size, margin),
             (margin, 297 - margin - marker_size), (210 - margin - marker_size, 297 - margin - marker_size)]

# Gerar e adicionar marcadores ao PDF
for i, position in enumerate(positions):
    id = i + 1  # ID do marcador
    
    # Tenta gerar o dicionário ArUco e o marcador
    try:
        arucoDict = cv2.aruco.getPredefinedDictionary(aruco_dict_type)
        tag = cv2.aruco.generateImageMarker(arucoDict, id, 600)  # Substituição especulativa para drawMarker
    except Exception as e:
        print(f"Erro ao criar o marcador: {e}")
        continue
    
    image_path = f"aruco_{id}.png"
    cv2.imwrite(image_path, tag)  # Salva a imagem localmente

    # Adicionar a imagem ao PDF
    pdf.image(image_path, x=position[0], y=position[1], w=marker_size)

# Salvar o PDF
pdf.output("ArUco_Markers.pdf")

# Remover as imagens após a inclusão no PDF
import os
for i in range(1, 5):
    image_path = f"aruco_{i}.png"
    if os.path.exists(image_path):
        os.remove(image_path)
