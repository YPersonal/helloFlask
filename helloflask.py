from flask import Flask,request,render_template,redirect,session
from  forms import LoginForm
from flask.ext.sqlalchemy import SQLAlchemy
#from manage import save



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="mysql://root:Test1234@localhost:3306/helloflask"
app.config['SECRET_KEY'] = '123456'
db = SQLAlchemy(app)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route("/", methods=['GET','POST'])
# def login():
#     myForm = LoginForm(request.form)
#     if request.method=="POST":
#         # username = request.form["username"]
#         # password = request.form["password"]
#         if myForm.username.data:
#             session['username']=myForm.username.data
#             session['description'] = myForm.description.data
#             save()
#             # user = User(myForm.username.data, myForm.description.data)
#             # db.session.add(user)
#             # db.session.commit()
#             return render_template('index.html', form=myForm)
#         # if myForm.username.data =="zhang" and myForm.description.data =="123456":
#         #     return redirect("http://www.baidu.com")
#         else:
#             message = "login failed"
#             return render_template('index.html' , message=message ,form = myForm)
#     return render_template('index.html',form= myForm)

# @app.route("/", methods=['GET','POST'])
# def login():
#     myForm = LoginForm(request.form)
#     if request.method=="POST":
#         # username = request.form["username"]
#         # password = request.form["password"]
#         if myForm.username.data:
#             #session['username']=myForm.username.data
#             # session['description'] = myForm.description.data
#             # user = User(myForm.username.data, myForm.description.data)
#             # db.session.add(user)
#             # db.session.commit()
#             return render_template('index.html', form=myForm)
#         # if myForm.username.data =="zhang" and myForm.description.data =="123456":
#         #     return redirect("http://www.baidu.com")
#         else:
#             message = "login failed"
#             return render_template('index.html' , message=message ,form = myForm)
#     return render_template('index.html',form= myForm)
if __name__ == '__main__':
    app.run(port=8080)

