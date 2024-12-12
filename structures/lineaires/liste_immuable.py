from typing import Callable, Iterator

# Le vide est modélisé par un tuple vide.
type vide = tuple[()]

# La liste vide est... vide.
LISTE_VIDE: vide = ()

# Une liste est :
#       - soit vide, 
#       - soit un tuple contenant une tete (int), et la queue (qui est une liste)

type liste = vide | tuple[int, liste]


# La définition de cette structure fait appel à sa propre définition.
# C'est une structure récursive.


def exemple() -> liste:
    """
    Retourne un exemple de liste chaînée.
    Cette liste a pour tête 2, et pour queue la liste (3, (4,()))
    >>> exemple()
    (2, (3, (4, ())))
    """
    return (2, (3, (4, ())))


def exemple2() -> liste:
    """
    Retourne un autre exemple de liste chaînée.
    Cette liste a pour tête 2343, et pour queue la liste (98764, (9898598,()))

    >>> exemple2()
    (2343, (98764, (9898598, ())))
    """
    return (2343, (98764, (9898598,())))


#?#####################################
#! LES FONCTIONS D'ACCES ET DE CREATION
#*#####################################


def tete(lst: liste) -> int:
    """
    Renvoie la tête de la liste (le premier élément).

    Précondition :
    - La liste ne doit pas être vide

    >>> tete(exemple())
    2
    >>> tete(LISTE_VIDE)
    Traceback (most recent call last):
    AssertionError: Liste vide
    """
    assert len(lst) == 2, "Liste vide"
    return lst[0]


def queue(lst: liste) -> liste:
    """
    Renvoie la queue de la liste.

    Précondition :
    - La liste ne doit pas être vide

    >>> queue(exemple())
    (3, (4, ()))
    >>> queue(LISTE_VIDE)
    Traceback (most recent call last):
    AssertionError: Liste vide
    """
    assert len(lst) == 2, "Liste vide"
    return lst[1]




def creer(t: int, q: liste) -> liste:
    """
    Crée une liste à partir d'une tête et d'une queue.

    >>> creer(2, creer(3, creer(4, LISTE_VIDE)))
    (2, (3, (4, ())))
    """
    return (t, q)


def est_vide(lst: liste) -> bool:
    """
    Vérifie si une liste est vide.

    >>> est_vide(LISTE_VIDE)
    True
    >>> est_vide(exemple())
    False
    """
    return lst == LISTE_VIDE


#?#########################
#! LES FONCTIONS EN LECTURE
#*#########################


def taille(lst: liste) -> int:
    """
    Calcule la taille de la liste.

    >>> taille(exemple())
    3
    >>> taille(LISTE_VIDE)
    0
    """
    if est_vide(lst):
        return 0
    else:
        return 1 + taille(queue(lst))


def somme(lst: liste) -> int:
    """
    Calcule la somme des éléments d'une liste d'entiers.
    Si la liste est vide, renvoie 0.

    >>> somme(exemple())
    9
    >>> somme(LISTE_VIDE)
    0
    """
    if est_vide(lst):
        return 0
    return tete(lst) + somme(queue(lst))


def minimum(lst: liste) -> int:
    """
    Renvoie le minimum des éléments de la liste chaînée.
    On lève une erreur si la liste est vide.

    Précondition :
    - La liste ne doit pas être vide

    >>> minimum(exemple())
    2
    >>> minimum(LISTE_VIDE)
    Traceback (most recent call last):
    AssertionError: La liste est vide
    """
    assert not est_vide(lst), "La liste est vide"  
    
    if est_vide(queue(lst)):
        return tete(lst)
    
    
    else:
        min_queue = minimum(queue(lst))
        return min(tete(lst), min_queue)


def dernier_element(lst: liste) -> int:
    """
    Renvoie le dernier élément d'une liste chaînée.
    On lève une erreur si la liste est vide.

    Précondition :
    - La liste ne doit pas être vide

    >>> L = exemple()
    >>> dernier_element(L)
    4
    >>> dernier_element(LISTE_VIDE)
    Traceback (most recent call last):
    AssertionError: La liste vide n'a pas de dernier élément
    """
    assert not est_vide(lst), "La liste vide n'a pas de dernier élément"  

    
    if est_vide(queue(lst)):
        return tete(lst)
    
    
    return dernier_element(queue(lst))

