from peewee import *
import datetime
database = SqliteDatabase("datetime")

class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)

def create_tables():
    with database:
        database.create_tables([User])

create_tables()

