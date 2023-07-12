from flask import Flask
from flask import render_template, request

app = Flask(__name__, template_folder='templates')
app.app_context().push()

# Configuration settings (if any)
# app.config['KEY'] = 'value'

from application.controllers import *

if __name__ == '__main__':
    app.run(debug=True)