from flask import Flask, render_template

app = Flask(__name__)

@app.route('/templates/')
def templates():
    users = [('Daniel',19),('Jonathan',19),('Katherine',19) ]
    return render_template('ejercicio.html', usuarios=users)

if __name__ == '__Main__':
    app.run()
