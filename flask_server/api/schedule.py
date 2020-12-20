from __init__ import app

class Schedule:
    @app.route('/api/schedule', methods=['PUT'])
    def put():
        return 'shedule put', 200 
    @app.route('/api/schedule', methods=['POST'])
    def post():
        return 'shedule post', 200 
    @app.route('/api/schedule', methods=['DELETE'])
    def delete():
        return 'shedule delete', 200 
    @app.route('/api/schedule', methods=['GET'])
    def get():
        return 'shedule get', 200 



