import pandas as pd

stazioni = pd.read_csv('/workspace/flask/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv',sep=";")
stazioni.head()

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