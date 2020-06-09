from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employees(db.Model):

    __tablename__ = 'employees'
    __searchable__ = ['name', 'designation', 'phone']
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    designation = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    phone = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    picture = db.Column(db.String, nullable = False)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.designation = kwargs.get('designation','')
        self.address  = kwargs.get('address','Not Provided')
        self.phone  = kwargs.get('phone','Not Provided')
        self.email  = kwargs.get('email','')
        self.picture = kwargs.get('picture','default_picture.png')


    def serialize(self):
        return{
        'id': self.id,
        'name': self.name,
        'designation': self.designation,
        'address': self.address,
        'phone': self.phone,
        'email': self.email,
        'picture': self.picture
        }
