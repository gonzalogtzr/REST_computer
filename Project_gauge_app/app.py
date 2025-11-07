from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variable global para almacenar el nivel
current_level = 50

@app.route('/')
def index():
    return render_template('index.html', level=current_level)

@app.route('/set_level', methods=['POST'])
def set_level():
    global current_level
    data = request.get_json()
    level = data.get('level')
    if level is not None:
        current_level = int(level)
        print(f"Nuevo nivel: {current_level}")
        return jsonify({'status': 'ok', 'level': current_level})
    return jsonify({'status': 'error', 'message': 'no level provided'}), 400

@app.route('/get_level')
def get_level():
    return jsonify({'level': current_level})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4000)
