import json
import datetime
from peewee import *

db = SqliteDatabase('./database/smartwbdb.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    surname = CharField(null=True)
    email = CharField()
    contact = CharField(null=True)
        
    def __str__(self):
        return self.name+" "+self.surname
    
    def get_json(self):
        obj = {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "contact": self.contact
        }
        return obj
    
    def serialize(self):
        return json.dumps(self.get_json())


class SavedPassword(BaseModel):
    user = ForeignKeyField(User, backref="passwords")
    site = CharField()
    username = CharField()
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    def get_json(self):
        obj = {
            "site": self.site,
            "username": self.username,
            "password": self.password
        }
        return obj

    def serialize(self):
        return json.dumps(self.get_json())


class History(BaseModel):
    user = ForeignKeyField(User, backref="history", null=True)
    title = CharField()
    site = CharField()
    visit_date = DateTimeField(default=datetime.datetime.now)

    def get_json(self):
        obj = {
            "site": self.site,
            "visit_date": self.visit_date
        }
        return obj

    def serialize(self):
        return json.dumps(self.get_json())


class SavedPage(BaseModel):
    user = ForeignKeyField(User, backref="saved_pages", null=True)
    title = CharField()
    url = CharField()

    def get_json(self):
        obj = {
            "title": self.title,
            "url": self.url
        }
        return obj
    
    def serialize(self):
        return json.dumps(self.get_json())


class Favourite(SavedPage):
    pass


class Bookmark(SavedPage):
    folder = CharField()
    
    def get_json(self):
        obj = super().get_json()
        obj["folder"] = self.folder
        return obj


class SettingProvider:
    def __init__(self, load=False):
        self.__value = dict()
        if load:
            self.__load_settings()
    
    def __load_settings(self):
        pass

    def set(self, key, value):
        self.__value[key] = value
    
    def get(self, key):
        return self.__value[key]
    
    def get_all(self):
        return self.__value


if __name__=="__main__":
    db.create_tables([User, SavedPassword, History, Favourite, Bookmark])