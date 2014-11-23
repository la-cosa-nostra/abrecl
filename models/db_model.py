# -*- coding: utf-8 -*-

if db(db.auth_user).isempty():
    clave = db.auth_user.password.validate('1234')[0]
    db.auth_user.insert(first_name='Administrador',last_name='AbreCL',email='admin@abrecl.cl',password=clave)

import uuid

DB = db.define_table

DB('jardines_integra',
    Field('ano_proceso_asistencia'),
    Field('mes_proceso_asistencia'),
    Field('dir_reg'),
    Field('glosa_comuna'),
    Field('jornada'),
    Field('codigo_jardin'),
    Field('nombre_jardin'),
    Field('direccion_jardin'),
    Field('numero_jardin'),
    Field('telefono'),
    Field('modalidad_atencion'),
    Field('detalle_modalidad_atencion'),
    Field('zona_ubicacion'),
    Field('extension_horaria'),
    Field('tipologia'),
    Field('uuid',default=uuid.uuid4(),writable=False,readable=False),
    auth.signature
)

# DB('jardines_junji',
#     Field('')
# )


DB('menu_abrecl',
    Field('cat',requires=IS_IN_SET(['Salud','Educacion','Seguridad','Sociedad','Familia','Turismo','Tramites','Energia','Negocios'])),
    Field('subcat','string',requires=IS_NOT_EMPTY()),
    Field('uuid',default=uuid.uuid4(),writable=False,readable=False),
    auth.signature
)

if db(db.menu_abrecl).isempty():
    salud = ['CESFAM','Programa Nacional de Alimentación Complementaria','Farmacias','Farmacias de Turno','Bioequivalencias','No Donantes']
    for op in salud:
        db.menu_abrecl.insert(cat='Salud',subcat=op)

    educacion = ['Jardines Integra','Jardines Junji','Colegios, Escuelas y Liceos','Bibliotecas']
    for op in educacion:
        db.menu_abrecl.insert(cat='Educacion',subcat=op)

    seguridad = ['Reclusos por Region','Femicidios por Region']
    for op in seguridad:
        db.menu_abrecl.insert(cat='Seguridad',subcat=op)

    sociedad = ['Fondos Concursables','Personas juridicas sin fines de lucro']
    for op in sociedad:
        db.menu_abrecl.insert(cat='Sociedad',subcat=op)

    Familia = ['Centro SERNAM']
    for op in Familia:
        db.menu_abrecl.insert(cat='Familia',subcat=op)

    Turismo = ['Zonas y Centros de Interes Turistico','Museos']
    for op in Turismo:
        db.menu_abrecl.insert(cat='Turismo',subcat=op)

    Tramites = ['Servicios Chile Atiende','Formularios Chile Atiende']
    for op in Tramites:
        db.menu_abrecl.insert(cat='Tramites',subcat=op)

    Energia = ['Precios y Gas de Bencina por Region','Puntos de Reciclaje - Region Metropolitana']
    for op in Energia:
        db.menu_abrecl.insert(cat='Energia',subcat=op)

    Negocios = ['Oportunidades de Negocios Chile Compra']
    for op in Negocios:
        db.menu_abrecl.insert(cat='Negocios',subcat=op)


DB('pnac',
    Field('cod_antiguo'),
    Field('cod_nuevo'),
    Field('cod_antiguo_madre'),
    Field('cod_nuevo_madre'),
    Field('cod_region'),
    Field('region'),
    Field('servicio_salud'),
    Field('perteneciente'),
    Field('tipo_establecimiento'),
    Field('tipo_estrategia'),
    Field('certificacion'),
    Field('dependencia'),
    Field('nivel_atencion'),
    Field('nombre_oficial'),
    Field('alias_a'),
    Field('codigo_comuna'),
    Field('nombre_comuna'),
    Field('via'),
    Field('numero'),
    Field('direccion'),
    Field('telefono'),
    Field('fecha_vigencia_desde'),
    Field('fecha_cierre_hasta'),
    Field('cod_servicio_salud_seremi'),
    Field('uuid',default=uuid.uuid4(),writable=False,readable=False),
    auth.signature
)