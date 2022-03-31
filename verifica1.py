#Si vuole realizzare un server web che permetta di avere informazioni sulle stazioni radio a Milano. In particolare l’utente deve poter:
#Avere il numero di stazioni per ogni municipio (in ordine crescente sul numero del municipio) e il grafico corrispondente
#Avere un elenco di tutte le stazioni radio che si trovano in un certo quartiere. L’utente inserisce il nome del quartiere (anche solo una parte del nome) 
#e il sito risponde con l’elenco ordinato in ordine alfabetico delle stazioni radio presenti in quel quartiere
#Avere la posizione in città di una stazione radio. L’utente sceglie il nome della stazione da un menù a tendina (i nomi delle stazioni devono essere ordinati in ordine 
# alfabetico), clicca su un bottone e ottiene la mappa del quartiere che contiene la stazione radio, con un pallino nero sulla posizione della stazione radio
#Per richiamare i vari servizi del sito web, l’utente deve selezionare nella homepage il radiobutton corrispondente al servizio richiesto e cliccare su un bottone.
#Scrivere nella prima facciata del foglio protocollo il server flask, nella seconda i file html relativi alla home page e al primo esercizio, nella terza facciata i file html 
# relativi al secondo esercizio e nella quarta facciata i file html relativi al terzo esercizio.   
#È possibile utilizzare solo il materiale presente sul proprio github. Consegnare il cellulare prima della verifica. Al termine, riprendere il cellulare, 
#fare la foto alla propria verifica e consegnarla.


from flask import Flask, render_template, request, Response
app = Flask(__name__)

import io
import pandas as pd
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


stazioni = pd.read_csv('/workspace/flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv',sep=";")


@app.route("/", methods=["GET"])
def home():
    #numero stazioni per ogni municipio
    return render_template("home.html")

@app.route("/numero", methods=["GET"])
def numero():
    global risultato
    risultato = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    return render_template("elenco.html",risultato=risultato.to_html)


@app.route("/grafico", methods=["GET"])
def grafico():

    #visualizza grafico
    fig, ax = plt.subplots(figsize = (6,4))

    x = risultato.MUNICIPIO
    y = risultato.OPERATORE

    ax.bar(x, y, color = "#304C89")
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

    return render_template("home.html")

@app.route("/selezione", methods=["GET"])
def grafico():














if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3246, debug=True)