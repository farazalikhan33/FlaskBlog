
class Config:

    SECRET_KEY = '' # the secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'flaskblogger@gmail.com'
    MAIL_PASSWORD = '' # the password
