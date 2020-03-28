from math import pi, sin, cos, sqrt, acos, asin, atan2
import turtle


def pave(point1, point2, point3, point4, couleur):
    """
    peint un pavé ayant pour sommets les 4 points p1 à p4 dont les coordonnées dans le plan sont
    représentés sous forme de tuples(x, y)
    Entrées :
        p1 : point n°1
        p2 : point n°2
        p3 : point n°3
        p4 : point n°4
        couleur : couleur du pavé
    """
    turtle.goto(point1[0], point1[1])  # déplacer la tortue au point n°1
    turtle.down()  # commencer à dessiner
    turtle.color(couleur)  # changer la couleur de crayon
    turtle.beginfill()  # commencer à remplir
    turtle.goto(point2[0], point2[1])  # relier tous les points
    turtle.goto(point3[0], point3[1])
    turtle.goto(point4[0], point4[1])
    turtle.goto(point1[0], point1[1])
    turtle.end_fill()  # clôturer et remplir le pavé
    turtle.up()  # lever le crayon
import math


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

    x, y, z = point

    # dessin du pavé n°1
    p1 = (x, y, z)
    p2 = (x + cos(2 * pi / 3) * longueur, y + sin(pi / 3) * longueur, 0)
    p3 = (x + cos(pi / 3) * longueur, y + sin(pi / 3) * longueur, 0)
    p4 = (x + longueur, y, 0)
    pave(p1, p2, p3, p4, col)

    # dessin du pavé n°2
    p1 = (x, y, z)
    p2 = (x + longueur, y, 0)
    p3 = (x + cos(pi / 3) * longueur, y - sin(pi / 3) * longueur, 0)
    p4 =  (x + cos(2 * pi / 3) * longueur, y - sin(pi / 3) * longueur, 0)
    pave(p1, p2, p3, p4, col)
    pass  # TODO -- Créer une fonction qui dessine hexagone

    # dessin du pavé n°3
    p1 = (x, y, z)
    p2 = (x + longueur, y, 0)
    p3 = (x + cos(pi / 3) * longueur, y - sin(pi / 3) * longueur, 0)
    p4 = (x + cos(2 * pi / 3) * longueur, y - sin(pi / 3) * longueur, 0)
    pave(p1, p2, p3, p4, col)


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
def deformation(point, centre, rayon):
    pass  # TODO -- Calcule la déformation


def pavage(inf_gauche, sup_droit, longueur, col, rayon):
    pass  # TODO -- Dessine le pavage


pass  # TODO -- code principal

