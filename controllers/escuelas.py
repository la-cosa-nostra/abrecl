# -*- coding: utf-8 -*-

def jardines_integra():
    comuna = request.vars.comuna or ''
    action = db.menu_abrecl(request.vars.action) or False
    # if comuna!='ubicación desconocida':
    #     dataset=db(db.pnac).select(orderby=db.pnac.nombre_comuna,limitby=(0,50))
    # else:
    #     dataset = db(db.pnac.nombre_comuna.like(comuna)).select(limitby=(0,50))
    dataset = db(db.jardines_integra.glosa_comuna.like(comuna)).select(limitby=(0,50))
    return dict(dataset=dataset,action=action,comuna=comuna)

def colegios():
    import requests
    comuna = request.vars.comuna or ''
    action = db.menu_abrecl(request.vars.action) or False
    url_colegios = "http://data.mineduc.cl/odata/Establecimiento_Matricula/?$format=json&$filter=nombre_comuna eq '%s' and agno eq '2014'"%comuna
    res = requests.get(url_colegios)
    return dict(res=res.json()['d'],action=action,comuna=comuna)

def jardines_juni():
    return dict()