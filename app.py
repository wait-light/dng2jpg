import rawpy
from PIL import Image

# Carregando a imagem DNG
dng_path = "DSC_2298.dng"
raw = rawpy.imread(dng_path)

# Convertendo a imagem RAW para uma imagem RGB
rgb = raw.postprocess()

# Convertendo a imagem RGB para o formato JPEG
jpeg_image = Image.fromarray(rgb)
jpeg_path = "DSC_2298.dng.jpg"
jpeg_image.save(jpeg_path)

print("Imagem DNG convertida para JPEG e salva com sucesso.")
