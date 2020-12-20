from __init__ import app

class Schedule:
    @app.route('/api/schedule/get', methods=['GET'])
    def get_schedule():
        return 'shedule', 200 



