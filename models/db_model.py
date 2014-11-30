# -*- coding: utf-8 -*-

if db(db.auth_user).isempty():
    clave = db.auth_user.password.validate('1234')[0]
    db.auth_user.insert(first_name='Administrador',last_name='AbreCL',email='admin@abrecl.cl',password=clave)

import uuid

DB = db.define_table

DB('jardines_integra',
    Field('anho_proceso_asistencia'),
    Field('mes_proceso_asistencia'),
    Field('dire_reg'),
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

DB('centros_salud',
    Field('cod_old'),
    Field('cod_new'),
    Field('costa'),
    Field('cod_reg'),
    Field('region'),
    Field('seremi_servicio_salud'),
    Field('perteneciente'),
    Field('tipo_estrategia'),
    Field('tipo_establecimiento'),
    Field('dependencia'),
    Field('nivel_atencion'),
    Field('nombre_oficial'),
    Field('cod_com'),
    Field('comuna'),
    Field('via'),
    Field('numero'),
    Field('direccion'),
    Field('cod_seremi_servicio_salud'),
    Field('utm_x'),
    Field('utm_y'),
    Field('lat','double',writable=False,readable=False),
    Field('lon','double',writable=False,readable=False),
    Field('uuid',default=uuid.uuid4(),writable=False,readable=False),
    auth.signature
)

def to_latlon(easting, northing, zone_number=19, zone_letter='K',northern=None):
    import math

    K0 = 0.9996

    E = 0.00669438
    E2 = E * E
    E3 = E2 * E
    E_P2 = E / (1.0 - E)

    SQRT_E = math.sqrt(1 - E)
    _E = (1 - SQRT_E) / (1 + SQRT_E)
    _E2 = _E * _E
    _E3 = _E2 * _E
    _E4 = _E3 * _E
    _E5 = _E3 * _E

    M1 = (1 - E / 4 - 3 * E2 / 64 - 5 * E3 / 256)
    M2 = (3 * E / 8 + 3 * E2 / 32 + 45 * E3 / 1024)
    M3 = (15 * E2 / 256 + 45 * E3 / 1024)
    M4 = (35 * E3 / 3072)

    P2 = (3. / 2 * _E - 27. / 32 * _E3 + 269. / 512 * _E5)
    P3 = (21. / 16 * _E2 - 55. / 32 * _E4)
    P4 = (151. / 96 * _E3 - 417. / 128 * _E5)
    P5 = (1097. / 512 * _E4)

    R = 6378137

    ZONE_LETTERS = [
        (84, None), (72, 'X'), (64, 'W'), (56, 'V'), (48, 'U'), (40, 'T'),
        (32, 'S'), (24, 'R'), (16, 'Q'), (8, 'P'), (0, 'N'), (-8, 'M'), (-16, 'L'),
        (-24, 'K'), (-32, 'J'), (-40, 'H'), (-48, 'G'), (-56, 'F'), (-64, 'E'),
        (-72, 'D'), (-80, 'C')
    ]

    x = easting - 500000
    y = northing

    if not northern:
        y -= 10000000

    m = y / K0
    mu = m / (R * M1)

    p_rad = (mu +
             P2 * math.sin(2 * mu) +
             P3 * math.sin(4 * mu) +
             P4 * math.sin(6 * mu) +
             P5 * math.sin(8 * mu))

    p_sin = math.sin(p_rad)
    p_sin2 = p_sin * p_sin

    p_cos = math.cos(p_rad)

    p_tan = p_sin / p_cos
    p_tan2 = p_tan * p_tan
    p_tan4 = p_tan2 * p_tan2

    ep_sin = 1 - E * p_sin2
    ep_sin_sqrt = math.sqrt(1 - E * p_sin2)

    n = R / ep_sin_sqrt
    r = (1 - E) / ep_sin

    c = _E * p_cos**2
    c2 = c * c

    d = x / (n * K0)
    d2 = d * d
    d3 = d2 * d
    d4 = d3 * d
    d5 = d4 * d
    d6 = d5 * d

    latitude = (p_rad - (p_tan / r) *
                (d2 / 2 -
                 d4 / 24 * (5 + 3 * p_tan2 + 10 * c - 4 * c2 - 9 * E_P2)) +
                 d6 / 720 * (61 + 90 * p_tan2 + 298 * c + 45 * p_tan4 - 252 * E_P2 - 3 * c2))

    longitude = (d -
                 d3 / 6 * (1 + 2 * p_tan2 + c) +
                 d5 / 120 * (5 - 2 * c + 28 * p_tan2 - 3 * c2 + 8 * E_P2 + 24 * p_tan4)) / p_cos

    return (math.degrees(latitude),
            math.degrees(longitude) + zone_number_to_central_longitude(zone_number))


def latitude_to_zone_letter(latitude):
    for lat_min, zone_letter in ZONE_LETTERS:
        if latitude >= lat_min:
            return zone_letter

    return None


def latlon_to_zone_number(latitude, longitude):
    if 56 <= latitude <= 64 and 3 <= longitude <= 12:
        return 32

    if 72 <= latitude <= 84 and longitude >= 0:
        if longitude <= 9:
            return 31
        elif longitude <= 21:
            return 33
        elif longitude <= 33:
            return 35
        elif longitude <= 42:
            return 37

    return int((longitude + 180) / 6) + 1


def zone_number_to_central_longitude(zone_number):
    return (zone_number - 1) * 6 - 180 + 3

def generate_latlon():
    import utm,uuid
    dataset = db(db.centros_salud.lat==None).select()
    k = 0

    for d in dataset:
        utm_x = float(d.utm_x.replace('&','.'))
        utm_y = float(d.utm_y.replace('&','.'))
        try:
            lat,lon = utm.to_latlon(easting=utm_x,northing=utm_y,zone_number=19,zone_letter='K')
            d.update_record(lat=lat,lon=lon,uuid=uuid.uuid4())
        except:
            try:
                lat,lon = to_latlon(utm_x,utm_y)
                d.update_record(lat=lat,lon=lon,uuid=uuid.uuid4())
            except Exception, e:
                k+=1
                print e

    # print k
    return k

# generate_latlon()