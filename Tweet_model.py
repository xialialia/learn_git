import datetime
from peewee import *

db = SqliteDatabase('tweet_model.db')

class User(Model):
    username = CharField(unique=True)
    class Meta:
        database = db

class Tweet(Model):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
    class Meta:
        database = db

db.connect()
db.create_tables([User, Tweet])