import MySQLdb

from helloflask import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self,name,description):
        # self.id = id
        self.name = name
        self.description = description

# def get_connection():
#     host="127.0.0.1"
#     port = 3306
#     db="helloflask"
#     user = 'root'
#     password = 'Test1234'
#     conn = MySQLdb.connect( host = host,
#                             user= user,
#                             passwd = password,
#                             db =db,
#                             port = port,
#                             charset = "utf8")
#     return conn

# class User(object):
#     def __init__(self,name,description):
#         # self.id = id
#         self.name = name
#         self.description = description

    # def save(self):
    #     conn = get_connection()
    #     cursor = conn.cursor()
    #     sql = "insert into user(name,description)VALUES(%s,%s)"
    #     cursor.execute(sql,(self.name,self.description))
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #
    # @staticmethod
    # def query_all():
    #     conn = get_connection()
    #     cursor = conn.cursor()
    #     sql = "select * from user"
    #     cursor.execute(sql)
    #     rows = cursor.fetchall()
    #     users=[]
    #     for r in rows:
    #         user = User(r[1],r[2])
    #         users.append(user)
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     return users


    def __str__(self):
        return " 'id':{},'name':{},'description':{} ".format(self.id,self.name,self.description)