DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "drmozart",
        "USER": "root",
        "PASSWORD": "rktn4156",
        "HOST": "drmozart.cl2mk0mgzle0.us-east-2.rds.amazonaws.com",
        "PORT": "3306",
        "TEST": {"CHARSET": "utf8", "COLLATION": "utf8_general_ci",},
        "OPTIONS": {"init_command": 'SET sql_mode="STRICT_TRANS_TABLES"'},
    }
}

SECRET = "mozart"


EMAIL = {
'EMAIL_BACKEND' : 'django.core.mail.backends.smtp.EmailBackend',
'EMAIL_USE_TLS' : True,
'EMAIL_PORT' : 587,
'EMAIL_HOST' : 'smtp.gmail.com',   
'EMAIL_HOST_USER' : 'dongsagi90@gmail.com',                    
'EMAIL_HOST_PASSWORD' : '7979cnrgk',
'REDIRECT_PAGE' : 'http://10.58.5.40:3000/signin'
}
