from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Mi Clave'

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/invitado', methods=['POST'])
def invitado():
    session['invitado'] = int(request.form['invitado'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

