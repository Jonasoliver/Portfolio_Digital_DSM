# Bem-vindo ao meu portfólio
## Autor: Jonas Miguel de Oliveira
<p align= "center">
<img src="./src/static/eu.jpg" width= "auto" height= "250" alt= "minha foto">
</p>

## Visite o meu portfólio por este link:
https://portfolio-jonas-dsm.vercel.app/
 
## Tecnologias

As tecnologias que foram utilizadas são:
* HTML: uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. <img src="./src/static/html.png" width= "27" height= "27" alt= "html foto">
* CSS: mecanismo para adicionar estilos a uma página web, aplicado diretamente nas tags HTML ou ficar contido dentro das tags <style>. <img src="./src/static/css.png" width= "27" height= "27" alt= "css foto">
* Python:  uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. <img src="./src/static/python.png" width= "27" height= "27" alt= "css foto">
* Flask:  é um pequeno framework web escrito em Python. <img src="./src/static/flask.png" width= "32" height= "32" alt= "css foto">

## Descrição das pastas

1. mgt: pdf do figma do portfólio
2. src: código-fonte do projeto
3. static: imagens e css do projeto
4. templates: html do projeto

## Como utilizar o diretório

Como construir e executar o projeto (Windows / prompt de comandos):
1. Criar uma pasta vazia
2. Clonar o repositório com: 
```console
	git clone https://github.com/Jonasoliver/portfolio_digital_dsm.git  .
```
3. Abrir a pasta raiz
4. Com o terminal aberto na pasta raiz, digitar:
-Python -m venv venv
5. Após a criação da pasta venv, digitar:
- .\venv\Scripts\activate
6. Já dentro da pasta venv digitar o código:
- pip install flask
7. Geralmente o arquivo requirements.txt vem automaticamente após instaalar o Flask, caso isso não aconteça execute o passo 8
8. Digitar no terminal:
 - pip freeze > requirements.txt
9. Após executar estes passos digitar:
- cd ./src
11. Já dentro da pasta src, onde se encontra o app.py, digitar:
- flask run ou python app.py
12. Acessar o link segurando a tecla Ctrl e clicando com o botão esquerdo do mouse
## Como iniciar o seu projeto

1. Ter um computador.
2. Utilizar o terminal ou caso prefira, instalar uma ferramenta de desenvolvimento web. Aperte [aqui](https://www.hostinger.com.br/tutoriais/ferramentas-de-desenvolvimento-web) para acessar um link onde exibe-se algumas ferramentas desse tipo.
## Como subir o portfolio no vercel
1. Baixe em seu compudador o node, caso ainda não o possua, baixe-o aqui [node.js](https://nodejs.org/en)
2. Na pasta raiz do projeto, abra o terminal  (npm install -g vercel)
3. Após a instalação digite no terminal (vercel), dê um nome para a pasta e suba para o vercel.
(Validação professor FGMC - 1DSM - 2023-02)
