from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_db.sqlite3'
db = SQLAlchemy(app)

# モデル作成
class Reqs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jsontext = db.Column(db.String(124))

    def __init__(self, jsontext):
        self.jsontext = jsontext

    def __repr__(self):
        return '<User %r>' % self.username



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
    db.session.query(Reqs).delete()
    db.session.commit()

    response = jsonify('reset all data')
    response.status_code = 200
    return response

@app.route('/lists')
def return_lists():
    return jsonify(db.session.query(Reqs.jsontext).all())

@app.route("/add_blocks", methods=["POST"])
def add_block():
    a = Reqs(str(request.json))
    db.session.add(a)
    db.session.commit()
    
    response = jsonify({'results': 'ok'})
    response.status_code = 200
    return response




if __name__ == "__main__":
    app.run(debug=True)
