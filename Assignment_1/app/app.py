#!userdetails/bin/python

import os
from flask import Flask, request, jsonify,g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

#Database Details
basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = os.path.join(basedir, '../data.sqlite')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbdir


db = SQLAlchemy(app)
auth = HTTPBasicAuth()


##ErrorHandling
class ValidationError(ValueError):
      pass

@app.errorhandler(ValidationError)
def bad_request(e):
    return jsonify({'Status':400,'error':'Bad Request'}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({'status':404,'error':'User Stuff Not Found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'status':500,'error':"Internal Server Error"}), 500 

#User Model
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(128))
    shelltype = db.Column(db.String(60))
    homedir = db.Column(db.String(60))

    def export_details(self):
        return {
              "id"       : self.id,
              "username" : self.username,
              "shelltype" : self.shelltype,
              "homedir" : self.homedir
         }

    def import_details(self,data):
        try:
             self.username  = data['username']
             self.shelltype = data['shelltype']
             self.homedir   = data['homedir']

        except KeyError as e:
             raise ValidationError('Invalid User Details' + e.args[0])

        return self

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

@auth.verify_password
def verify_password(username,password):
    g.user = Users.query.filter_by(username=username).first()
    if g.user is None:
       return False
    return g.user.verify_password(password)

@app.before_request
@auth.login_required
def before_request():
    pass

@auth.error_handler
def unauthorized():
    return jsonify({'status': 401, 'error':'Unauthorized','Message':"Please Authenticate"})

## CURD Operation
@app.route('/user', methods=['POST'])
def create():
    new_user = Users()
    new_user.import_details(request.json)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"Status":"User Created Successfully"}),201

@app.route('/')
@app.route('/user', methods=['GET'])
def get_users():
    return jsonify({'Users' : [ user.export_details() for user in Users.query.all()]})

@app.route('/user/<int:id>',methods=['GET'])
def get_user(id):
    return jsonify(Users.query.get_or_404(id).export_details())

@app.route('/user/<int:id>',methods=['PUT'])
def update_user(id):
    user_data = Users.query.get_or_404(id)
    user_data.import_details(request.json)
    db.session.add(user_data)
    db.session.commit()
    return jsonify({"Status" :" User Details Update"})

@app.route('/user/<int:id>',methods=['DELETE'])
def delete_user(id):
    if id != 1:
       user_data = Users.query.get_or_404(id)
       db.session.delete(user_data)
       db.session.commit()
       return jsonify({"Status":"User Details Deleted"})
    else:
       return jsonify({"Status": "Cannot Delete Admin User"})


#Driver Program
if __name__ == '__main__':
    db.create_all()
    if Users.query.get(1) is None:
       admin = Users(username='admin')
       admin.hash_password('admin123')
       db.session.add(admin)
       db.session.commit()
    app.run("0.0.0.0",port=5000,debug=True)
