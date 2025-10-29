# TODO 1: Set up flask server
# TODO 2: Use bootstrap to customize layout
# TODO 3: Upload an image functionality
# TODO 4: Use Numpy to detect colors
# TODO 5: Output a data in an easy to read formate

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
