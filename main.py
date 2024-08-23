
from flask import Flask, jsonify, make_response, request
# importa o banco de dados
from bd import Carros


#Instanciar o modulo Flask na nossa variavel app
app = Flask('carros')

#PRIMEIRO METODO - VISULAIZAR DADOS(GET)
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros


#PRIMEIRO METODO II - VISUALIZAR DADOS POR ID (GET / ID)

@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)
        

    
#SEGUNDO METODO - CRIAR NOVOS DADOS (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso',
                carro=carro
                )
    )


    
#TERCEIRO METODO - EDITAR DADOS (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])
        

#QUARTO METODO - DELETAR DADOS (DELETE)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro():
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({'mensagem': 'Carro excluido com sucesso'})





app.run(port=5000, host='localhost', debug=True)
