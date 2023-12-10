from flask import Flask, render_template, request
import tensorflow as tf

app = Flask(__name__)


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2.0
    area = tf.sqrt(s * (s - a)*(s - b)*(s - c))
    return area.numpy()


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['side_a'])
    b = float(request.form['side_b'])
    c = float(request.form['side_c'])

    area = area_of_triangle(a, b, c)

    return render_template('result.html', area=area_of_triangle(a, b, c))


if __name__ == '__main__':
    app.run(debug=True)
