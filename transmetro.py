# ============================================================================
# SISTEMA INTELIGENTE DE RUTAS - TRANSMETRO BARRANQUILLA
# ============================================================================

from datetime import datetime   # solo para usar la hora actual si no se escribe

# ---------------------------------------------------------------------------
# 1) ESTACIONES DE LA RED TRONCAL (17)
#    clave -> (nombre oficial, troncal, orden dentro de la troncal)
# ---------------------------------------------------------------------------
ESTACIONES = {
    "portal_soledad": ("Estación Portal de Soledad", "murillo", 0),
    "pacho_galan": ("Estación Pacho Galán", "murillo", 1),
    "pedro_ramaya": ("Estación Pedro Ramayá Beltrán", "murillo", 2),
    "joaquin_barrios": ("Estación Joaquín Barrios Polo / Estadio Metropolitano", "murillo", 3),
    "buenos_aires": ("Estación Buenos Aires", "murillo", 4),
    "la_ocho": ("Estación La Ocho", "murillo", 5),
    "la_catorce": ("Estación La Catorce", "murillo", 6),
    "la_veintiuna": ("Estación La Veintiuna", "murillo", 7),
    "atlantico": ("Estación Atlántico", "murillo", 8),
    "chiquinquira": ("Estación Chiquinquirá", "murillo", 9),
    "la_arenosa": ("Estación La Arenosa", "murillo", 10),
    "parque_cultural": ("Estación Parque Cultural del Caribe", "olaya_herrera", 0),
    "barrio_abajo": ("Estación Barrio Abajo", "olaya_herrera", 1),
    "la_catedral": ("Estación La Catedral", "olaya_herrera", 2),
    "alfredo_correa": ("Estación Alfredo Correa De Andréis", "olaya_herrera", 3),
    "esthercita_forero": ("Estación Esthercita Forero", "olaya_herrera", 4),
    "joe_arroyo": ("Estación retorno Joe Arroyo", "olaya_herrera", 5),
}

