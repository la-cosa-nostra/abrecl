# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else ['*']

## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables

# - [Fonasa, Isapre]
# [  ] Embarazada
# [  ] Amamantando
# [  ] Pertenece a Chile Solidario o Programa de ingreso ético familiar

# [  ] Enfermedades autoinmunes
# [  ] Desnutrición
# [  ] Nacimiento prematuro
# [  ] Diabetes
# [  ] Hipertención
# [  ] Tiene o tuvo TBC
# [  ] Otras enfermedades crónicas

auth.settings.extra_fields['auth_user'] = [
    Field('rut','string',length=12),
    Field('fecha_nacimiento','date'),
    Field('sexo',requires=IS_IN_SET(['Femenino','Masculino'],zero=None)),
    Field('prevision',requires=IS_IN_SET(['Fonasa','Isapre'],zero=None)),
    Field('embarazada','boolean',default=False),
    Field('amamantando','boolean',default=False),
    Field('chile_solidario','boolean',default=False,label='Pertenece a Chile Solidario o Programa de ingreso ético familiar'),
    Field('enf_autoinmunes','boolean',default=False,label='Enfermedades autoinmunes'),
    Field('desnutricion','boolean',default=False),
    Field('nac_prematuro','boolean',default=False,label='Nacimiento prematuro'),
    Field('diabetes','boolean',default=False),
    Field('hipertencion','boolean',default=False),
    Field('has_tbc','boolean',default=False,label='Tiene o tuvo TBC'),
    Field('otra_enf_cronica','boolean',default=False,label='Otras enfermedades crónicas')
]

auth.define_tables(username=False, signature=False)

db.auth_user.embarazada.show_if = (db.auth_user.sexo=='Femenino')
db.auth_user.amamantando.show_if = (db.auth_user.sexo=='Femenino')

auth.settings.formstyle = 'divs'

if request.controller=='default' and request.function=='user' and request.args(0)=='profile':
    db.auth_user.email.writable=False
    db.auth_user.email.readable=False

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
#from gluon.contrib.login_methods.janrain_account import use_janrain
#use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
