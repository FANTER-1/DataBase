from flask import Flask
from .views import submit_data
from .database import close_db

app = Flask(__name__)

app.add_url_rule('/submitData', 'submit_data', submit_data, methods=['POST'])

app.teardown_appcontext(close_db)

if __name__ == '__main__':
    app.run(debug=True)