# ---------------------------------------------------------------------------
# 2) RUTAS TRONCALES (12).
#    - tipo 'corriente' = para en todas las estaciones de su recorrido
#      tipo 'expreso'   = solo para en las de su lista (se salta las demas)
#    - estado 'suspendida' = la ruta no presta servicio
#    - horarios = franjas del dia LABORAL en MINUTOS desde medianoche
#      (300 = 5:00 a.m.). Fuera de las franjas, la ruta no opera.
# ---------------------------------------------------------------------------
RUTAS = {
    "B1": {
        "nombre": "B1",
        "tipo": "corriente",
        "estado": "activa",
        # opera el dia laboral de 05:00 a 18:22
        "paradas": [
            "portal_soledad",
            "pacho_galan",
            "pedro_ramaya",
            "joaquin_barrios",
            "buenos_aires",
            "la_ocho",
            "la_catorce",
            "la_veintiuna",
            "atlantico",
            "chiquinquira",
            "la_arenosa",
            "barrio_abajo",
            "parque_cultural",
        ],
        "horarios": [[300, 1102]],
    },
    "B2": {
        "nombre": "B2",
        "tipo": "corriente",
        "estado": "activa",
        # opera el dia laboral de 06:15 a 20:00
        "paradas": [
            "joe_arroyo",
            "esthercita_forero",
            "alfredo_correa",
            "la_catedral",
            "barrio_abajo",
            "parque_cultural",
        ],
        "horarios": [[375, 1200]],
    },
    "R1": {
        "nombre": "R1",
        "tipo": "corriente",
        "estado": "activa",
        # opera el dia laboral de 05:00 a 21:18
        "paradas": [
            "portal_soledad",
            "pacho_galan",
            "pedro_ramaya",
            "joaquin_barrios",
            "buenos_aires",
            "la_ocho",
            "la_catorce",
            "la_veintiuna",
            "atlantico",
            "chiquinquira",
            "la_arenosa",
            "la_catedral",
            "alfredo_correa",
            "esthercita_forero",
            "joe_arroyo",
        ],
        "horarios": [[300, 1278]],
    },
    "R2": {
        "nombre": "R2",
        "tipo": "corriente",
        "estado": "activa",
        # opera el dia laboral de 06:00 a 19:45
        "paradas": [
            "parque_cultural",
            "barrio_abajo",
            "la_catedral",
            "alfredo_correa",
            "esthercita_forero",
            "joe_arroyo",
        ],
        "horarios": [[360, 1185]],
    },
    "S1": {
        "nombre": "S1",
        "tipo": "corriente",
        "estado": "activa",
        # opera el dia laboral de 05:12 a 22:00
        "paradas": [
            "joe_arroyo",
            "esthercita_forero",
            "alfredo_correa",
            "la_catedral",
            "la_arenosa",
            "chiquinquira",
            "atlantico",
            "la_veintiuna",
            "la_catorce",
            "la_ocho",
            "buenos_aires",
            "joaquin_barrios",
            "pedro_ramaya",
            "pacho_galan",
            "portal_soledad",
        ],
        "horarios": [[312, 1320]],
    },
    "S2": {
        "nombre": "S2",
        "tipo": "corriente",
        "estado": "activa",
        # opera el dia laboral de 05:38 a 22:00
        "paradas": [
            "parque_cultural",
            "barrio_abajo",
            "la_arenosa",
            "chiquinquira",
            "atlantico",
            "la_veintiuna",
            "la_catorce",
            "la_ocho",
            "buenos_aires",
            "joaquin_barrios",
            "pedro_ramaya",
            "pacho_galan",
            "portal_soledad",
        ],
        "horarios": [[338, 1320]],
    },
    "B10": {
        "nombre": "B10",
        "tipo": "expreso",
        "estado": "suspendida",
        # opera el dia laboral de 05:30 a 08:26
        "paradas": [
            "portal_soledad",
            "joaquin_barrios",
            "la_ocho",
            "atlantico",
            "la_arenosa",
            "parque_cultural",
        ],
        "horarios": [[330, 506]],
    },
    "R10": {
        "nombre": "R10",
        "tipo": "expreso",
        "estado": "activa",
        # opera el dia laboral de 05:37 a 09:37  y  15:30 a 20:00
        "paradas": [
            "portal_soledad",
            "joaquin_barrios",
            "la_ocho",
            "la_catedral",
            "alfredo_correa",
            "esthercita_forero",
            "joe_arroyo",
        ],
        "horarios": [[337, 577], [930, 1200]],
    },
    "R40": {
        "nombre": "R40",
        "tipo": "expreso",
        "estado": "suspendida",
        # opera el dia laboral de 05:30 a 08:00
        "paradas": [
            "pacho_galan",
            "pedro_ramaya",
            "buenos_aires",
            "la_catedral",
            "alfredo_correa",
            "joe_arroyo",
        ],
        "horarios": [[330, 480]],
    },
    "S10": {
        "nombre": "S10",
        "tipo": "expreso",
        "estado": "activa",
        # opera el dia laboral de 05:37 a 09:37
        "paradas": [
            "joe_arroyo",
            "alfredo_correa",
            "la_catedral",
            "la_ocho",
            "joaquin_barrios",
            "portal_soledad",
        ],
        "horarios": [[337, 577]],
    },
    "S20": {
        "nombre": "S20",
        "tipo": "expreso",
        "estado": "suspendida",
        # opera el dia laboral de 16:30 a 19:33
        "paradas": [
            "parque_cultural",
            "la_arenosa",
            "atlantico",
            "la_ocho",
            "joaquin_barrios",
            "portal_soledad",
        ],
        "horarios": [[990, 1173]],
    },
    "S40": {
        "nombre": "S40",
        "tipo": "expreso",
        "estado": "activa",
        # opera el dia laboral de 16:00 a 19:00
        "paradas": [
            "joe_arroyo",
            "alfredo_correa",
            "la_catedral",
            "buenos_aires",
            "pedro_ramaya",
            "pacho_galan",
            "portal_soledad",
        ],
        "horarios": [[960, 1140]],
    },
}

