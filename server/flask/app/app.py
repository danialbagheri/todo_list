from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS

# create flask app
app = Flask(__name__)
# database connection
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:p@ssw0rd123@todo-db/todoapp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/DanialBagheri/Dropbox/Sites/todo-list/server/app/todo.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(15), unique=False, nullable=False)
    todo_id = db.column(db.Integers, db.ForeignKey('person.id'),nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    req_by = db.relationship('User', backref="todo", lazy=True)
    project_number = db.Column(db.String(80), unique=True, nullable=True)
    position_number = db.Column(db.String(80), unique=True, nullable=True)
    department = db.Column(db.String(80), unique=True, nullable=False)
    delivery_date= db.Column(db.String(120), unique=False, nullable=False)
    delivery_date= db.Column(db.String(120), unique=False, nullable=False)
    meeting = db.Column(db.String(15), unique=False, nullable=False)
    project_detail = db.Column(db.String(15), unique=False, nullable=False)
    amendment = db.Column(db.Boolean(), unique=False, nullable=False)
    completion_date = db.Column(db.String(120), unique=False, nullable=False)
    approve = db.Column(db.Boolean(), unique=False, nullable=False)
    assigned_to = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.project_number

@app.route('/')
def index():
    testUser = User.query.all()
    print(testUser)
    users = ""
    for i in testUser:
        users += i.username
    print(users)

    return 'Users: ' + users

@app.route('/add-user', methods = ['POST'])
def addUser():
    result={"response":"request submitted"}
    data = {
        'username': json.loads(request.data).get('username'),
        'email': json.loads(request.data).get('email'),
        'password': json.loads(request.data).get('password')
    }
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    
    result=new_user.serialize()

    # testUser = User.query.filter_by(username='admin').first()
    return jsonify(result)
# endpoint for storing todo item
# @app.route('/add-todo', methods = ['POST'])
# @app.route('/update-todo/<item_id>', methods = ['POST'])
# def updateTodo(item_id):
#     data = {
#     'completed': json.loads(request.data).get('completed', 0)
#     }
#     pusher.trigger('todo', 'item-updated', data)
#     return jsonify(data)
# def addTodo():
    


# # endpoint for deleting todo item
# @app.route('/remove-todo/<item_id>')
# def removeTodo(item_id):
#     data = {'id': item_id }
#     pusher.trigger('todo', 'item-removed', data)
#     return jsonify(data)

# # endpoint for updating todo item

# run Flask app in debug mode
if __name__ == '__main__':
    # Table needs to be created on the first time it's run
    # Try to create table, if it fails, no biggie, it probably already exists
    try:
        db.create_all()
        db.session.commit()
    except:
        #table probably exists
        pass
    app.run(debug=True,host='0.0.0.0',port='8082')