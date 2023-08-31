import rawpy
from PIL import Image
import os
import glob

folder = "./raw"
dng_files = glob.glob(os.path.join(folder, "*.dng"))

for dng_file in dng_files:
	file_name = os.path.basename(dng_file)

	raw = rawpy.imread(file_name)
	rgb = raw.postprocess()

	jpeg_image = Image.fromarray(rgb)
	jpeg_path = f"output/{file_name}.jpg"
	jpeg_image.save(jpeg_path)

	print(f"Image {file_name} converted to JPEG e and sabed successfully.")
