from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/admin/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    todos = Todo.query.all()  
    
    return render_template("index.html", todos = todos)



@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    """ if todo.complete == True:
        todo.complete == False
    else:                                   #burdaki 3 satir ile db tablosundaki verileri degisitirip kaydedebiliyoruz,(orm ile)
        todo.complete = True """
    
    todo.complete = not todo.complete 

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):    
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/add",methods = ["POST"])   
def addTodo():
    title = request.form.get("title")

    newTodo = Todo(title = title,complete = False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)




















#https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/ bu link ile orm yi dahil eedebiliriz. orm ile sql verilerini db ye daha kisa ve kolay sekilde ekleniyor.