# ---------------------------------------------------------------------------
# 3) RUTAS ALIMENTADORAS (29).  Conectan los barrios con las estaciones
#    de la troncal: el primer o ultimo tramo del viaje puede ser en una.
#    - 'estaciones': donde se transborda con la troncal ([] = la fuente
#      oficial no publica ese dato para esa ruta)
#    - 'barrios': barrios que recorre, para buscarla tambien por barrio
# ---------------------------------------------------------------------------
ALIMENTADORAS = {
    "A1-2 Carrera Ocho": {
        "estado": "activa",
        "estaciones": ["la_ocho"],
        "barrios": ["El Campito", "El Santuario", "Kennedy", "La Alboraya", "La Magdalena", "La Sierra", "La Sierrita", "La Unión", "Las Nieves", "Las Palmas", "Los Continentes", "Santa Helena", "Tayrona"],
    },
    "A1-3 Galán": {
        "estado": "activa",
        "estaciones": ["joaquin_barrios"],
        "barrios": ["Bella Arena", "El Milagro", "José Antonio Galán", "Las Dunas", "Las Palmas", "Los Laureles", "Tabaco Rubio", "Universal I", "Universal II", "Villa Blanca"],
    },
    "A1-4 La Magdalena": {
        "estado": "activa",
        "estaciones": ["buenos_aires"],
        "barrios": ["Buenos Aires", "José Antonio Galán", "La Magdalena", "Las Palmas", "Limón", "Tabaco Rubio", "Tayrona"],
    },
    "A2-1 Hipódromo": {
        "estado": "activa",
        "estaciones": ["joaquin_barrios"],
        "barrios": ["Barrio Centro", "Calle de las Flores", "Ciudadela 20 de Julio", "El Carnero", "El Centenario", "El Hipódromo", "El Oriental", "El Pasito", "El Porvenir", "El Tucán", "La Arboleda", "La María", "Las Marinas", "Los Arrayanes", "San Antonio", "Simón Bolívar", "Urb"],
    },
    "A3-1 Villa Katanga": {
        "estado": "activa",
        "estaciones": ["pedro_ramaya"],
        "barrios": ["Costa de Oro", "El Éxito", "La Arboleda", "Las Trinitarias", "Muvdi", "Urb"],
    },
    "A3-2 Soledad 2000": {
        "estado": "activa",
        "estaciones": ["portal_soledad"],
        "barrios": ["Barrio Normandía", "Bella Murillo", "Ciudadela Metropolitana", "El Oasis", "La Fe", "La Ferruca", "La Inmaculada", "Los Cusules", "Nueva Jerusalén", "Nuevo Milenio", "Soledad Dos Mil", "Tajamar", "Tajamar II", "Urb"],
    },
    "A3-3 Manuela Beltrán": {
        "estado": "activa",
        "estaciones": ["portal_soledad"],
        "barrios": ["Bella Murillo", "Ciudadela Metropolitana", "La Inmaculada", "La Puerta de Oro", "Manuela Beltrán", "Nuevo Milenio", "Soledad 2000", "Villa Adela", "Villa Estadio", "Villa Rosa"],
    },
    "A3-4 Villa Sol": {
        "estado": "suspendida",
        "estaciones": ["portal_soledad"],
        "barrios": ["Bella Jerusalén", "Ciudad Caribe", "Ciudad Transmetro", "La Candelaria", "La Candelaria II", "La Central", "Las Cometas", "Los Loteros", "Nuevo Milenio", "San Vicente", "Urb"],
    },
    "A5-1 Los Robles": {
        "estado": "activa",
        "estaciones": ["pedro_ramaya"],
        "barrios": ["Ciudadela 20 de Julio", "Jardín de Villa Estadio", "Los Almendros", "Los Almendros III", "Los Cerezos", "Los Robles", "Villa Estadio II", "Villa Sevilla"],
    },
    "A5-2 Las Moras": {
        "estado": "activa",
        "estaciones": ["pacho_galan"],
        "barrios": ["Altos de Sevilla", "Los Cedros", "Moras Norte", "Moras Occidente", "Urb"],
    },
    "A5-3 La Central": {
        "estado": "activa",
        "estaciones": ["portal_soledad"],
        "barrios": ["Ciudad Caribe", "Ciudad Transmetro", "Don Bosco", "La Central", "Los Loteros", "Nuevo Milenio", "San Bernardo", "Urb"],
    },
    "A5-4 San Antonio": {
        "estado": "activa",
        "estaciones": ["portal_soledad"],
        "barrios": ["Ciudad Caribe", "Ciudad Salitre", "Ciudad Transmetro", "La Central", "Los Loteros", "Nuevo Milenio", "Urb"],
    },
    "A5-5 Manantial (opera con desvío)": {
        "estado": "activa",
        "estaciones": ["portal_soledad"],
        "barrios": ["Ciudad Caribe", "Ciudad Transmetro", "El Manantial", "Nuevo Milenio", "Urb"],
    },
    "A6-5 Carrizal": {
        "estado": "activa",
        "estaciones": ["buenos_aires"],
        "barrios": ["Buenos Aires", "Carrizal", "Ciudadela 20 de Julio", "El Santuario"],
    },
    "A6-6 Ciudadela": {
        "estado": "activa",
        "estaciones": ["joaquin_barrios"],
        "barrios": ["7 de Abril", "Ciudadela 20 de Julio"],
    },
    "A7-1 Miramar": {
        "estado": "activa",
        "estaciones": ["joe_arroyo"],
        "barrios": ["Altamira", "América", "Ciudad Jardín", "Colombia", "El Poblado", "El Porvenir", "El Tabor", "Granadillo", "La Campiña", "La Cumbre", "Los Alpes", "Los Nogales", "Miramar", "Villa Santos"],
    },
    "A7-3 Carrera 38 (opera con desvío)": {
        "estado": "activa",
        "estaciones": ["la_arenosa", "joe_arroyo"],
        "barrios": ["América", "Betania", "Boston", "Centro", "Ciudad Jardín", "Colombia", "El Porvenir", "El Recreo", "El Rosario", "Las Delicias", "Las Mercedes", "Mercedes Sur", "Olaya"],
    },
    "A7-4 Los Andes": {
        "estado": "activa",
        "estaciones": ["atlantico", "joe_arroyo"],
        "barrios": ["Alfonso López", "América", "Ciudad Jardín", "Ciudadela De La Salud", "Colombia", "El Porvenir", "El Silencio", "El Valle", "Las Colinas", "Las Mercedes", "Los Andes", "Me Quejo", "Mercedes Sur", "Nueva Granada", "Olaya", "Pumarejo", "San Felipe", "San Isidro"],
    },
    "A8-1 Paraíso (opera con desvío)": {
        "estado": "activa",
        "estaciones": ["joe_arroyo"],
        "barrios": ["Alto Prado", "América", "Andalucía", "Colombia", "El Castillo", "El Golf", "El Limoncito", "El Porvenir", "Granadillo", "La Floresta", "Las Tres Ave Marías", "Paraíso", "Riomar", "San Salvador", "San Vicente", "Solaire Norte", "Villa del Este"],
    },
    "A8-2 Vía 40": {
        "estado": "activa",
        "estaciones": ["joe_arroyo"],
        "barrios": ["Alto Prado", "América", "Colombia", "El Golf", "El Porvenir", "La Concepción", "Sector Industrial II - Vía 40", "Villa Country"],
    },
    "A8-3 Prado": {
        "estado": "activa",
        "estaciones": ["parque_cultural", "barrio_abajo", "la_catedral"],
        "barrios": ["Alto Prado", "Barrio Abajo", "Boston", "Centro", "El Prado", "El Rosario", "Montecristo"],
    },
    "A9-3 Buenavista": {
        "estado": "activa",
        "estaciones": ["joe_arroyo"],
        "barrios": ["Altamira", "Alto Prado", "Altos de Riomar", "Altos del Limón", "América", "Buenavista", "Colombia", "El Poblado", "El Porvenir", "El Prado", "Riomar", "San Vicente", "Santa Mónica", "Villa Country", "Villa Santos"],
    },
    "Gran Malecón": {
        "estado": "suspendida temporalmente",
        "estaciones": [],
        "barrios": ["Recorrido: América", "Bellavista", "Colombia", "El Prado", "La Concepción", "San Francisco", "Sector Industrial II - Vía 40"],
    },
    "U-30 Universidades (opera con desvío)": {
        "estado": "activa",
        "estaciones": ["joe_arroyo"],
        "barrios": ["de Altamira", "América", "Buenavista", "Colombia", "El Poblado", "El Porvenir", "Granadillo", "La Campiña", "Miramar", "Paseo de la Castellana", "San Vicente", "Villa Santos", "Villa Campestre", "Ciudad Mallorquín"],
    },
    "A3-41 Villa Karla": {
        "estado": "activa",
        "estaciones": ["portal_soledad"],
        "barrios": ["Ciudad Caribe", "Ciudad Transmetro", "La Candelaria II", "La Central"],
    },
    "Ruta Navideña": {
        "estado": "suspendida temporalmente",
        "estaciones": [],
        "barrios": [],
    },
    "A9-4 Carrera 46 / fines de semana": {
        "estado": "activa",
        "estaciones": [],
        "barrios": ["como Altamira", "América", "Buenavista", "Colombia", "El Poblado", "El Porvenir", "Granadillo", "La Campiña", "Miramar", "Paseo de la Castellana", "San Vicente", "Villa Santos", "Ciudad Mallorquín"],
    },
    "Ruta Chévere": {
        "estado": "activa",
        "estaciones": [],
        "barrios": [],
    },
    "A4-1 Malambo": {
        "estado": "suspendida temporalmente",
        "estaciones": [],
        "barrios": [],
    },
}

