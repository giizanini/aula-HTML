from flask import (Flask, request) # Importa o flask
app = Flask("_name_") # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página
    return "<h1>Página inicial</h1>" "<P>lalala<P>" # HTML retornado

@app.route("/area")
def area():
  altura = float (request.args.get('a'))
  largura = float(request.args.get('l'))
  return f""" 
<h1> A área informada> L={largura}* A={altura} Area={largura*altura}</h1>"""

@app.route("/par_ou_impar", methods=('GET',))
def par_ou_impar():
  numero = float(request.args.get('n'))
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome", methods=('GET',))
def nomesobrenome():
  nome = request.args.get('nome')
  sobrenome = request.args.get('sobrenome')
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""