from flask import Flask # Importa o flask

app = Flask(__name__fv) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): # função responsável pela página
    return "<h1>Página inicial</h1>" "<P>lalala<P>" # HTML retornado