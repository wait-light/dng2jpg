import os
import re
import rawpy
import imageio
from flask import Flask, request, send_from_directory, jsonify, render_template

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'dng', 'raw', 'nef', 'cr2', 'arw'}  # 可根据需求添加更多格式

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_folder_existence(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def dng_name_clear(file_name):
    return re.sub(r"\.dng$", "", file_name, flags=re.IGNORECASE)

def rename_dng(dng_file, output_folder):
    try:
        file_name = os.path.basename(dng_file)
        cleaned_file_name = dng_name_clear(file_name)

        # Load and process the RAW file with optimized settings
        with rawpy.imread(dng_file) as raw:
            rgb = raw.postprocess(
                no_auto_bright=True,  # Disable automatic brightness adjustment
                use_camera_wb=True,   # Use camera white balance
                bright=1.0,           # Keep brightness to default
                gamma=(2.2, 4.5),     # Apply gamma correction
                dcb_iterations=1,     # DCB interpolation algorithm iterations
                dcb_enhance=True      # Enable DCB enhance
            )

        # Convert the processed image to an array
        img = imageio.core.util.Array(rgb)
        jpeg_path = os.path.join(output_folder, f"{cleaned_file_name}.jpg")
        
        # Save the image with high quality setting
        imageio.imwrite(jpeg_path, img, quality=95)
        
        print(f"Successfully processed and saved {jpeg_path}")
        return jpeg_path
    except Exception as e:
        print(f"Error processing {dng_file}: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        check_folder_existence(app.config['UPLOAD_FOLDER'])
        check_folder_existence(app.config['OUTPUT_FOLDER'])
        
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Convert the uploaded file
        jpeg_path = rename_dng(filepath, app.config['OUTPUT_FOLDER'])
        
        if jpeg_path:
            return jsonify({"download_link": f"/download/{os.path.basename(jpeg_path)}"}), 200
        else:
            return jsonify({"error": "Failed to process the file"}), 500
    else:
        return jsonify({"error": "Invalid file format"}), 400

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