# ---------------------------------------------------------------------------
# 4) PARAMETROS DEL MODELO DE COSTOS
#    "ute" = unidad de tiempo estimado (aprox. 1 minuto). Se usan para
#    comparar opciones entre si. Cambiar estos numeros cambia el criterio.
# ---------------------------------------------------------------------------
PARAMETROS = {
    "avance": 1.0,          # costo por cada estacion que el bus recorre
    "parada": 0.5,          # costo extra por cada parada que hace el bus
    "transbordo": 2.0,      # penalizacion por cambiar de ruta
    "espera_inicial": 2.0,  # espera estimada antes de abordar el primer bus
    "alimentadora": 2.0,    # costo estimado del tramo en una alimentadora
}

# ---------------------------------------------------------------------------
# FUNCIONES AUXILIARES
# ---------------------------------------------------------------------------

def a_minutos(texto):
    """Convierte una hora escrita como '7', '7:05', '07:00' o '0700' a
    minutos desde medianoche. Devuelve None si el formato no es valido."""
    t = texto.strip().replace(".", "")
    if ":" in t:
        partes = t.split(":")
        if len(partes) != 2 or not partes[0].isdigit() or not partes[1].isdigit():
            return None
        horas, minutos = int(partes[0]), int(partes[1])
    elif t.isdigit() and len(t) <= 2:          # '7' -> 7:00 a. m.
        horas, minutos = int(t), 0
    elif t.isdigit() and len(t) == 4:          # '0700' -> 7:00 a. m.
        horas, minutos = int(t[:2]), int(t[2:])
    else:
        return None
    if 0 <= horas <= 23 and 0 <= minutos <= 59:
        return horas * 60 + minutos
    return None

