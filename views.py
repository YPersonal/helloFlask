from helloflask import app
from forms import LoginForm
from flask import  request,render_template,session,jsonify,json,redirect
from manage import save,query_all,query_filter,removeItem,updateUserinfo



@app.route('/allinfo',methods=['GET'])
def getinfo():
    users = query_all()#query_filter("v-daoz")#query_all()
    #return query_all()
    return jsonify({'users':users})

@app.route('/remove/<id>', methods=['GET'])
def removeUser(id):
    removeItem(id)
    return render_template('index.html')

@app.route('/updateUser/<id>',methods=['POST'])
def editUser(id):
    name = request.form['username']
    desc =request.form['description']
    updateUserinfo(id,name,desc)
    # return render_template('index.html')
    return redirect('/')
@app.route('/')
def home():
    return render_template('index.html' )


@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET','POST'])
def login():
    myForm = LoginForm(request.form)
    if request.method=="POST":
        # username = request.form["username"]
        # password = request.form["password"]
        if myForm.username.data:
            session['username']=myForm.username.data
            session['description'] = myForm.description.data
            save()
            # user = User(myForm.username.data, myForm.description.data)
            # db.session.add(user)
            # db.session.commit()
            return redirect('/')
        # if myForm.username.data =="zhang" and myForm.description.data =="123456":
        #     return redirect("http://www.baidu.com")
        else:
            message = "login failed"
            return render_template('register.html' , message=message ,form = myForm)
    return render_template('register.html',form= myForm)

app.run(port=8080)