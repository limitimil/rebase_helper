# -*- coding: utf-8 -*-
from flask import jsonify
from flask import request
from flask import send_from_directory
from flask import make_response
from flask import current_app

from models.repositoryConfig import RepositoryConfig
from rebase_helper import RebaseHandler

from werkzeug.exceptions import HTTPException
import os
import logging
import logging.config

from __init__ import app
import views 

_PATH = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.join(_PATH, 'logging.ini')
DEFAULT_LOG_CONFIG = os.path.abspath(_PATH)

logging.config.fileConfig(DEFAULT_LOG_CONFIG)
file_logger = logging.getLogger('flask')


@app.route('/rebase/execute', methods=['POST'])
def execute():
    request_payload = request.form.to_dict()
    request_payload['branches'] = [ request.form['branch'] ]

    rc = [ RepositoryConfig(request_payload) ] 
    rh = RebaseHandler()
    rh.run_for_each_repo(rc)
    rh.remove_all_workspace()
    return 'Done', 200 

@app.route('/helloworld', methods=['GET'])
def helloworld():
    return 'helloworld', 200

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    file_logger.error('%s', str(e))
    return jsonify(error=str(e)), code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9007)
