from peewee import *
database = SqliteDatabase("tweepee")
class BaseModel(Model):
    class Meta:
        database = database

class Category(BaseModel):
    name = CharField()
    parent = ForeignKeyField('self', backref='children')

def create_tables():
    with database:
        database.create_tables([Category])

create_tables()
