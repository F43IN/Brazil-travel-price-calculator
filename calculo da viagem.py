coordenadas_estados = {
    'Acre': (-9.0238, -70.812),
    'Alagoas': (-9.5713, -36.782),
    'Amapá': (1.415, -51.602),
    'Amazonas': (-3.4168, -65.8561),
    'Bahia': (-12.5797, -41.7007),
    'Ceará': (-5.4984, -39.3206),
    'Distrito Federal': (-15.8267, -47.9218),
    'Espírito Santo': (-19.1834, -40.3089),
    'Goiás': (-15.827, -49.8362),
    'Maranhão': (-4.9609, -45.2744),
    'Mato Grosso': (-12.6819, -56.9211),
    'Mato Grosso do Sul': (-20.7722, -54.7852),
    'Minas Gerais': (-18.5122, -44.555),
    'Pará': (-3.4168, -52.3168),
    'Paraíba': (-7.2395, -36.7819),
    'Paraná': (-24.8916, -51.9054),
    'Pernambuco': (-8.8137, -36.9541),
    'Piauí': (-7.7183, -42.7289),
    'Rio de Janeiro': (-22.9068, -43.1729),
    'Rio Grande do Norte': (-5.7945, -36.9541),
    'Rio Grande do Sul': (-30.0346, -51.2177),
    'Rondônia': (-10.9472, -62.8278),
    'Roraima': (2.7376, -62.0751),
    'Santa Catarina': (-27.5954, -48.548),
    'São Paulo': (-23.5505, -46.6333),
    'Sergipe': (-10.5741, -37.3857),
    'Tocantins': (-10.1753, -48.2982)
}


from math import radians, sin, cos, sqrt, atan2

price1 = 0.5    # price for first distance
price2 = 0.45   # price for second distance

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth's radius in km

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def obter_coordenadas(estado):
    return coordenadas_estados.get(estado)

def calcular_distancia(estado1, estado2):
    coords1 = obter_coordenadas(estado1)
    coords2 = obter_coordenadas(estado2)

    if not coords1 or not coords2:
        return None

    return haversine(coords1[0], coords1[1], coords2[0], coords2[1])

def main():
    estado1 = input("Digite o nome do primeiro estado: ") # enter the name of the place of departure
    estado2 = input("Digite o nome do segundo estado: ")  # enter the name of the place of arrival

    distancia = calcular_distancia(estado1, estado2)

    if distancia <= 200:    # enter the minimum distance for the first trip price
        custo = distancia * price1
    else:
        custo = distancia * price2

    if distancia is None:
        print("Um ou ambos os estados fornecidos são inválidos.")    # message if the name is not in the dictionary included in the code
    else:
        print(f"A distância entre {estado1} e {estado2} é de {distancia:.2f} km e o valor é R${custo:.2f}.")

if __name__ == "__main__":
    main()
