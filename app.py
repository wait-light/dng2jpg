import rawpy
import imageio
import re
import os
import glob

def check_folder_existence(folder_name):
	if not os.path.exists(folder_name):
		os.makedirs(folder_name)
		print(f"Folder \"{folder_name}\" created successfully.")

def dng_name_clear(file_name):
	return re.sub(r"\.dng$", "", file_name)

def dng_renamer(dng_files, output_folder):
	for dng_file in dng_files:
		file_name = os.path.basename(dng_file)
		cleaned_file_name = dng_name_clear(file_name)

		raw = rawpy.imread(dng_file)
		rgb = raw.postprocess()

		img = imageio.core.util.Array(rgb)
		jpeg_path = f"{output_folder}/{cleaned_file_name}.jpg"
		imageio.imwrite(jpeg_path, img)

		print(f"Image {file_name} converted to JPEG and saved successfully.")

raw_folder = "raw"
output_folder = "output"
dng_files = glob.glob(os.path.join(raw_folder, "*.dng"))

check_folder_existence(output_folder)
dng_renamer(dng_files, output_folder)

