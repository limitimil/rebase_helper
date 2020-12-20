from __init__ import app
from db import TASK

from flask import jsonify
from flask import request

# hack
from config import config
from db_models.repositoryConfig import RepositoryConfig

class Schedule:
    @app.route('/api/schedule/<doc_id>', methods=['POST'])
    @app.route('/api/schedule', methods=['POST'], defaults={'doc_id': None})
    def post(doc_id):
        payload = request.json if request.json else config[0]
        if not doc_id:
            result = TASK.insert(payload)
        else:
            result = TASK.update(payload, doc_ids=[int(doc_id)])
        return f'shedule put {result}', 200 
    @app.route('/api/schedule', methods=['DELETE'])
    def delete():
        return 'shedule delete', 200 
    @app.route('/api/schedule', methods=['GET'])
    def get():
        res = TASK.all()
        return jsonify(res), 200 



