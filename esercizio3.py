from flask import Flask, render_template
app = Flask(__name__)

import random

@app.route('/', methods=['GET'])
def home():
    return render_template('index2.html')
@app.route('/frasicelebri', methods=['GET'])

def frase():
    n = random.randint(0,10)

    frasi = [{'autore':'Dietrich Bonhoeffer','Frase':'Contro la stupidità non abbiamo difese.'},
    {'autore':'Charlie Chaplin','Frase':'Un giorno senza un sorriso è un giorno perso.'},
    {'autore':'Francesco Bacone','Frase':'Sapere è potere.'},
    {'autore':'Italo Calvino','Frase':'Il divertimento è una cosa seria.'},
    {'autore':'Johann Wolfgang von Goethe','Frase':'Il dubbio cresce con la conoscenza.'},
    {'autore':'Luis Sepùlveda','Frase':'Vola solo chi osa farlo.'},
    {'autore':'Voltaire','Frase':'Chi non ha bisogno di niente non è mai povero.'},
    {'autore':'Ricky Nelson','Frase':'Le lacrime di oggi sono gli arcobaleni di domani.'},
    {'autore':'Steve Jobs','Frase':'Siate affamati, siate folli.'},
    {'autore':'Henry David Thoreau','Frase':'Le cose non cambiano; siamo noi che cambiamo.'},]

    return render_template('frasi.html', autore= frasi[n]['autore'], frase=frasi[n]['Frase'])












if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)