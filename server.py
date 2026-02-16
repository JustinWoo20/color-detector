import atexit
import cv2 as c
from flask import Flask, render_template, request
from detector import ColorDetector
import os
import shutil
import tempfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Create temp directory
TEMP_DIR = tempfile.mkdtemp(prefix='uploads_', dir='static')

def clean_dir():
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

atexit.register(clean_dir)

@app.route('/')
def home():
    ex_img = ColorDetector(image=c.imread('static/img/colors_test.png', c.IMREAD_COLOR_RGB), n=5)
    return render_template('index.html', color_data=ex_img.color_dict)

@app.route('/detected', methods=['POST'])
def detected():
    uploaded_file = request.files.get('imgFile')
    # Check and make sure there is a file
    if not uploaded_file or uploaded_file.filename == '':
        return "No file uploaded", 400
    # Temporary save image
    filename = secure_filename(uploaded_file.filename)
    filepath = os.path.join(TEMP_DIR, filename)
    uploaded_file.save(filepath)
    # Process new image
    new_img = ColorDetector(image=c.imread(filepath, c.IMREAD_COLOR_RGB),
                            n=int(request.form['num_results']))

    relative_path = os.path.relpath(filepath, 'static')
    print(relative_path)
    return render_template('detected.html', color_data=new_img.color_dict, display_img=relative_path)

if __name__ == '__main__':
    app.run(debug=True)

