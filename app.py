from flask import Flask, jsonify, request

# Criar uma instancia do flask
app = Flask(__name__)

# Dados
filmes = [
  {'id': 1, 'titulo': 'A proposta', 'descricao': 'Uma editora de livros canadense que força seu assistente a se casar com ela para evitar a deportação, e eles acabam se apaixonando.'},
  {'id': 2, 'titulo': 'Dez Coisas que Odeio em Voce', 'descricao': 'Um garoto é pago para namorar a irmã rebelde de uma garota popular, mas acaba se apaixonando por ela de verdade.'},
  {'id': 3, 'titulo': 'Como Perder um Homem em Dez Dias', 'descricao': 'Uma jornalista tenta afastar um homem em 10 dias como parte de um artigo, sem saber que ele faz parte de uma aposta para conquistar uma mulher.'}
]

# Rota raiz
@app.route('/')
def raiz():
  return 'Bem Vindo ao Catálogo de Filmes!'


# Rota para listar todos os filmes
@app.route('/filmes', methods=['GET'])
def get_filmes():
  return jsonify(filmes)


app.run(port=5000, host='localhost', debug=True)
