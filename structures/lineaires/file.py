from . import pile

type file[T] = tuple[pile.pile[T], pile.pile[T]]


def creer[T]() -> file[T]:
    """
    Crée une nouvelle file vide.

    >>> f: file[int] = creer()
    >>> len(f[0]) == 0 and len(f[1]) == 0
    True
    """
    return (pile.creer(), pile.creer())


def enfiler[T](f: file[T], e: T):
    """
    Ajoute un élément à la file.

    >>> f: file[int] = creer()
    >>> enfiler(f, 1)
    >>> enfiler(f, 2)
    >>> f[0]
    [1, 2]
    """
    pile.empiler(f[0], e)


def defiler[T](f: file[T]) -> T:
    """
    Retire et renvoie l'élément au début de la file.
    Soulève une assertion si la file est vide.

    >>> f: file[int] = creer()
    >>> enfiler(f, 1)
    >>> enfiler(f, 2)
    >>> defiler(f)
    1
    >>> defiler(f)
    2
    >>> defiler(f)
    Traceback (most recent call last):
    AssertionError: La file est vide
    """
    if pile.est_vide(f[1]):
        while not pile.est_vide(f[0]):
            pile.empiler(f[1], pile.depiler(f[0]))

    assert not pile.est_vide(f[1]), "La file est vide"
    return pile.depiler(f[1])


def est_vide[T](f: file[T]) -> bool:
    """
    Vérifie si la file est vide.

    >>> f: file[int] = creer()
    >>> est_vide(f)
    True
    >>> enfiler(f, 1)
    >>> est_vide(f)
    False
    """
    return len(f[0]) + len(f[1]) == 0

if __name__ == "__main__":
    import doctest
    print(f"Début des tests de {__file__}")
    doctest.testmod()
    print("Fin des tests")
