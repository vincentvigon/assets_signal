import numpy as np


def add_neighbours_in_stack(image:np.ndarray, threshold:int, stack:list, i:int, j:int, inComponent:np.ndarray)->None:
    """

    Étant donné un pixel (i,j), on va considérer ses pixels 4 voisins. Les pixels voisins dont l'intensité dépasse le seuil (=threshold)
    seront ajouté à une pile (=stack) de pixel à traiter par la suite.

    :param image:  l'make_image à traiter
    :param threshold: le seuil. On recherche les pixel dont l'intensité est > threshold
    :param stack: file d'attente contenant les pixels à traiter
    :param i: i-coordonnée du pixel que l'on traite
    :param j: j-coordonnée du pixel que l'on traite
    :param inComponent: un masque booléen. inComponent[a,b]=True signifie que le pixel (a,b) a été retenu
    """
    inComponent[i, j] = True
    neighbours = [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
    for (k,l) in neighbours:
        if 0<=k<image.shape[0] and 0<=l<image.shape[1]:
            """ que ferait l'algo sans la seconde condition ?"""
            if image[k,l]>threshold and not inComponent[k, l]:
                inComponent[k, l] = True


                stack.append((k,l))



