from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='/')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/api/messages/chats', methods=['GET'])
def get_chats():
    # Por enquanto retorna uma lista vazia
    # Você pode implementar a lógica real de busca das conversas aqui
    return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


