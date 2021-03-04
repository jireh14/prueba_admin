import web

db_host = 'localhost'
db_name = 'kuorra_admin'
db_user = 'prueba'
db_pw = 'prueba.2021'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )