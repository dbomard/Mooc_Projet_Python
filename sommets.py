def calculate_points(center_point, rayon):
    """
    Calcule les coordonnées des points de l'hexagone et les renvoie sous formes d'objet
    de 6 tuples
    Entrées :
        center_point: coordonnées du centre
        rayon: rayon entre le centre et les points
     Sortie :
        sommets : objet contenant les 6 couples de points
    """

    # initialisation d'un objet de 6 tuples
    sommets = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

    # calcul et remplissage des coordonnées des 6 sommets de l'hexagone
    for i in range(len(sommets)):
        sommets[i]=(center_point[0]+cos(2*pi/6*i)*rayon, center_point[1]+sin(2*pi/6*i)*rayon)

    return sommets