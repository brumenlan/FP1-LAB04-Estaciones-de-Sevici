from collections import namedtuple

EstacionSevici = namedtuple("EstacionSevici", 
    "nombre, direccion, latitud, longitud, capacidad, puestos_libres, bicicletas_disponibles")

def selecciona_color(estacion:EstacionSevici) -> str:
    """
    Devuelve el color en que debe pintarse cada estación según su disponibilidad.

    Parámetros:
    estacion: EstacionSevici

    Devuelve:
    str: "green", "orange", "red" o "gray"
    """
    # TODO: Ejercicio 1
    if estacion.capacidad == 0:
        return "gray"
    disponibilidad = estacion.bicicletas_disponibles / estacion.capacidad
    if disponibilidad >= 2/3:
        return "green"
    elif disponibilidad >= 1/3:
        return "orange"
    elif disponibilidad > 0:
        return "red"
    else:
        return "gray"

def calcula_estadisticas(estaciones: list[EstacionSevici]) -> tuple[int, int, float, int]:
    """
    Calcula estadísticas de las estaciones.
    Parametros:
    estaciones: lista de EstacionSevici
    Devuelve:
    tupla con (total de bicicletas libres, total de capacidad, porcentaje de ocupación, total de estaciones)
    """
    # TODO: Ejercicio 2
    total_bicis = 0
    total_capacidad = 0
    total_estaciones = 0
    for estacion in estaciones:
        total_bicis += estacion.bicicletas_disponibles
        total_capacidad += estacion.capacidad
        total_estaciones += 1
    porcentaje_ocupacion = ((total_capacidad - total_bicis) / total_capacidad) * 100

    return (total_bicis, total_capacidad, porcentaje_ocupacion, total_estaciones)

def busca_estaciones_direccion(estaciones: list[EstacionSevici], direccion_parcial: str) -> list[EstacionSevici]:
    """
    Busca las estaciones que contengan en su dirección (subcadena, sin distinguir mayúsculas/minúsculas) la dirección parcial dada.    

    Parametros:
    estaciones: lista de EstacionSevici
    direccion_parcial: subcadena a buscar en la dirección de las estaciones

    Devuelve:
    lista de EstacionSevici que cumplen el criterio
    """
    # TODO: Ejercicio 3
    lista = []
    direccion_parcial_min = direccion_parcial.lower()
    for estacion in estaciones:
        direccion_lower = estacion.direccion.lower()
        if direccion_parcial_min in direccion_lower:
            lista.append(estacion)

    return lista

def busca_estaciones_con_disponibilidad(estaciones:list[EstacionSevici], min_disponibilidad: float = 0.5) -> list[EstacionSevici]:
    """
    Devuelve una lista de EstacionSevici con al menos el porcentaje mínimo de bicicletas disponible
    indicado.

    Parametros:
    estaciones: lista de EstacionSevici
    min_disponibilidad: porcentaje mínimo de bicicletas disponibles (0.0 a 1.0)
    
    Devuelve:
    lista de EstacionSevici
    """
    # TODO: Ejercicio 4
    lista = []
    for estacion in estaciones:
        if estacion.capacidad > 0:
            disponibilidad = estacion.bicicletas_disponibles / estacion.capacidad
            if disponibilidad >= min_disponibilidad:
                lista.append(estacion)
    return lista

def calcula_distancia(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    """
    Calcula la distancia euclídea entre dos puntos (latitud, longitud).

    Parámetros:
    p1: tupla (latitud, longitud) del primer punto
    p2: tupla (latitud, longitud) del segundo punto

    Devuelve:
    float: distancia euclídea entre los dos puntos
    """
    # TODO: Ejercicio 5
    return abs(abs(p2[0] - p1[0])**2 - abs(p2[1] - p2[1]))**2 ** 0.5

def busca_estacion_mas_cercana(estaciones:list[EstacionSevici], punto:tuple[float, float]) -> EstacionSevici | None:
    """
    Devuelve la estación más cercana al punto dado (latitud, longitud) que tenga al menos una bicicleta disponible.
    
    Parametros:
    estaciones: lista de EstacionSevici
    punto: tupla (latitud, longitud)

    Devuelve:
    EstacionSevici más cercana con al menos una bicicleta disponible, o None si no hay ninguna.
    """ 
    # TODO: Ejercicio 5
    lista = []
    for estacion in estaciones:
        if estacion.bicicletas_disponibles > 0:
            coords = (estacion.latitud, estacion. longitud)
            dist = calcula_distancia(punto, coords)
            lista.append([dist, estacion])
        est_cercana = min(lista, key = lambda x: x[0])[1]
    return est_cercana



def calcula_ruta(estaciones:list[EstacionSevici], origen:tuple[float, float], destino:tuple[float, float]) -> tuple[EstacionSevici | None, EstacionSevici | None]   :
    """
    Devuelve las estaciones más cercanas al punto de origen y destino dados, que tengan al menos una bicicleta disponible.

    Parametros: 
    estaciones: lista de EstacionSevici
    origen: tupla (latitud, longitud) del punto de origen
    destino: tupla (latitud, longitud) del punto de destino

    Devuelve:
    tupla con (estacion_origen, estacion_destino)
    """
    # TODO: Ejercicio 5
    return (busca_estacion_mas_cercana(estaciones, origen), busca_estacion_mas_cercana(estaciones, destino))