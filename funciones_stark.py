from data_stark import*


# Utilizo una función para encontrar al mínimo de una lista de datos.
####################################################################
def buscamos_minimo(lista:list):
    '''Buscamos el minimo dentro de una lista. Retornamos otra lista con los minimos encontrados.'''
    minimo = lista[0]
    min_list = []
    if isinstance(lista, list) and len(lista) > 0:
        for dato in lista:
            if dato < minimo:
                minimo = dato
        for data in lista:
            if data == minimo:
                min_list.append(data)
    return min_list

# Función para obtener cualquier tipo de dato por medio de su key.
#################################################################
def obtener_dato(lista:dict, key:str):
    '''Obtiene un dato en particular dentro de una lista de diccionarios y retorna los mismos en una lista'''
    dato_heroe = []
    for heroe in lista:
        if key in heroe:
            dato = heroe.get(key)
            dato_heroe.append(dato)
    return dato_heroe

heroes = obtener_dato(lista_personajes, "nombre")
# Algoritmo para devolver los datos ordenados.
##############################################
def ordenar_dato(lista:list):
    '''Recibe una lista como argumento y la retorna ordenada de manera ascendente.'''
    return sorted(lista)

 
'''A. Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por
Nombre de manera ascendente.'''



# heroes_ordenados = ordenar_dato(heroes)
# print("\n".join(heroes_ordenados))

'''B. Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de
género M.'''


# Algoritmo para hallar y listar al héroe menos fuerte.
######################################################
def lista_de_menos_fuertes(lista: list[dict]) -> list[dict]:
    '''Retorna una lista de héroes masculinos con la menor fuerza.'''
    lista_fuerza = []
    nombre_heroe = []

    for heroe in lista:
        if heroe.get("genero") == "M" and "fuerza" in heroe:
            try:
                fuerza_heroes = int(float(heroe.get("fuerza")))
                nombre = heroe.get("nombre")
                lista_fuerza.append(fuerza_heroes)
                nombre_heroe.append(nombre)
            except ValueError:
                continue 

    # Encontrar la menor fuerza
    if lista_fuerza:
        minima_fuerza = min(lista_fuerza)
        mas_debiles = [{"nombre": name, "fuerza": debil} for name, debil in zip(nombre_heroe, lista_fuerza) if debil == minima_fuerza]
    else:
        mas_debiles = []

    return mas_debiles

heroes_mas_debiles = lista_de_menos_fuertes(lista_personajes)



## DESARROLLO DE UNA FUNCIÓN PARA LISTAR UN CONJUNTO DE DATOS DENTRO DE UNA LISTA DE DICCIONARIOS A PARTIR DE SUS KEYS.

def listar_heroes_agrupados(lista: list[dict], key_agrupacion: str, key_nombre: str) -> dict:
    '''
    Busca datos dentro de una lista de diccionarios a partir de sus keys.

    Args:
        lista list[dict]: lista de diccionarios.
        key_agrupacion: clave del diccionario utilizada para agrupar los datos en un grupo especificado.
        key_nombre: clave del diccionario para obtener el nombre del personaje.
    
    Returns:
        Retorna un diccionario con los datos agrupados por la clave key_agrupacion y ordenados por la clave
        key_nombre.

    '''

    heroes_agrupados = {}

    for heroe in lista:
        if key_agrupacion in heroe:
            valor_agrupacion = heroe[key_agrupacion]
            nombre_heroe = heroe[key_nombre]

            if valor_agrupacion in heroes_agrupados:
                heroes_agrupados[valor_agrupacion]["cantidad"] += 1
                heroes_agrupados[valor_agrupacion]["nombres"].append(nombre_heroe)
            else:
                heroes_agrupados[valor_agrupacion] = {"cantidad": 1, "nombres": [nombre_heroe]}

    heroes_agrupados_ordenados = sorted(heroes_agrupados.items(), key=lambda x: x[0])
    for valor_agrupacion, datos in heroes_agrupados_ordenados:
        heroes_agrupados[valor_agrupacion]["nombres"] = sorted(datos["nombres"])

    return dict(heroes_agrupados_ordenados)

agrupar_heroes = listar_heroes_agrupados(lista_personajes, "peso","nombre")






def calcular_promedio(notas: list) -> float:
    """Calcula el promedio de una lista de notas."""
    if len(notas) > 0:
        return sum(notas) / len(notas)
    else:
        return 0.0


## ALGORITMO PARA HALLAR NOMBRE Y PESO DE UN HÉROE.
def nombre_peso(nombre:str, peso:str)->dict:
    name = obtener_dato(lista_personajes, nombre)
    peso_heroe = obtener_dato(lista_personajes, peso)
    return dict(zip(name, peso_heroe))

# name_peso = nombre_peso("nombre", "peso")
# for heroe, pes in name_peso.items():
#     print("--------")
#     print(f"Nombre: {heroe}\n Peso: {pes}" )

## FUNCIÓN PARA OBTENER LA FUERZA DE LAS HEROÍNAS.
def fuerzas_femeninas(lista:list[dict]):
    heroinas = [heroe for heroe in lista if heroe.get("genero") == "F"]
    heroina_name = obtener_dato(heroinas, "nombre")
    fuerza_heroina = obtener_dato(heroinas, "fuerza")

    fuerza_heroina = [int(fuerza) for fuerza in fuerza_heroina]

    promedio = calcular_promedio(fuerza_heroina)

    return heroina_name, fuerza_heroina, promedio

    #         nombres_heroinas, heroina_fuerzas, promedio_fuerza = fuerzas_femeninas(lista_personajes)
    #         for nombre, fuerza in zip(nombres_heroinas, heroina_fuerzas):
    #             print("----")
    #             print(f"Nombre: {nombre}\nFuerza: {fuerza}")
    #             print()
    #         print(f"Promedio de las fuerzas Femeninas: {promedio_fuerza}")



def nombre_peso_heroe(lista, nombre_clave, peso_clave):
    nombres = obtener_dato(lista, nombre_clave)
    pesos = obtener_dato(lista, peso_clave)
    return nombres, pesos

def heroes_mas_fuertes_que_promedio_femenino(lista: list[dict]):
    _, _, promedio_fuerza = fuerzas_femeninas(lista)
    
    heroes_fuertes = [heroe for heroe in lista if int(heroe.get("fuerza", 0)) > promedio_fuerza]
    nombres, pesos = nombre_peso_heroe(heroes_fuertes,"nombre", "peso")
    
    return nombres, pesos



def obtener_dato_heroe(lista, clave):
    return [float(personaje[clave]) for personaje in lista]


calc_imc_ = lambda peso, altura: peso / altura**2 if altura > 0 else 0

