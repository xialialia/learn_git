from peewee import *

db = SqliteDatabase('peewee.db')

class Photo(Model):
    image = CharField()
    class Meta:
        database = db

class Tag(Model):
    name = CharField()
    class Meta:
        database = db

class PhotoTag(Model):
    photo = ForeignKeyField(Photo)
    tag = ForeignKeyField(Tag)
    class Meta:
        database = db

db.connect()
db.create_tables([Photo, Tag, PhotoTag])