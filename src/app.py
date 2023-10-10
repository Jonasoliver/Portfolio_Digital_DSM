from flask import Flask
from flask  import render_template  

app = Flask('__name__')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trabalhos')
def quem():
    return render_template('trabalhos.html')

@app.route('/sobremim')
def contato():
    return render_template('sobremim.html')

if __name__ == '__main__':
    app.run(debug=True)