from flask import Flask, jsonify, request, abort
from .models import SubmitData
from flask import Flask
from .urls import bp

app = Flask(__name__)

@app.route('/submitData/', methods=['GET', 'POST'])
def submit_data_list_create():
    if request.method == 'GET':
        submit_data_list = SubmitData.query.all()
        return jsonify([sd.to_dict() for sd in submit_data_list]), 200
    elif request.method == 'POST':
        data = request.get_json()
        submit_data = SubmitData(**data)
        submit_data.save()
        return jsonify(submit_data.to_dict()), 201

@app.route('/submitData/<int:pk>/', methods=['GET', 'PUT', 'DELETE'])
def submit_data_detail(pk):
    submit_data = SubmitData.query.get_or_404(pk)
    if request.method == 'GET':
        return jsonify(submit_data.to_dict()), 200
    elif request.method == 'PUT':
        data = request.get_json()
        submit_data.update(**data)
        return jsonify(submit_data.to_dict()), 200
    elif request.method == 'DELETE':
        submit_data.delete()
        return '', 204

app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/api')

app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/api')
app.register_blueprint(swagger_bp, url_prefix='/api/docs')

if __name__ == '__main__':
    app.run(debug=True)