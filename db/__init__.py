from tinydb import TinyDB
from tinydb import Query

DB = TinyDB('./db.json')
TASK = DB.table('task')
