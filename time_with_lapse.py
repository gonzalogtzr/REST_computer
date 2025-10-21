from flask import Flask, jsonify, render_template_string
from datetime import datetime
import locale

app = Flask(__name__)

# Configura el idioma español
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
        <title>Actualización Automática Flask</title>
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
                margin-bottom: 20px;
            }
            button:hover { background-color: #2980b9; }
            #resultado {
                font-size: 20px;
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <h2>⏱️ Actualización Automática del Día y Hora</h2>
        <button onclick="toggleUpdate()">⏯️ Iniciar / Detener</button>
        <div id="resultado">Esperando actualización...</div>

        <script>
            let intervalo = null;

            async function obtenerDia() {
                const res = await fetch('/api/dia');
                const data = await res.json();
                document.getElementById('resultado').innerText =
                    "Hoy es " + data.dia + "\\nHora: " + data.hora;
            }

            function toggleUpdate() {
                if (intervalo) {
                    clearInterval(intervalo);
                    intervalo = null;
                    document.getElementById('resultado').innerText += "\\n⏸️ Actualización detenida";
                } else {
                    obtenerDia();  // primer update inmediato
                    intervalo = setInterval(obtenerDia, 3000); // cada 3 segundos
                }
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

# --- API REST que envía fecha y hora actual ---
@app.route('/api/dia', methods=['GET'])
def get_dia():
    fecha = datetime.now()
    dia_texto = fecha.strftime("%A %d de %B de %Y").capitalize()
    hora_texto = fecha.strftime("%H:%M:%S")
    return jsonify({
        "fecha": fecha.strftime("%Y-%m-%d"),
        "dia": dia_texto,
        "hora": hora_texto
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
