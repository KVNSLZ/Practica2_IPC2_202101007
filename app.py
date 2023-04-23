from flask import jsonify, Flask, request
from flask_cors import CORS
import Pila

app = Flask(__name__)
CORS(app)

miPila = Pila.Pila()

@app.route('/postAgregar', methods=['POST'])     
def addPila():
    if request.method == 'POST':
        valorLeido = request.form['valor']
        miPila.insertar(valorLeido)
        return jsonify({"msg": "ok"})

@app.route('/postGenerarImagen', methods=['POST'])  
def agregar():
    return jsonify({"pila": str(miPila.generarDot())})

@app.route('/getImagen')  
def getPila():
    return jsonify({"pila": miPila.printPila()})

@app.route('/')  
def devolver():
    return jsonify({"msg": "Todo OK",
                    "status": 200})


if __name__ == '__main__':
    app.run(debug=True, port=3004)