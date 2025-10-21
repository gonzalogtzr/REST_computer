from flask import Flask, jsonify, render_template_string
from datetime import datetime
import locale

app = Flask(__name__)

# Configura idioma español (si está disponible)
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except:
    locale.setlocale(locale.LC_TIME, 'es_MX.UTF-8')

# --- Página principal ---
@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mostrar Día Actual</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 50px; }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
            button:hover { background-color: #2980b9; }
            #resultado {
                margin-top: 20px;
                font-size: 18px;
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <h2>🕓 Consultar el día actual</h2>
        <button onclick="mostrarDia()">Mostrar Día</button>
        <div id="resultado"></div>

        <script>
            async function mostrarDia() {
                const res = await fetch('/api/dia');
                const data = await res.json();
                document.getElementById('resultado').innerText = 
                    "Hoy es " + data.dia;
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

# --- API REST para obtener la fecha ---
@app.route('/api/dia', methods=['GET'])
def get_dia():
    ahora = datetime.now()
    dia_texto = ahora.strftime("%A %d de %B de %Y").capitalize()
    return jsonify({
        "fecha": ahora.strftime("%Y-%m-%d"),
        "dia": dia_texto
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
