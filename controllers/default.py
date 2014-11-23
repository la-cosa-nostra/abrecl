# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def index2():
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login()
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)

def search_schools():
    import requests
    comuna = request.vars.comuna or ''
    url_colegios = "http://data.mineduc.cl/odata/Establecimiento_Matricula/?$format=json&$filter=nombre_comuna eq '%s'"%comuna
    res = requests.get(url_colegios)
    return dict(res=res.json())

def action_menu():
    action = request.vars.action or False

    opciones = []

    if action=='salud':
        opciones = db(db.menu_abrecl.cat=='Salud').select()
    elif action=='educacion':
        opciones = db(db.menu_abrecl.cat=='Educacion').select()
    elif action=='seguridad':
        opciones = db(db.menu_abrecl.cat=='Seguridad').select()
    elif action=='sociedad':
        opciones = db(db.menu_abrecl.cat=='Sociedad').select()
    elif action=='familia':
        opciones = db(db.menu_abrecl.cat=='Familia').select()
    elif action=='turismo':
        opciones = db(db.menu_abrecl.cat=='Turismo').select()
    elif action=='tramites':
        opciones = db(db.menu_abrecl.cat=='Tramites').select()
    elif action=='energia':
        opciones = db(db.menu_abrecl.cat=='Energia').select()
    elif action=='negocios':
        opciones = db(db.menu_abrecl.cat=='Negocios').select()
    else:
        return 'request invalid'

    return dict(opciones=opciones,action=action)

def action_submenu():
    action = db.menu_abrecl(request.vars.action) or False

    opciones = ['Programa Nacional de Alimentación Complementaria','Jardines Integra']

    if action:
        if action.subcat==opciones[0]:
            redirect(URL('pnac','index.load',vars=request.vars))
        else:
            return 'invalid request'
    else:
        return 'invalid request'


def admin():
    response.view = 'generic.%s'%request.extension
    return {'menu':UL([A(t, _href=URL(args=t)) for t in db.tables]),'admin':SQLFORM.smartgrid(db[request.args(0) or 'menu_abrecl'])}

def login():
    return dict()

def paso1():
    return dict()

def paso2():
    return dict()

def paso3():
    return dict()