from flask import Flask, render_template,request
app = Flask(__name__)
import pandas as pd


@app.route('/', methods=['GET'])
def home():
    return render_template('squadraHome.html')

@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('inserisci.html')

@app.route('/dati', methods=['GET'])
def dati():
    # inserimento dei dati nel file csv
    # lettura dei dati dal form html 
    squadra = request.args['Nome']
    anno = request.args['Anno']
    citta = request.args['Citta']
    # lettura dei dati daal file nel dataframe
    df1 = pd.read_csv('/workspace/flask/templates/dati.csv')
    # aggiungiamo i nuovi dati nel dataframe 
    nuovi_dati = {'squadra':squadra,'anno':anno,'citta':citta}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    # salviamo il dataframe sul file dati.csv
    df1.to_csv('/workspace/flask/templates/dati.csv', index=False)
    return render_template('risultatoes5.html',tables=[df1.to_html()], titles=[''])

@app.route("/ricerca", methods=["GET"])
def ricerca():
    return render_template("ricerca.html")

@app.route("/dataRicerca", methods=["GET"])
def datiRic():
    scelta = request.args["Scelta"]
    cerca = request.args["Ricerca"]
    df = pd.read_csv("/workspace/flask/templates/dati.csv")
    df_result = df[df[scelta] == cerca]
    return df_result.to_html()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)