def hhmm(minutos):
    """Convierte minutos desde medianoche al texto 'HH:MM'."""
    return f"{minutos // 60:02d}:{minutos % 60:02d}"

def nombre(clave_estacion):
    """Devuelve el nombre oficial de una estacion dada su clave."""
    return ESTACIONES[clave_estacion][0]

# ---------------------------------------------------------------------------
# REGLA 1 y REGLA 2: disponibilidad de una ruta (estado + franja horaria).
# ---------------------------------------------------------------------------
def esta_disponible(clave_ruta, minuto):
    """True si la ruta presta servicio a esa hora de un dia laboral."""
    ruta = RUTAS[clave_ruta]
    if ruta["estado"] != "activa":              # REGLA 1: ¿esta suspendida?
        return False
    for inicio, fin in ruta["horarios"]:        # REGLA 2: ¿cae en una franja?
        if inicio <= minuto < fin:
            return True
    return False

# ---------------------------------------------------------------------------
# Mapa fisico del corredor (para contar cuantas estaciones se salta un expres)
# ---------------------------------------------------------------------------
def construir_vecinos():
    """Dos estaciones son 'vecinas' si son paradas consecutivas de alguna
    ruta CORRIENTE (las corrientes paran en todas, asi que entre todas
    dibujan la red fisica completa)."""
    vecinos = {}
    for ruta in RUTAS.values():
        if ruta["tipo"] != "corriente":
            continue
        paradas = ruta["paradas"]
        for i in range(len(paradas) - 1):
            a, b = paradas[i], paradas[i + 1]
            vecinos.setdefault(a, set()).add(b)
            vecinos.setdefault(b, set()).add(a)
    return vecinos

VECINOS = construir_vecinos()

def distancia_fisica(a, b):
    """Numero de saltos entre estaciones vecinas para ir de a hasta b
    (busqueda simple en anchura). Sirve para contar las estaciones que
    un expreso se salta entre dos paradas suyas."""
    if a == b:
        return 0
    vistos = {a}
    cola = [(a, 0)]
    while cola:
        actual, d = cola.pop(0)
        for vecino in VECINOS.get(actual, ()):
            if vecino == b:
                return d + 1
            if vecino not in vistos:
                vistos.add(vecino)
                cola.append((vecino, d + 1))
    return None

# ---------------------------------------------------------------------------
# REGLA 4: costo de un tramo.
#   Cada salto entre paradas de la ruta cuesta (estaciones saltadas + 1) *
#   avance + parada. Un EXPRES se salta estaciones, asi que en hora pico
#   resulta mejor que ir parando en todas.
# ---------------------------------------------------------------------------
def costo_tramo(clave_ruta, desde, hasta):
    """Devuelve (costo, numero de paradas) de viajar sin paradas en la ruta
    desde una parada hasta otra posterior."""
    paradas = RUTAS[clave_ruta]["paradas"]
    i = paradas.index(desde)
    j = paradas.index(hasta)
    costo = 0.0
    for k in range(i, j):
        a, b = paradas[k], paradas[k + 1]      # cada salto entre paradas
        saltadas = distancia_fisica(a, b) - 1  # estaciones que se salta
        costo += (saltadas + 1) * PARAMETROS["avance"]
        costo += PARAMETROS["parada"]          # esta parada si la paga
    return costo, (j - i)

