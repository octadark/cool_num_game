from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = "YOU_SHALL_NOT_PASS!"

@app.route('/', methods=['GET', 'POST'])
def juego():
    if 'numero_secreto' not in session:
        session['numero_secreto'] = random.randint(1, 100)
        session['intentos'] = 0
    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['intentos'] += 1
        if guess < session['numero_secreto']:
            mensaje = 'demasiado bajo. Intenta de nuevo.'
        elif guess > session['numero_secreto']:
            mensaje = 'demasiado alto. Intenta de nuevo'
        else:
            mensaje = f'¡Felicitaciones! Adivinaste el número en {session["intentos"]} intentos. El número era {session["numero_secreto"]}.'
            del session['numero_secreto']
    return render_template("juego.html", mensaje = mensaje) 

if __name__ == "__main__":
    app.run(debug=True)