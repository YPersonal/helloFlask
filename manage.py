#encoding =utf-8
from flask import session
from flask_script import Manager
from helloflask import app
from helloflask import db
from models import User

manager = Manager(app)
@manager.command
def save():
    # user = User('name','desc')
    # user.save();
    name = session.get('username')
    desc = session.get('description')
    user =User(name,desc)
    db.session.add(user)
    db.session.commit()

@manager.command
def query_all():
    #users = User.query_all()
    users= User.query.all()
    urs=[]
    for u in users:
        ur={"id":u.id,"name":u.name,"description":u.description}
        urs.append(ur)
    return urs


@manager.command
def query_filter(name):
    name = name
    user = User.query.filter_by(name = name).all()
    urs=[]
    for u in user:
        ur={"id":u.id,"name":u.name,"description":u.description}
        urs.append(ur)
    return urs

@manager.command
def removeItem(id):
    item = User.query.filter_by(id=id).first()
    if item:
     db.session.delete(item)
     db.session.commit()
#
@manager.command
def updateUserinfo(id,name,desc):
    # user=User.query.filter_by(id=id).first().update({User.name:name,User.description:desc})
    user = User.query.filter_by(id=id).first()
    user.name=name
    user.description=desc
    db.session.commit()

if __name__ =='__main__':
    manager.run()