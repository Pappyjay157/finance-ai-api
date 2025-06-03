from flask import request, jsonify
import pandas as pd

def register_routes(app):
    @app.route('/')
    def hello():
        return {'message': 'Finance AI API running 🚀'}

    @app.route('/upload', methods=['POST'])
    def upload_csv():
        file = request.files['file']
        df = pd.read_csv(file)
        return jsonify(df.head().to_dict(orient='records'))
