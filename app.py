import rawpy
from PIL import Image
import os
import glob

pasta = "."  # Substitua pelo caminho da pasta que você deseja verificar

# Use a função glob para pegar todos os arquivos .dng na pasta
arquivos_dng = glob.glob(os.path.join(pasta, "*.dng"))

# Imprima o nome de cada arquivo .dng
for arquivo_dng in arquivos_dng:
	nome_arquivo = os.path.basename(arquivo_dng)

	# Carregando a imagem DNG
	raw = rawpy.imread(nome_arquivo)

	# Convertendo a imagem RAW para uma imagem RGB
	rgb = raw.postprocess()

	# Convertendo a imagem RGB para o formato JPEG
	jpeg_image = Image.fromarray(rgb)
	jpeg_path = f"output/{nome_arquivo}.jpg"
	jpeg_image.save(jpeg_path)

	print(f"Imagem {nome_arquivo} convertida para JPEG e salva com sucesso.")
