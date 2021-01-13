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
    def __init__(self, name, surname, email, contact="", prefs=[]):
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


if __name__=="__main__":
    pref = SitePreference('cookies', False, True)
    user = User('username', 'usersurname', 'test@example.com', '7777777777',[pref])
    print(user.serialize())