# TODO: Use post requests, to create upload an image functionality
# TODO: Output a data in an easy to read format
# TODO: Use Jinja for Loop to add colors to demo

import cv2 as c
from flask import Flask, render_template
from detector import ColorDetector

app = Flask(__name__)

@app.route('/')
def home():
    ex_img = ColorDetector(image=c.imread('static/test.jpg'), n=10)
    return render_template('index.html', image=ex_img, hex_code=ex_img.final_hex,
                           percentage=ex_img.pct)

if __name__ == '__main__':
    app.run(debug=True)

