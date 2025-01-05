from flask import Flask, render_template, render_template_string
from pegar_dados import atualizar_dados

app = Flask('__main__')

@app.route('/', methods = ['GET'])
def atualizar_dados_pagina():
    resposta = atualizar_dados()

    return render_template_string(resposta)
