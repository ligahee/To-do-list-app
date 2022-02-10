from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///D:\\12780\\todolist\\test.db'

db= SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list= db.Column(db.String(255))
    state = db.Column(db.Boolean)
    date= db.Column(db.DateTime)

db.create_all()


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task= Task(list=request.form['Todo'], state=False)
    db.session.add(task)
    db.session.commit()

    return redirect(url_for('index'))
@app.route('/complete/<oid>')
def complete(oid):
    task = Task.query.get(int(oid))
    task.state=True
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete')
def delete( ):
    Task.query.filter(Task.state==True).delete()
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
    