def avant_dernier_element(lst: liste) -> int:
    """
    Renvoie l'avant-dernier élément d'une liste chaînée.
    On lève une erreur si la liste contient moins de deux éléments.

    Préconditions :
    - La liste doit contenir au moins deux éléments

    >>> L = exemple()
    >>> avant_dernier_element(L)
    3
    >>> avant_dernier_element(creer(2, LISTE_VIDE))
    Traceback (most recent call last):
    AssertionError: La liste n'a pas au moins deux éléments
    >>> avant_dernier_element(LISTE_VIDE)
    Traceback (most recent call last):
    AssertionError: La liste n'a pas au moins deux éléments
    """
    
    assert not est_vide(lst) and not est_vide(queue(lst)), "La liste n'a pas au moins deux éléments"

    
    if est_vide(queue(queue(lst))):
        return tete(lst)

    return avant_dernier_element(queue(lst))

def compte(e: int, lst: liste) -> int:
    """
    Compte le nombre d'occurrences de l'élément e dans la liste chaînée.

    Arguments :
    - e : l'élément à rechercher
    - lst : la liste dans laquelle compter les occurrences

    Renvoie :
    - Un entier représentant le nombre d'occurrences de e dans lst

    >>> compte(3, exemple())
    1
    >>> compte(5, exemple())
    0
    """
    
    if est_vide(lst):
        return 0
    
    
    return (1 if tete(lst) == e else 0) + compte(e, queue(lst))


def contient(e: int, lst: liste) -> bool:
    """
    Vérifie si l'élément e est contenu dans la liste chaînée.

    Arguments :
    - e : l'élément à rechercher
    - lst : la liste dans laquelle chercher l'élément

    Renvoie :
    - True si e est présent dans lst, sinon False

    >>> contient(3, exemple())
    True
    >>> contient(55, exemple())
    False
    """
    
    if est_vide(lst):
        return False
    
    
    return tete(lst) == e or contient(e, queue(lst))


def get_n(n: int, lst: liste) -> int:
    """
    Renvoie l'élément d'indice n dans une liste chaînée (commence à 0).

    Préconditions :
    - n >= 0
    - La liste ne doit pas être vide
    - n doit être inférieur à la taille de la liste

    Arguments :
    - n : l'indice de l'élément à obtenir
    - lst : la liste chaînée dans laquelle chercher l'élément

    Renvoie :
    - L'élément situé à l'indice n de la liste

    >>> L = exemple()
    >>> get_n(0, L)
    2
    >>> get_n(1, L)
    3
    >>> get_n(2, L)
    4
    >>> get_n(3, L)
    Traceback (most recent call last):
    AssertionError: Index hors limite
    """
   
    assert n >= 0, "L'indice doit être positif"
    assert not est_vide(lst), "La liste ne doit pas être vide"
    
    
    if n == 0:
        return tete(lst)
    
    
    assert not est_vide(queue(lst)), "Index hors limite"
    return get_n(n - 1, queue(lst))


def to_str(lst: liste) -> str:
    """
    Retourne une chaîne de caractères représentant la liste chaînée.

    La chaîne de caractères se termine par '_|_' pour indiquer la fin de la liste.

    Arguments :
    - lst : la liste chaînée à représenter sous forme de chaîne de caractères

    Renvoie :
    - Une chaîne de caractères représentant la liste

    >>> to_str(exemple())
    '2 -> 3 -> 4 -> _|_'
    >>> to_str(())
    '_|_'
    """
    
    if est_vide(lst):
        return "_|_"
    
    return f"{tete(lst)} -> {to_str(queue(lst))}"


def egal(l1: liste, l2: liste) -> bool:
    """
    Vérifie si deux listes chaînées sont égales, c'est-à-dire si elles contiennent
    les mêmes éléments dans le même ordre.

    Arguments :
    - l1 : première liste chaînée
    - l2 : deuxième liste chaînée

    Renvoie :
    - True si les deux listes sont égales, sinon False

    >>> L1 = exemple()
    >>> L2 = exemple()
    >>> egal(L1, L2)
    True
    >>> L3 = creer(5, L2)
    >>> egal(L1, L3)
    False
    """
    
    if est_vide(l1) and est_vide(l2):
        return True
    
    
    if est_vide(l1) or est_vide(l2):
        return False
    
    
    return tete(l1) == tete(l2) and egal(queue(l1), queue(l2))


