from flask import Flask, render_template, request, redirect, jsonify, session
from flask_cors import CORS, cross_origin
from datetime import datetime, timedelta
import sys
sys.path.append("../cheer")
import settings

app = Flask(__name__)
app.secret_key = settings.secret_key
app.permanent_session_lifetime = timedelta(days=1)
CORS(app, support_credentials=True)


@app.route('/user', methods=['GET'])
# @cross_origin(supports_credentials=True)
def index():
    json_data = request.get_json()
    user_id = json_data.get('user_id')
    password = json_data.get('password')
    if user_id == 'masashi07':
        if password == 'masashi':
            return {
                'user': 'masashi07',
                'mail': 'masashi07@gmail.com'
            }, 200
        else:
            return {}, 400
    else:
        return {}, 400

