from flask import Flask, render_template
app = Flask(__name__)

from datetime import datetime

@app.route('/', methods=['GET'])
def home():
    return render_template('index2.html')
@app.route('/quantomanca', methods=['GET'])
def quantomanca():
    quantomanca = datetime(2022,6,15) - datetime.today()
    return render_template('manca.html',giorni=quantomanca)
    


















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)