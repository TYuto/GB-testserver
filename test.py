from flask import Flask, request, jsonify
app = Flask(__name__)

lists = []

@app.route('/')
def return_index():
    return """
    <h3>/index</h3>
    これ

    <h3>/add_blocks</h3>
    データのpost先, jsonしか受け取らない
   
    <h3>/lists</h3>
    これまでpostされたデータを表示
    
    <h3>/reset</h3>
    すべてのデータをリセット
    """


@app.route('/reset')
def reset_data():
    response = jsonify('reset all data')
    response.status_code = 200
    return response

@app.route('/lists')
def return_lists():
    return jsonify(lists)

@app.route("/add_blocks", methods=["POST"])
def add_block():
    print (request)
    lists.append(request.json)
    
    response = jsonify({'results': 'ok'})
    response.status_code = 200
    return response




if __name__ == "__main__":
    app.run(debug=True)
