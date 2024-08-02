from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    if request.method == 'POST':
        data = request.get_json()
        response = {
            'Status': data.get('Status'),
            'User ID': data.get('User ID'),
            'College Email ID': data.get('College Email ID'),
            'College Roll Number': data.get('College Roll Number'),
            'Array for numbers': data.get('Array for numbers'),
            'Array for alphabets': data.get('Array for alphabets'),
        }
        return jsonify(response)
    elif request.method == 'GET':
        return jsonify({'operation_code': '123456'})

if __name__ == '__main__':
    app.run(debug=True)
