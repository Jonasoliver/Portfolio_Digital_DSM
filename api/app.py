from flask import Flask, render_template

app = Flask(__name__)

# Lista de trabalhos
trabalhos = [
    {
        'titulo': 'Projeto API',
        'descricao': 'O projeto realizado visa ajudar aos pais de crianças que sofrem de doença renal crônica, ajudando na informatização, como por exemplo onde há hospitais no Brasil especializados na área, quais os cuidados devem ser tomados com crianças assim, uma área de conversas, troca de mensagens entre os pais, para tirar possíveis dúvidas.',
        'imagem': '../static/api.jpeg'
    },
    {
        'titulo': 'Projeto da Arte Desenvolvimento Web',
        'descricao': 'Este projeto foi para a aprendizagem, visando a utilização do bootstrap e a capacidade de desenvolver uma arte própria em seu site, referindo-me ao front end.',
        'imagem': '../static/arte.jpeg'
    },
        {
        'titulo': 'Projeto API',
        'descricao': 'Este projeto Api foi desenvolvido utilizando React. O projeto é um site de atendimento ao cliente, com tema de correios. O site tem três tipos de acesso: Cliente, Atendente e Administrador. Possui um chat e tickets, onde os funcionarios podem ajudar os clientes com seus problemas em relação a seus produtos.',
        'imagem': '../static/Api2024.png'
    },
   
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trabalhos')
def mostrar_trabalhos():
    return render_template('trabalhos.html', trabalhos=trabalhos)

@app.route('/sobremim')
def sobre_mim():
    return render_template('sobremim.html')

if __name__ == '__main__':
    app.run(debug=True)
