from flask import Flask, render_template
app = Flask(__name__)

import random

@app.route('/', methods=['GET'])
def home():
    return render_template('index2.html')

@app.route('/meteo', methods=['GET'])
def meteo():
    n = random.randint(0,8)
    if n < 2:
        return render_template('previsioni.html', testo= 'PIOGGIA' , img = 'static/img/pioggia.jpg')
    elif 3 <= n <= 5:
        return render_template('previsioni.html', testo= 'NUVOLOSO', img = 'static/img/nuvoloso.jpg')
    else:
        return render_template('previsioni.html', testo= 'SOLE' , img = 'static/img/sole.jpg')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)