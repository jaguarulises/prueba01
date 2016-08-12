from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Pagina Inicial'

@app.route('/nowmypython')
def nowmypython():
    return 'NOW Python World WORKING'

@app.route('/webserver')
def webserver():
    return 'Pagina del Servidor' 

@app.route('/projects/')
def projects():
    return 'El Proyecto'

@app.route('/about')
def about():
    return 'Acerca del Proyecto'


if __name__ == '__main__':
   app.debug = True
   app.run()