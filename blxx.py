from crypt import methods
from enum import unique
from flask import Flask,redirect, render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# todoData = []
#find the current app path (directory name)
project_dir = os.path.dirname(os.path.abspath(__file__))

#creating the database file
database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))

#connecting the database file(todo.db) to the SQLAlchemy dependencies
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

class Todo(db.Model):
      # id = db.Column( db. Integer, unique=True, nullable=False, primary_key=True)
      todo = db.Column(db.String(30), unique=False, nullable=False, primary_key=True)

      def __repr__(self):
          return f"Todo: {self.todo}"

@app.route("/")
def home():
      return render_template('index.html',todos=todoData)


@app.route('/create_todo', methods=["post"]) 
def create_todo(): 
  new_todo = request.form.get("new_todo")
  todoData.append(new_todo)
  print (todoData)
  return redirect(url_for('home'))

@app.route('/delete/<todo_item>', )
def delete(todo_item):
      todoData.remove(todo_item)
      return redirect(url_for('home'))

index_to_update=''
@app.route('/update/<todo_item>', methods = ['GET', 'post'])
def update(todo_item):


      index =todoData.index(todo_item)

      global index_to_update
      index_to_update = index
      return render_template('update.html', todo_item = todo_item)

@app.route('/update_item',methods = ['post'])
def update_item():

        if request.method =='POST':

              new_item = request.form.get('new_item')
              todoData[index_to_update] = new_item

              return redirect(url_for('home'))

  
if __name__ == "__main__":
    app.run(debug=True)
    