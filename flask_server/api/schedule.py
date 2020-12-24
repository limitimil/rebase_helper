from __init__ import app
from db import TASK

from flask import jsonify
from flask import request

from models.repositoryConfig import RepositoryConfig
from rebase_helper import RebaseHandler

class Schedule:

    def _pop_id(payload):
        if 'id' in payload:
            payload.pop('id')
        return payload

    @app.route('/api/schedule/task/<doc_id>', methods=['POST'])
    @app.route('/api/schedule/task', methods=['POST'], defaults={'doc_id': None})
    def post(doc_id):
        payload = request.json
        payload = Schedule._pop_id(payload)
        if not doc_id:
            result = TASK.insert(payload)
        else:
            result = TASK.update(payload, doc_ids=[int(doc_id)])
        return f'shedule put {result}', 200 
    @app.route('/api/schedule/task/<doc_id>', methods=['DELETE'])
    def delete(doc_id):
        result = TASK.remove(doc_ids=[int(doc_id)])
        return f'shedule delete {result}', 200 
    @app.route('/api/schedule/all_task', methods=['GET'])
    def get():
        res = TASK.all()
        for r in res:
            r['id']=r.doc_id
        return jsonify(res), 200 

    @app.route('/api/schedule/execute', methods=['POST'])
    def execute_schedule():
        rc = map( lambda k: RepositoryConfig(k), TASK.all())
        rh = RebaseHandler()
        rh.run_for_each_repo(rc)
        rh.remove_all_workspace()
        return 'Done', 200 


