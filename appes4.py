#si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull andamento dell epidemia di covid nel nostro paese a partire da i dati prtesenti nel file 
#https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv
# l utente sceglie la regione da un elenco (menu a tendina), clicca su un bottone e il sito deve visualizzare una tabella contente le informazioni relative a quella regione
#i dati da inserire nel menu a tendina devono essere caricati automaticamente dalla pagina
#https://github.com/italia/covid19-opendata-vaccini/blob/master/dati/platea-dose-addizionale-booster.csv

from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv')

@app.route('/', methods=['GET'])
def home():
    return render_template('formes4.html')

@app.route('/data', methods=['GET'])
def data():
  regione = request.args['Regioni']
  df_result = df[df['nome_area']== regione]
  return render_template('risultatoes4.html',tables=[df_result.to_html()], titles=[''])
















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)