from flask import Flask, jsonify, abort, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:ximbestnayda@localhost:3306/iot-test-db-2'
db = SQLAlchemy(app)


class Automobile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    engine = db.Column(db.Integer)
    year = db.Column(db.Integer)
    manf = db.Column(db.String(45))


@app.route('/automobiles', methods=['GET'])
def get_all_automobiles():
    automobiles = []
    all_automobiles = Automobile.query.all()
    for at in all_automobiles:
        automobile = {
            'name': at.name,
            'engine': at.engine,
            'year': at.year,
            'manf': at.manf
        }
        automobiles.append(automobile)
    db.session.commit()
    return jsonify({'automobiles': automobiles})


@app.route('/automobiles/<int:automobile_id>', methods=['GET'])
def get_automobile(automobile_id):
    at = Automobile.query.filter_by(id=automobile_id).first()
    automobile = {
        'name': at.name,
        'engine': at.engine,
        'year': at.year,
        'manf': at.manf
    }
    db.session.commit()
    return jsonify({'automobile': automobile})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/automobiles', methods=['POST'])
def add_automobile():
    # if not request.json or not 'name' in request.json:
    #     abort(400)
    new_automobile = Automobile()
    # print(new_automobile)
    new_automobile.iD = request.json['id']
    new_automobile.name = request.json['name']
    new_automobile.engine = request.json.get('engine', 0)
    new_automobile.year = request.json.get('year', 0)
    new_automobile.manf = request.json['manf']

    db.session.add(new_automobile)
    db.session.commit()
    return jsonify('Successful')



@app.route('/automobiles/<int:automobile_id>', methods=['PUT'])
def update_automobile(automobile_id):
    automobile = Automobile.query.get(automobile_id)

    automobile.name = request.json['name']
    automobile.engine = request.json.get('engine', automobile.engine)
    db.session.commit()
    return jsonify('Successful')


@app.route('/automobiles/<int:automobile_id>', methods=['DELETE'])
def delete_automobile(automobile_id):
    at = Automobile.query.filter_by(id=automobile_id).first()
    db.session.delete(at)
    db.session.commit()
    return jsonify({'result': True})



if __name__ == '__main__':
    app.run()