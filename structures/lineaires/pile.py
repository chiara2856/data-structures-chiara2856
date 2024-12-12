type pile[T] = list[T]


def creer[T]() -> pile[T]:
    """
    Crée une nouvelle pile vide.

    >>> p: pile[int] = creer()
    >>> len(p) == 0
    True
    """
    return list[T]()



def empiler[T](p: pile[T], e: T):
    """
    Ajoute un élément au sommet de la pile.

    >>> p: pile[int] = creer()
    >>> empiler(p, 1)
    >>> empiler(p, 2)
    >>> p
    [1, 2]
    """
    p.append(e)


def depiler[T](p: pile[T]) -> T:
    """
    Retire et renvoie l'élément au sommet de la pile.
    Soulève une assertion si la pile est vide.

    >>> p: pile[int] = creer()
    >>> empiler(p, 1)
    >>> empiler(p, 2)
    >>> depiler(p)
    2
    >>> depiler(p)
    1
    >>> depiler(p)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    AssertionError: La pile est vide
    """
    assert len(p) != 0, "La pile est vide"
    return p.pop()


def est_vide[T](p: pile[T]) -> bool:
    """
    Vérifie si la pile est vide.

    >>> p: pile[int] = creer()
    >>> est_vide(p)
    True
    >>> empiler(p, 1)
    >>> est_vide(p)
    False
    """
    return len(p) == 0

def taille[T](p: pile[T]) -> int:
    """
    Renvoie la taille de la pile.

    >>> p: pile[int] = creer()
    >>> taille(p)
    0
    >>> empiler(p, 1)
    >>> empiler(p, 2)
    >>> taille(p)
    2
    """
    return len(p)


def taille_rec[T](p: pile[T]) -> int:
    """
    Renvoie la taille de la pile.

    >>> p: pile[int] = creer()
    >>> taille_rec(p)
    0
    >>> empiler(p, 1)
    >>> empiler(p, 2)
    >>> taille_rec(p)
    2
    """
    if est_vide(p):
        return 0
    tmp = depiler(p)
    res = 1 + taille_rec(p)
    empiler(p, tmp)
    return res

if __name__ == "__main__":
    import doctest
    print(f"Début des tests de {__file__}")
    doctest.testmod()
    print("Fin des tests")

