# -*- coding: utf-8 -*-

def index():
    comuna = request.vars.comuna or ''
    action = db.menu_abrecl(request.vars.action) or False
    # if comuna!='ubicación desconocida':
    #     dataset=db(db.pnac).select(orderby=db.pnac.nombre_comuna,limitby=(0,50))
    # else:
    #     dataset = db(db.pnac.nombre_comuna.like(comuna)).select(limitby=(0,50))
    dataset = db(db.pnac.nombre_comuna.like('providencia')).select(limitby=(0,50))
    return dict(dataset=dataset,action=action,comuna=comuna)

def view():
    pnc = db.pnac(request.arg(0)) or False

    if pnc:
        return dict(pnc=pnc)
    else:
        return 'invalid request'