from flask import Flask, request,render_template
import mysql.connector
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources=r'/*')

@app.route('/userList', methods=['GET'])
def userList():
    conn = mysql.connector.connect(user='root', password='', database='test')
    cursor = conn.cursor()
    cursor.execute(r"select * from user")
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    response = {
        'users': values
    }
    print(values, '===')
    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)
