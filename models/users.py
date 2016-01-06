from google.appengine.ext import ndb

class Users(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    confirmation_code = ndb.StringProperty(required=True) # For email confirmation process
    confirmation_email = ndb.BooleanProperty(default=False)

    @classmethod
    def check_if_exists(cls, email):
        return cls.query(cls.email == email).get()

    @classmethod
    def add_new_user(cls, name, email, password):
        user = cls.check_if_exists(email)

        if user:
            pass
        else:
            return {
                'created': False,
                'title': 'This email is already in use',
                'message': 'Please log in if this is your email account'
            }

