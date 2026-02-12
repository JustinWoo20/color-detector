import cv2 as c
from flask import Flask, render_template
from detector import ColorDetector

app = Flask(__name__)

@app.route('/')
def home():
    ex_img = ColorDetector(image=c.imread('static/img/colors_test.png', c.IMREAD_COLOR_RGB), n=5)
    return render_template('index.html', color_data=ex_img.color_dict)

# @app.route('/detected')
# def detected():


if __name__ == '__main__':
    app.run(debug=True)

