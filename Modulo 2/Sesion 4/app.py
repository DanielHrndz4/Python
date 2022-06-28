from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return '<h1>Hola Universo 700000</h1>' 
@app.route('/hola/<nombre>')
@app.route('/hola/')
def saludar(nombre=""):
    return f'Hola {nombre}'

@app.route('/mi-primer-template/<name>/<last_name>')
def mi_primer_template(name, last_name):
    users = ['daniel', 'jonathan', 'katherine', 'lissete']
    return render_template('mi-primer-template.html', nombre=name, apellido=last_name, usuarios=users)

if __name__ == '__Main__':
    app.run()