# ---------------------------------------------------------------------------
# REGLA 3: busqueda de combinaciones de tramos.
#   El bus solo avanza en su sentido (solo paradas posteriores a la subida).
#   Se prueban combinaciones de hasta 3 tramos (2 transbordos), suficiente
#   para esta red de dos troncales.
# ---------------------------------------------------------------------------
def buscar_tramos(origen, destinos, disponibles, max_tramos=3, usadas=frozenset()):
    """Todas las formas de llegar desde 'origen' hasta el 'destino' usando las rutas disponibles. Devuelve una lista de
    itinerarios; cada itinerario es una lista de tramos ruta/desde/hasta."""
    resultados = []
    for clave in disponibles:
        if clave in usadas:                  # no repetir una ruta ya usada
            continue
        paradas = RUTAS[clave]["paradas"]
        if origen not in paradas:             # la ruta no pasa por 'origen'
            continue
        i = paradas.index(origen)
        for j in range(i + 1, len(paradas)):       # REGLA 3: solo hacia adelante
            llegada = paradas[j]
            tramo = {"ruta": clave, "desde": origen, "hasta": llegada}
            if llegada in destinos:
                resultados.append([tramo])         # se llego al destino
            elif max_tramos > 1:                   # probar con transbordo
                for resto in buscar_tramos(llegada, destinos, disponibles,
                                           max_tramos - 1, usadas | {clave}):
                    resultados.append([tramo] + resto)
    return resultados

def evaluar(troncal, alim_origen, alim_destino):
    """Calcula (costo, transbordos, paradas) de un viaje candidato."""
    costo = PARAMETROS["espera_inicial"]            # una sola espera inicial
    paradas = 0
    for tramo in troncal:
        c, p = costo_tramo(tramo["ruta"], tramo["desde"], tramo["hasta"])
        costo += c
        paradas += p
    n_alim = (1 if alim_origen else 0) + (1 if alim_destino else 0)
    costo += n_alim * PARAMETROS["alimentadora"]
    buses = len(troncal) + n_alim
    transbordos = max(buses - 1, 0)               # cambios de bus
    costo += transbordos * PARAMETROS["transbordo"]
    return costo, transbordos, paradas

# ---------------------------------------------------------------------------
# REGLA 7 y REGLA 8: resolver el viaje completo.
# ---------------------------------------------------------------------------
def resolver_viaje(origen, destino, minuto):
    """Devuelve (resultado, mensaje):
       - resultado: el mejor viaje encontrado (dict) o None;
       - mensaje: la explicacion cuando no hay viaje posible (REGLA 8)."""
    disponibles = [c for c in RUTAS if esta_disponible(c, minuto)]

    # --- punto de ORIGEN (REGLA 5 si es estación, REGLA 6 si es alimentadora) ---
    if origen[0] == "estacion":
        estaciones_origen, alim_origen = [origen[1]], None
    else:
        info = ALIMENTADORAS[origen[1]]
        if info["estado"] != "activa":           # REGLA 1 para alimentadoras
            return None, (f"la alimentadora {origen[1]} está {info['estado']}: "
                          "no hay servicio desde ese barrio.")
        if not info["estaciones"]:
            return None, (f"la alimentadora {origen[1]} no tiene punto de "
                          "transbordo con la troncal.")
        estaciones_origen, alim_origen = info["estaciones"], origen[1]

    # --- punto de DESTINO (REGLA 5 / REGLA 6) ---
    if destino[0] == "estacion":
        estaciones_destino, alim_destino = [destino[1]], None
    else:
        info = ALIMENTADORAS[destino[1]]
        if info["estado"] != "activa":
            return None, (f"la alimentadora {destino[1]} está {info['estado']}: "
                          "no hay servicio hacia ese barrio.")
        if not info["estaciones"]:
            return None, (f"la alimentadora {destino[1]} no tiene punto de "
                          "transbordo con la troncal.")
        estaciones_destino, alim_destino = info["estaciones"], destino[1]

    # --- combinar cada estacion posible de origen con cada una de destino ---
    candidatos = []
    for so in estaciones_origen:
        for sd in estaciones_destino:
            if so == sd:
                candidatos.append({"troncal": [], "so": so, "sd": sd})
            else:
                for troncal in buscar_tramos(so, {sd}, disponibles):
                    candidatos.append({"troncal": troncal, "so": so, "sd": sd})

    if not candidatos:                           # REGLA 8
        if not disponibles:
            return None, (f"a las {hhmm(minuto)} no hay servicio: el sistema "
                          "opera aprox. de 05:00 a 22:00 en día laboral.")
        return None, "no encontré conexión posible entre esos dos puntos a esa hora."

    # Numeros de cada candidato (para poder compararlos)
    for cand in candidatos:
        cand["alim_origen"] = alim_origen
        cand["alim_destino"] = alim_destino
        cand["costo"], cand["transbordos"], cand["paradas"] = evaluar(
            cand["troncal"], alim_origen, alim_destino)
        cand["etiqueta"] = tuple(t["ruta"] for t in cand["troncal"])

    # REGLA 7: mejor costo; si empatan, menos transbordos; luego menos
    # paradas; y por ultimo orden alfabetico (resultado siempre igual).
    mejor = None
    for cand in candidatos:
        orden = (cand["costo"], cand["transbordos"], cand["paradas"], cand["etiqueta"])
        if mejor is None or orden < mejor["orden"]:
            cand["orden"] = orden
            mejor = cand
    return mejor, None

