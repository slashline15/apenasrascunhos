from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('charada.html')
def index():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Charada</title>
        </head>
        <body>
            <h2>Resolva a Charada!</h2>
            <form id="charadaForm">
                <label for="resposta">Insira sua resposta:</label>
                <input type="text" id="resposta" name="resposta">
                <button type="submit">Enviar Resposta</button>
            </form>
            <script>
                document.getElementById('charadaForm').onsubmit = async function(e) {
                    e.preventDefault();
                    const resposta = document.getElementById('resposta').value;
                    const response = await fetch('/enviar-resposta', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({resposta: resposta})
                    });

                    if (response.ok) {
                        alert('Resposta enviada com sucesso!');
                    } else {
                        alert('Erro ao enviar resposta.');
                    }
                }
            </script>
        </body>
        </html>
    '''

# Endpoint para processar a resposta
@app.route('/enviar-resposta', methods=['POST'])
def receber_resposta():
    dados = request.json
    resposta = dados.get('resposta')
    print(f"Resposta recebida: {resposta}")
    return jsonify({'mensagem': 'Resposta recebida com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
