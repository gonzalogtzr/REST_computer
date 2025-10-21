from flask import Flask, jsonify
from datetime import datetime
import locale

app = Flask(__name__)

# Opcional: mostrar los días en español (si el sistema lo soporta)
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except:
    locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

@app.route('/')
def home():
    return "✅ Servidor Flask funcionando"

@app.route('/api/dia', methods=['GET'])
def get_dia():
    ahora = datetime.now()
    dia_texto = ahora.strftime("%A %d de %B de %Y")  # Ejemplo: lunes 20 de octubre de 2025
    return jsonify({
        "fecha": ahora.strftime("%Y-%m-%d"),
        "dia": dia_texto.capitalize()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
