from flask import Flask

# Toda classe começa com letra Maisc.
# variável mínu.
#
#app é um objeto da classe Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Estilo do rei Barbearia"

@app.route('/raposo')
def mostrar_raposo():
    return "oi"

@app.route('/novofuncionario')
def novofuncionario():
    return "Essa é a pagina dos funcionários"

@app.route('/novocliente')
def novocliente():
    return "Essa é a pagina dos novos clientes cadastrados!"

@app.route('/novoservico')
def novoservico():
    return "Essa é a pagina de definição dos novos serviços implementados!"

@app.route('/novoagendamento')
def novoagendamento():
    return "Essa é a pagina organiozação da agenda!"

@app.route('/login')
def login():
    return "Login: Nome e senha!"

@app.route('/logout')
def logout():
    return "Encerrar a sessão!"

##salao = EstiloDoRei(__name__)

 

app.run(debug=True)



