from peewee import *

db = SqliteDatabase('join.db')

class User(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Team(Model):
    user = ForeignKeyField(User, backref='team')
    name = CharField()
    team_type = CharField()

    class Meta:
        database = db

class Teamprofile(Model):
    user = ForeignKeyField(Team, backref='profile')
    something = CharField()
    address = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([User, Team, Teamprofile])
