from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O senhor dos Anéis - A sociedade do Anel',
        'autor': 'J.Rick King'

    },
    {
        'id': 2,
        'título': 'O senhor dos Anéis - A B  A W',
        'autor': 'J. BURGUER King'

    },
    {
        'id': 3,
        'título': 'O senhor dos Anéis W- A sociedade W',
        'autor': 'J.R King'

    },
]

# CONSULTAR (TODOS)

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# CONSULTAR ID
# <int:id> = número inteiro + id

@app.route('/livros/<int:id>',methods=['GET'])
def obterlivroporid(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar Livro
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Incluir novo Livro
# POST = CRIAR

@app.route('/livros/',methods=['POST'])
def incluirlivro():
    novolivro = request.get_json()
    livros.append(novolivro)

# Excluir 

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

app.run(port=5000,host='localhost',debug=True)