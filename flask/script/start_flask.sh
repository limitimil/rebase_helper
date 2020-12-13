SCRIPT_DIR="$( cd "$( dirname ${BASH_SOURCE[0]} )" >/dev/null 2>&1 && pwd )"
export FLASK_APP=main.py
export FLASK_DEBUG=1
export PYTHONPATH=$SCRIPT_DIR/../../:$SCRIPT_DIR/../
