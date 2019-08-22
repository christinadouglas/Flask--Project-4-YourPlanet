from peewee import * 
from flask_login import UserMixin 
import datetime 

from peewee import * 
from flask_login import UserMixin 
import datetime

DATABASE = SqliteDatabase('planet.sqlite')

class User(UserMixin, Model):
    username = CharField() 
    email = CharField()
    password = CharField()

    class Meta:
        database = DATABASE

def initalize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True) 
    print('TABLES CREATED')
    DATABASE.close()