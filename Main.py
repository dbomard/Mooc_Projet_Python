from math import pi, sin, cos, sqrt, acos, asin
import turtle


def calculate_sommets(center_point, rayon):
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
    sommets = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

    # calcul et remplissage des coordonnées des 6 sommets de l'hexagone
    for i in range(len(sommets)):
        sommets[i] = (center_point[0] + cos(2 * pi / 6 * i) * rayon, center_point[1] + sin(2 * pi / 6 * i) * rayon, 0)

    return sommets


def dessine_pave(point1, point2, point3, point4, couleur):
    """
    peint un pavé ayant pour sommets les 4 points p1 à p4 dont les coordonnées dans le plan sont
    représentés sous forme de tuples(x, y, z)
    Entrées :
        p1 : point n°1
        p2 : point n°2
        p3 : point n°3
        p4 : point n°4
        couleur : couleur du pavé

    """
    turtle.up()
    turtle.goto(point1[0], point1[1])  # déplacer la tortue au point n°1
    turtle.down()  # commencer à dessiner
    turtle.color(couleur)  # changer la couleur de crayon
    turtle.begin_fill()  # commencer à remplir
    turtle.goto(point2[0], point2[1])  # relier tous les points
    turtle.goto(point3[0], point3[1])
    turtle.goto(point4[0], point4[1])
    turtle.goto(point1[0], point1[1])
    turtle.end_fill()  # clôturer et remplir le pavé
    turtle.up()  # lever le crayon


def hexagone(point, longueur, col, centre, rayon):
    """
    La fonction peint un hexagone déformé en traçant des lignes droites entre le centre et les extrémités
    dont la position est calculée avec la fonction 'deformation'
    Entrées:
        point : coordonnées du centre de l'hexagone sous forme d'un tripe tuple (x, y, z)
        longueur : distance entre le centre et les sommets de l'hexagone
        col : les 3 couleurs utilisées pour les 3 pavés, sous forme d'un triple tuple (col1, col2, col3)
        centre : centre de la sphère de déformation sous forme d'un triple tuple (c_x, c_y, c_z)
        rayon : rayon de la sphère de déformation
    """

    # calcul des coordonnées des sommets de l'hexagone par la fonction 'calculate_sommets'
    points_sommets = calculate_sommets(point, longueur)

    # transformation de la déformation des coordonnées des sommets selon la sphère
    point_centre = deformation(point, centre, rayon)  # d'abord le point central de l'hexagone
    for p in range(6):
        points_sommets[p] = deformation(points_sommets[p], centre, rayon)  # puis les 6 sommets

    # dessins des pavés avec la fonction 'dessine_pave'
    dessine_pave(point_centre, points_sommets[2], points_sommets[1], points_sommets[0], col[0])  # dessin du pavé n°1
    dessine_pave(point_centre, points_sommets[0], points_sommets[5], points_sommets[4], col[1])  # dessin du pavé n°2
    dessine_pave(point_centre, points_sommets[4], points_sommets[3], points_sommets[2], col[2])  # dessin du pavé n°3


def deformation(p, centre, rayon):
    """ Calcul des coordonnées d'un point suite à la déformation
        engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer
             (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage
             à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon ** 2 > zc ** 2:
        zc = zc if zc <= 0 else -zc
        r = sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)  # distance horizontale
        # depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = sqrt(rayon ** 2 - zc ** 2)  # rayon de la partie
        # émergée de la sphère
        rprim = rayon * sin(acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:  # calcul de la déformation
            # dans les autres cas
            xprim = xc + (x - xc) * rprim / r  # les nouvelles coordonnées
            # sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = asin(rprim / rayon)
            zprim = zc + rayon * cos(beta)
            if centre[2] > 0:
                zprim = -zprim
    return xprim, yprim, zprim


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """
    Dessine le pavage en commençant en bas à gauche
    inf_gauche: tuple : coordonnées du coin inférieur gauche
    sup_droit: tuple : coordonnées du coin suprieur droit
    longueur: longueur des arêtes
    col: tuple triple : les 3 couleurs utilisées
    centre: tuple triple : coordonnées du centre du cercle de déformation
    rayon: rayon du cercle de déformation
    """
    turtle.reset()  # On commence par initialiser 'turtle'
    turtle.speed('fastest')  # sélectionne la vitesse maximum pour les tracés
    coo_centre_y = inf_gauche[1] + longueur  # ordonnée du centre du premier hexagone tracé en bas à gauche
    ligne = 0  # Cette variable sera incrémentée à chaque novelle ligne afin de savoir si la ligne est paire ou impaire

    # calcul des pas de décalage entre les colonnes et les lignes
    ystep = int(sin(pi / 3) * longueur)
    xstep = longueur * 3

    # boucle des lignes
    for y in range(coo_centre_y, sup_droit[1] - longueur, ystep):
        if ligne % 2:  # détecte si la ligne est impaire pour décaler ou non le premier hexagone
            coo_centre_x = int(inf_gauche[0] + longueur * 2.5)
        else:
            coo_centre_x = int(inf_gauche[0] + longueur)
        # boucle des colonnes, qui appelle la fonction 'hexagone' pour les tracés
        for x in range(coo_centre_x, sup_droit[0] - longueur, xstep):
            hexagone((x, y, 0), longueur, col, centre, rayon)
        ligne += 1

    # sauvegarde l'image
    turtle.getcanvas().postscript(file = "pavage.eps")
    # attend une action de l'utilisateur avant de quitter
    turtle.done()


def get_parametres():
    """
    Fonction appelée pour obtenir les paramètres de dessin auprès de l'utilisateur
    :return: tuple contenant tous les informations nécessaires au dessin
    """
    coin_inf = int(input("Coin inférieur gauche :"))
    coin_sup = int(input("Coin supérieur droit :"))
    l_arrete = int(input("Longueur d'une arrête :"))
    coul1 = input("Couleur 1 :")
    coul2 = input("Couleur 2 :")
    coul3 = input("Couleur 3 :")
    x_cercle = int(input("Abscisse du centre du cercle :"))
    y_cercle = int(input("Ordonnée du centre du cercle :"))
    z_cercle = int(input("Hauteur du centre du cercle :"))
    r_cercle = int(input("Rayon du cercle :"))
    return ((coin_inf, coin_inf), (coin_sup, coin_sup), l_arrete, (coul1, coul2, coul3), (x_cercle, y_cercle, z_cercle),
            r_cercle)


"""
Programme principal
appelle la fonction get_parametres pour récupérer toutes les informations puis dessine le pavage
"""
parametres = get_parametres()
pavage(parametres[0], parametres[1], parametres[2], parametres[3], parametres[4], parametres[5])
