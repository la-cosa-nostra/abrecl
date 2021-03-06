# -*- coding: utf-8 -*-

# HELPERS

def beneficios_salud(familia=False):
    if familia:
        dataset = db(db.familia.user_id==auth.user.id).select()
    else:
        dataset = db(db.auth_user.id==auth.user.id).select()

    resultset = []
    result_temp = []

    default_img = 'http://placehold.it/150.png/09f/fff&text=Beneficio'

    # static/images/beneficios/anios_dorados.jpg
    # static/images/beneficios/educacion_publica.jpg
    # static/images/beneficios/examen_preventivo.jpg
    # static/images/beneficios/integra.jpg
    # static/images/beneficios/junji.jpg
    # static/images/beneficios/mi_sopita.jpg
    # static/images/beneficios/purita_cereal.jpg
    # static/images/beneficios/purita_fortificada.jpg
    # static/images/beneficios/purita_mama.jpg

    for d in dataset:
        diff = request.now.date() - d.fecha_nacimiento
        result_temp = []

        ######## PNAC ########
        if diff.days/30 < 18: # tiene menos de 18 meses
            result_temp.append({
                'cat':'pnac',
                'id':1,
                'nombre':'Leche Purita Fortificada',
                'descripcion':'Puede retirar leche Purita Fortificada (en cualquiera de los centros cercanos CESFAM).',
                'imagen':URL('static','images/beneficios/purita_fortificada.jpg')
                })

        if diff.days/30 >= 6 and diff.days/365 < 6: # tiene más de 6 meses y menos de 6 años
            result_temp.append({
                'cat':'pnac',
                'id':2,
                'nombre':'Mi Sopita',
                'descripcion':'Puede retirar Mi Sopita (en cualquiera de los centros cercanos CESFAM).',
                'imagen':URL('static','images/beneficios/mi_sopita.jpg')
                })

        if diff.days/30 >= 18 and diff.days/365 < 6: # tiene más de 18 meses y menos de 6 años
            result_temp.append({
                'cat':'pnac',
                'id':3,
                'nombre':'Leche Purita Cereal',
                'descripcion':'Puede retirar leche Purita Cereal (en cualquiera de los centros cercanos CESFAM).',
                'imagen':URL('static','images/beneficios/purita_cereal.jpg')
                })

        if diff.days/30 <= 12 and (d.desnutricion or d.nac_prematuro): # tiene menos de 12 meses y está desnutrido o nacio prematuro
            result_temp.append({
                'cat':'pnac',
                'id':4,
                'nombre':'Leche Purita Cereal',
                'descripcion':'Puede retirar leche Purita Cereal (en cualquiera de los centros cercanos CESFAM).',
                'imagen':URL('static','images/beneficios/purita_cereal.jpg')
                })

        if d.embarazada: # está embarazada
            result_temp.append({
                'cat':'pnac',
                'id':5,
                'nombre':'Leche Purita Mamá',
                'descripcion':'Puede retirar leche Purita Mamá (en cualquiera de los centros cercanos CESFAM).',
                'imagen':URL('static','images/beneficios/purita_mama.jpg')
                })

        # tiene más de 70 años y está en fonasa || tiene más de 65 años y tiene o tuvo tuberculosis
        if (diff.days/365 >=70 and d.prevision=='Fonasa') or (diff.days/365 >=65 and d.has_tbc) or (diff.days/365>=65 and d.chile_solidario):
            result_temp.append({
                'cat':'pnac',
                'id':6,
                'nombre':'Crema Años Dorados',
                'descripcion':'Puede retirar crema Años Dorados (en cualquiera de los centros cercanos CESFAM).',
                'imagen':URL('static','images/beneficios/anios_dorados.jpg')
                })
            result_temp.append({
                'cat':'pnac',
                'id':7,
                'nombre':'Bebida Láctea Adulto Mayor',
                'descripcion':'Puede retirar Bebida Láctea Adulto Mayor.',
                'imagen':'http://placehold.it/150.png/09f/fff&text=Bebida Láctea Adulto Mayor'
                })

        ######## FIN PNAC ########

        ######## CHEQUEO SALUD ########

        if d.prevision=='Fonasa' and (diff.days <30 or diff.days/365>=15 or d.embarazada): # guagua en fonasa
            result_temp.append({
                'cat':'check_salud',
                'id':8,
                'nombre':'Examen Preventivo',
                'descripcion':'Examen anual de salud gratuito en CESFAM',
                'imagen':URL('static','images/beneficios/examen_preventivo.jpg')
                })

        ######## FIN CHEQUEO SALUD ########

        resultset.append({
            'user':d.nombre if familia else d.first_name,
            'beneficios':result_temp,
            'familia':familia
            })


    return resultset


def beneficios_educacion(familia=False):
    if familia:
        dataset = db(db.familia.user_id==auth.user.id).select()
    else:
        dataset = db(db.auth_user.id==auth.user.id).select()

    resultset = []
    result_temp = []

    default_img = 'http://placehold.it/150.png/09f/fff&text=Beneficio'

    for d in dataset:
        diff = request.now.date() - d.fecha_nacimiento
        result_temp = []

        ######## EDUCACION ########
        if diff.days/365>=2 and diff.days/365<=4: # 2 <= x <= 4
            result_temp.append({
                'cat':'educacion',
                'id':9,
                'nombre':'Inscripción en jardín Junji',
                'descripcion':'Inscripción en jardín Junji',
                'imagen':URL('static','images/beneficios/junji.jpg')
                })

        if diff.days>=85 and diff.days <= 1824: # 2 <= x <= 4
            result_temp.append({
                'cat':'educacion',
                'id':10,
                'nombre':'Inscripción en jardín Integra',
                'descripcion':'Inscripción en jardín Integra',
                'imagen':URL('static','images/beneficios/integra.jpg')
                })

        if diff.days/365>4: # 2 <= x <= 4
            result_temp.append({
                'cat':'educacion',
                'id':11,
                'nombre':'Educación Gratutita Municipal.',
                'descripcion':'Educación básica y media gratutita en escuelas y liceos municipales.',
                'imagen':URL('static','images/beneficios/educacion_publica.jpg')
                })



        resultset.append({
            'user':d.nombre if familia else d.first_name,
            'beneficios':result_temp,
            'familia':familia
            })


    return resultset