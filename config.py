class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://feisal:1234@localhost/blog'
    SECRET_KEY = '123'




class ProdConfig(Config):
    pass



class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}