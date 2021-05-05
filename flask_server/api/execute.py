from __init__ import app

from flask import jsonify
from flask import request

from models.repositoryConfig import RepositoryConfig
from rebase_helper import RebaseHandler

class Execute:
    @app.route('/api/rebase/execute', methods=['POST'])
    def api_execute():
        ## TODO: model transform should defined as model for readability.
        request_payload = {}
        request_payload['branches'] = [ request.json['branch'] ]
        request_payload['repository_url'] = request.json['url']

        rc = [ RepositoryConfig(request_payload) ] 
        rh = RebaseHandler()
        rh.run_for_each_repo(rc)
        rh.remove_all_workspace()
        return 'Done', 200 



