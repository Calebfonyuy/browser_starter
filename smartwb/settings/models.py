import json


class Preference:
    """
    This class represents the user preferences on the browser.
    It is basically made up of the preference reference and the value
    """
    def __init__(self, ref_name, value):
        if ref_name is None or len(str(ref_name))<2:
            raise Exception("Invalid reference name. Reference name should be at least two characters long")
        
        if value is None:
            value = ""
            
        self.ref_name = ref_name
        self.value = value
        
    def serialize(self):
        data = {
            "ref_name": self.ref_name,
            "value": self.value
        }
        return json.dumps(data)


class SitePreference(Preference):
    """
    Settings for sites
    """
    def __init__(self, ref_name, value, site):
        if site is None or type(site) is not str:
            raise Exception("site attribute must be a string")
        
        self.super(ref_name, value)
        self.url = url

    def serialize(self):
        data = {
            "site": self.site,
            "ref_name": self.ref_name,
            "value": self.value
        }
        return json.dumps(data)
        

class User:
    def __init__(self, email, name, surname="", contact="", prefs=[]):
        if type(prefs) is not list:
            raise Exception("prefs attribute must be a list of preferences")
        
        for item in prefs:
            if type(item) is not Preference:
                raise Exception(str(item) + " is not an instance of Preference")
        
        self.name = name
        self.surname = surname
        self.email = email
        self.contact = contact
        self.prefs = prefs
        
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


class SavedPassword:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password
    
    def get_json(self):
        obj = {
            "site": self.site,
            "username": self.username,
            "password": self.password
        }
        return obj

    def serialize(self):
        return json.dumps(self.get_json())


class History:
    def __init__(self, site, visit_date):
        self.site = site
        self.visit_date = visit_date

    def get_json(self):
        obj = {
            "site": self.site,
            "visit_date": self.visit_date
        }
        return obj

    def serialize(self):
        return json.dumps(self.get_json())


class SavedSite:
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def get_json(self):
        obj = {
            "title": self.title,
            "url": self.url
        }
        return obj
    
    def serialize(self):
        return json.dumps(self.get_json())


class Favourite(SavedSite):
    pass


class Bookmark(SavedSite):
    def __init__(self, title, url, folder):
        super().__init__(title, url)
        self.folder = folder
    
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
    item = Bookmark("hello","hello","hello")
    print(item.serialize())