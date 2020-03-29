from flask_frozen import Freezer
from main import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze(host='0.0.0.0', port=8080, debug=True)