# ---------------------------------------------------------------------------
# PRESENTACION DEL RESULTADO
# ---------------------------------------------------------------------------
def describir_viaje(res, minuto):
    """Construye el texto del itinerario elegido, paso a paso."""
    pasos = []                                   # cada paso = un bus que se toma
    if res["alim_origen"]:                       # REGLA 6: primer tramo
        pasos.append({
            "titulo": f"Alimentadora {res['alim_origen']}",
            "desde": "tu barrio",
            "hasta": nombre(res['so']),
            "detalle": "tramo en alimentadora, costo estimado "
                       f"{PARAMETROS['alimentadora']:.1f} ute",
        })
    for tramo in res["troncal"]:                 # tramos por la red troncal
        ruta = RUTAS[tramo["ruta"]]
        tipo = "exprés" if ruta["tipo"] == "expreso" else "corriente"
        costo, n_paradas = costo_tramo(tramo["ruta"], tramo["desde"], tramo["hasta"])
        pasos.append({
            "titulo": f"{ruta['nombre']} ({tipo})",
            "desde": nombre(tramo['desde']),
            "hasta": nombre(tramo['hasta']),
            "detalle": f"{n_paradas} parada(s), {costo:.1f} ute",
        })
    if res["alim_destino"]:                      # REGLA 6: ultimo tramo
        pasos.append({
            "titulo": f"Alimentadora {res['alim_destino']}",
            "desde": nombre(res['sd']),
            "hasta": "tu barrio (destino)",
            "detalle": "tramo en alimentadora, costo estimado "
                       f"{PARAMETROS['alimentadora']:.1f} ute",
        })

    lineas = ["", "=============== MEJOR RUTA ENCONTRADA ===============",
              f"Día laboral, saliendo a las {hhmm(minuto)}.", ""]
    for k, paso in enumerate(pasos, start=1):
        lineas.append(f"  {k}) {paso['titulo']}:  {paso['desde']} -> {paso['hasta']}")
        lineas.append(f"       {paso['detalle']}")
        if k < len(pasos):                       # entre un bus y el otro: transbordo
            lineas.append(f"       -- transbordo en {paso['hasta']} "
                          f"({PARAMETROS['transbordo']:.1f} ute) --")
    lineas.append("")
    lineas.append(f"TOTAL: {res['paradas']} parada(s) | {res['transbordos']} transbordo(s) | "
                  f"costo estimado {res['costo']:.1f} ute")
    lineas.append("(1 ute ~ 1 minuto aprox.; el costo es una estimación para comparar opciones)")
    return lineas

# ---------------------------------------------------------------------------
# INTERFAZ POR CONSOLA: menú numerado ("select") + input()/print()
# ---------------------------------------------------------------------------

