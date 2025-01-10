import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tienda_8_2_iok1_user:tlVhpekwqImnjrpZWXcQ07iuQlgujqqx@dpg-ctvp2mbtq21c73ah810g-a.frankfurt-postgres.render.com/tienda_8_2_iok1'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:password@localhost/base_datos'
#SQLALCHEMY_TRACK_MODIFICATIONS=False