#?########################################
#! LES FONCTIONS DE CREATION NON TRIVIALES
#*########################################

def clone(lst: liste) -> liste:
    """
    Renvoie une copie de la liste.

    >>> clone(exemple())
    (2, (3, (4, ())))
    >>> clone(LISTE_VIDE)
    ()
    """
    if est_vide(lst):
        return LISTE_VIDE
    else:
        return creer(tete(lst), clone(queue(lst)))


def supprimer_tete(lst: liste) -> liste:
    """
    Retourne une nouvelle liste sans la tête.

    >>> L1 = exemple()
    >>> L2 = supprimer_tete(L1)
    >>> to_str(L2)
    '3 -> 4 -> _|_'
    """
    assert not est_vide(lst), "La liste est vide"
    return queue(lst)


def ajouter_fin(e: int, lst: liste) -> liste:
    """
    Renvoie une nouvelle liste avec l'élément e ajouté à la fin.

    >>> L1 = exemple()
    >>> L2 = ajouter_fin(5, L1)
    >>> to_str(L2)
    '2 -> 3 -> 4 -> 5 -> _|_'
    """
    if est_vide(lst):
        return creer(e, LISTE_VIDE)
    else:
        return creer(tete(lst), ajouter_fin(e, queue(lst)))


def concat(l1: liste, l2: liste) -> liste:
    """
    Retourne la concaténation de l1 et l2.

    >>> L1 = exemple()
    >>> L2 = exemple2()
    >>> to_str(concat(L1, L2))
    '2 -> 3 -> 4 -> 2343 -> 98764 -> 9898598 -> _|_'
    """
    if est_vide(l1):
        return l2
    else:
        return creer(tete(l1), concat(queue(l1), l2))


def inverser(lst: liste) -> liste:
    """
    Inverse les éléments d'une liste.

    >>> to_str(inverser(exemple()))
    '4 -> 3 -> 2 -> _|_'
    """
    def inverser_recursive(lst: liste, acc: liste) -> liste:
        if est_vide(lst):
            return acc
        else:
            return inverser_recursive(queue(lst), creer(tete(lst), acc))
    
    return inverser_recursive(lst, LISTE_VIDE)


def supprimer_n(n: int, lst: liste) -> liste:
    """
    Supprime l'élément à l'indice n de la liste.

    >>> supprimer_n(1, exemple())
    (2, (4, ()))
    """
    assert n >= 0, "L'indice doit être positif"
    assert not est_vide(lst), "La liste est vide"
    if n == 0:
        return queue(lst)
    else:
        return creer(tete(lst), supprimer_n(n - 1, queue(lst)))


def supprimer(e: int, lst: liste) -> liste:
    """
    Supprime la première occurrence de l'élément e dans la liste.

    >>> supprimer(3, exemple())
    (2, (4, ()))
    >>> supprimer(2, exemple())
    (3, (4, ()))
    """
    if est_vide(lst):
        return LISTE_VIDE
    elif tete(lst) == e:
        return queue(lst)
    else:
        return creer(tete(lst), supprimer(e, queue(lst)))




#?#########
#! PROBLEME
#*#########
def trier(lst: liste) -> liste:
    """
    Trie une liste chaînée dans l'ordre croissant.

    >>> to_str(trier(exemple()))
    '2 -> 3 -> 4 -> _|_'
    >>> to_str(trier(exemple2()))
    '2343 -> 98764 -> 9898598 -> _|_'
    """
    
    if est_vide(lst) or est_vide(queue(lst)):
        return lst
    
    
    min_val = minimum(lst)
    lst_sans_min = supprimer(min_val, lst)
    
    
    return creer(min_val, trier(lst_sans_min))


def fusionner(l1: liste, l2: liste) -> liste:
    """
    Fusionne deux listes triées en une seule liste triée.

    >>> L1 = trier(exemple2())
    >>> L2 = trier(exemple())
    >>> to_str(fusionner(L1, L2))
    '2 -> 3 -> 4 -> 2343 -> 98764 -> 9898598 -> _|_'
    """
    if est_vide(l1):
        return l2
    elif est_vide(l2):
        return l1
    elif tete(l1) < tete(l2):
        return creer(tete(l1), fusionner(queue(l1), l2))
    else:
        return creer(tete(l2), fusionner(l1, queue(l2)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