def construir_opciones():
    """Arma la lista NUMERADA de opciones del menú: primero las 17
    estaciones de la troncal y después las 29 rutas alimentadoras.
    Cada opción es (texto principal, texto extra o None, punto de viaje)."""
    opciones = []
    for clave, (nom, _troncal, _orden) in ESTACIONES.items():
        opciones.append((nom, None, ("estacion", clave, nom)))
    for clave, info in ALIMENTADORAS.items():
        marca = "" if info["estado"] == "activa" else f"   [{info['estado'].upper()}]"
        if info["estado"] != "activa" and info["estado"].upper() in clave.upper():
            marca = ""      # el nombre ya lo dice (evita repetirlo)
        if info["estaciones"]:
            conecta = ", ".join(nombre(s) for s in info["estaciones"])
        else:
            conecta = "sin transbordo troncal publicado"
        extra = None
        if info["barrios"]:
            extra = "barrios: " + ", ".join(info["barrios"][:4])
            if len(info["barrios"]) > 4:
                extra += ", ..."
        opciones.append((f"{clave}{marca}   (conecta en: {conecta})",
                         extra, ("alimentadora", clave, clave)))
    return opciones


OPCIONES = construir_opciones()      # se arma una sola vez al iniciar


def mostrar_menu():
    """Muestra el menú numerado ('select'): estaciones y alimentadoras."""
    print("=" * 68)
    print("ELIGE EL ORIGEN Y EL DESTINO POR SU NÚMERO (0 para salir).")
    print()
    print("ESTACIONES DE LA RED TRONCAL:")
    for i, (principal, _extra, punto) in enumerate(OPCIONES, start=1):
        if punto[0] == "estacion":
            print(f"   {i:>2}. {principal}")
    print()
    print("RUTAS ALIMENTADORAS (conectan los barrios con la troncal):")
    for i, (principal, extra, punto) in enumerate(OPCIONES, start=1):
        if punto[0] == "alimentadora":
            print(f"   {i:>2}. {principal}")
            if extra:
                print(f"       {extra}")
    print("=" * 68)


def pedir_seleccion(pregunta):
    """Pide una opción del menú por su número (0 = salir) y la valida.
    Devuelve el punto elegido o la palabra 'salir'."""
    total = len(OPCIONES)
    while True:
        respuesta = input(pregunta).strip()
        if respuesta == "0":
            return "salir"
        if respuesta.isdigit() and 1 <= int(respuesta) <= total:
            return OPCIONES[int(respuesta) - 1][2]
        print(f"   Opción no válida: escribe un número entre 1 y {total} (o 0 para salir).")


def pedir_hora():
    """Pide la hora del viaje (OPCIONAL: si escribe Enter, usa la hora actual)."""
    while True:
        respuesta = input("¿A qué hora viajas? (ej. 07:00 / Enter = hora actual): ").strip()
        if respuesta == "":
            ahora = datetime.now()
            minuto = ahora.hour * 60 + ahora.minute
            print(f"   Usaré la hora actual: {hhmm(minuto)}")
            return minuto
        minuto = a_minutos(respuesta)
        if minuto is not None:
            return minuto
        print("   Hora no válida: escribe por ejemplo 7, 07:00 o 0700.")


def main():
    """Punto de entrada: presentación, menú numerado y bucle de consultas."""
    while True:
        print()
        print("=" * 68)
        print("      SISTEMA INTELIGENTE DE RUTAS - TRANSMETRO BARRANQUILLA")
        print("=" * 68)
        print("Te ayudo a encontrar la mejor ruta entre dos puntos del sistema.")
        print("Elige el ORIGEN y el DESTINO por su número en el menú de abajo.")
        print("(Datos oficiales de transmetro.gov.co; se asume día laboral)")
        mostrar_menu()    
        origen = pedir_seleccion(f"\nSelecciona el ORIGEN (1 a {len(OPCIONES)}, 0 para salir): ")
        if origen == "salir":
            print("¡Hasta luego!")
            return
        destino = pedir_seleccion(f"Selecciona el DESTINO (1 a {len(OPCIONES)}, 0 para salir): ")
        if destino == "salir":
            print("¡Hasta luego!")
            return

        if origen[0] == destino[0] and origen[1] == destino[1]:
            print("\nYa estás en ese punto: ¡no necesitas moverte!")
        else:
            minuto = pedir_hora()
            mejor, mensaje = resolver_viaje(origen, destino, minuto)
            if mejor is None:
                print("\nNo hay ruta: " + mensaje)
            else:
                for linea in describir_viaje(mejor, minuto):
                    print(linea)

        otra = input("\n¿Quieres hacer otra consulta? (s/N): ").strip().lower()
        if otra != "s":
            print("\n¡Buen viaje!")
            return


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\n(Programa terminado)")


# ============================== FIN DEL PROGRAMA =============================
