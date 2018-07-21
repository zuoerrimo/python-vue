from flask import Flask, request,render_template
import mysql.connector
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources=r'/*')

@app.route('/modifyUser/<id>', methods=['POST'])
def modifyUser(id):
    print(request, '===request')
    username = request.form['username']
    conn = mysql.connector.connect(user='root', password='', database='test')
    cursor = conn.cursor()
    cursor.execute('update user set name = %s where id = %s', (username, int(id),))
    print('rowcount=', cursor.rowcount)
    conn.commit()
    cursor.close()
    return userList()

@app.route('/delUser/<id>', methods=['GET'])
def delUser(id):
    print(id, '===id')
    conn = mysql.connector.connect(user='root', password='', database='test')
    cursor = conn.cursor()
    cursor.execute('delete from user where id = %s', (int(id),))
    print('rowcount=', cursor.rowcount)
    conn.commit()
    cursor.close()
    return userList()

@app.route('/addUser', methods=['POST'])
def addUser():
    conn = mysql.connector.connect(user='root', password='', database='test')
    cursor = conn.cursor()
    id = request.form['id']
    username = request.form['name']
    cursor.execute('insert into user (id, name) values (%s, %s)', [id, username])
    print('rowcount=', cursor.rowcount)
    conn.commit()
    cursor.close()
    return userList()

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
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
