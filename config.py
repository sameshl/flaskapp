import os



class Config:
    '''
    Generate hidden secert key with the help of pythons inbuilt secrets module.
    We are generating a random 16 bits key.

    import secerts
    secrets.token_hex(16)
    '''


    SECRET_KEY='be2c117bdf7dfe089101bb27f4b99825'#Add SECRET_KEY and SQLALCHEMY_DATABASE_URI to path variables after wards
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    #app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
    #app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')

    MAIL_USERNAME='demouser967'
    MAIL_PASSWORD='demopassword'
