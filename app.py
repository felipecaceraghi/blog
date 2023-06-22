from flask import Flask, render_template
import time as t 



app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/user/<name>') ## Rota onde tudo que for envolvidos em tags '<>' é usado como parametro pra importar dados externos
def user(name):
	return render_template('user.html', name=name)

@app.errorhandler(404) ## Exibir páginas de erro HTTP personalizadas
def erro404(e):
	return render_template('404.html'), 404
	

if __name__ == '__main__':
	app.run(debug=True)
