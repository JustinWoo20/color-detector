# TODO 3: Upload an image functionality
# TODO 5: Output a data in an easy to read format
# TODO 6: Use render template to add colors to website

import cv2 as c
from flask import Flask, render_template
from detector import ColorDetector

app = Flask(__name__)

@app.route('/')
def home():
    ex_img = ColorDetector(image=c.imread('static/test.jpg'), n=10)
    return render_template('index.html', image=ex_img)

if __name__ == '__main__':
    app.run(debug=True)

