from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import json

# create flask app
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'todo-db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'p@ssw0rd123'
app.config['MYSQL_DB'] = 'todoapp'
mysql = MySQL(app)

# index route, shows index.html view
@app.route('/')
def index():
    return 'Flask Dockerized'

@app.route('/mysql')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)
# endpoint for storing todo item
# @app.route('/add-todo', methods = ['POST'])
# def addTodo():
#     data = json.loads(request.data) # load JSON data from request
#     pusher.trigger('todo', 'item-added', data) # trigger `item-added` event on `todo` channel
#     return jsonify(data)

# # endpoint for deleting todo item
# @app.route('/remove-todo/<item_id>')
# def removeTodo(item_id):
#     data = {'id': item_id }
#     pusher.trigger('todo', 'item-removed', data)
#     return jsonify(data)

# # endpoint for updating todo item
# @app.route('/update-todo/<item_id>', methods = ['POST'])
# def updateTodo(item_id):
#     data = {
#     'id': item_id,
#     'completed': json.loads(request.data).get('completed', 0)
#     }
#     pusher.trigger('todo', 'item-updated', data)
#     return jsonify(data)

# run Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8082')