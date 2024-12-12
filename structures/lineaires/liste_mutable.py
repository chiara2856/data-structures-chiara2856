#Sous environnement python 13
from typing import Iterator

class Maillon:
    """
    Un Maillon porte une donnée data
    TOUT Maillon porte une référence next vers son Maillon suivant.
    """
    def __init__(self, data: int, next: 'Maillon'):
        self.data = data
        self.next = next



class Liste(Maillon): # Une liste est un maillon, son propre maillon sentinelle

    def __init__(self):
        super().__init__(0, self) # Une liste vide est un Maillon qui pointe sur lui-même.
        # Ici, self sera toujours le maillon sentinelle.
        self.__taille: int = 0


    def __len__(self) -> int:
        """
        Renvoie la longueur de la chaine démarrant par le Maillon.
        grâce au dunder, on peut maintenant appeler la fonction len.
        >>> lst = Liste()
        >>> lst.ajouter_tete(1)
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(3)
        >>> len(lst)
        3
        """
        return self.__taille

    def est_vide(self) -> bool:
        """Une liste est vide si elle est de taille 0"""
        return self.__taille == 0


    def __str__(self) -> str:
        """
        Convertit la liste en str. Grâce au dunder on peut maintenant utiliser les fonctions str()
        et toutes celles qui s'en servent (comme print).
        
        >>> lst = Liste()
        >>> lst.ajouter_tete(1)
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(3)
        >>> str(lst)
        '3 -> 2 -> 1 -> _|_'
        """
        result = []
        current = self.next  # On commence après le maillon sentinelle
        while current is not self:  # On s'arrête quand on atteint la sentinelle
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> _|_"

    

    def ajouter_tete(self, e: int):
        """il faut ajouter un maillon entre la sentinelle et son maillon suivant.
        """
        m = Maillon(e, self.next)
        self.next = m
        self.__taille +=1


    def _dernier(self) -> Maillon:
        """
        Renvoie le dernier Maillon, la liste elle-même si elle est vide.
        
        >>> lst = Liste()
        >>> lst.ajouter_tete(1)
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(3)
        >>> lst._dernier().data
        1
        >>> lst = Liste()
        >>> lst._dernier() is lst  # Liste vide doit retourner la sentinelle
        True
        """
        if self.est_vide():
            return self  # Renvoie la sentinelle si la liste est vide
        current = self.next
        while current.next is not self:  # Parcours jusqu'à atteindre la sentinelle
            current = current.next
        return current


    def ajouter_fin(self, e: int):
        """Ajoute un élément en dernière position.
        #! réutilisez la fonction _dernier
            
        >>> lst = Liste()
        >>> lst.ajouter_fin(4)
        >>> lst.ajouter_tete(3)
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(1)
        >>> print(lst)
        1 -> 2 -> 3 -> 4 -> _|_
        >>> len(lst)
        4
        >>> lst._dernier().data
        4
        >>> lst.ajouter_fin(5)
        >>> print(lst)
        1 -> 2 -> 3 -> 4 -> 5 -> _|_
        """
        dernier_maillon = self._dernier()
        nouveau_maillon = Maillon(e, self)  # Crée un maillon avec `self` comme `next`
        dernier_maillon.next = nouveau_maillon
        self.__taille += 1


    def clone(self) -> 'Liste':
        """
        Renvoie une copie de la liste (pas d'utilisation de deepcopy, on crée une nouvelle liste).
        
        >>> lst = Liste()
        >>> lst.ajouter_tete(1)
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(3)
        >>> clone_lst = lst.clone()
        >>> print(clone_lst)
        3 -> 2 -> 1 -> _|_
        >>> len(clone_lst)
        3
        >>> clone_lst.ajouter_tete(4)
        >>> print(lst)
        3 -> 2 -> 1 -> _|_
        >>> print(clone_lst)
        4 -> 3 -> 2 -> 1 -> _|_
        """
        clone_lst = Liste()  # Crée une nouvelle liste
        current = self.next  # Commence à partir du premier maillon
        while current is not self:  # Continue jusqu'à la sentinelle
            clone_lst.ajouter_fin(current.data)  # Ajoute à la fin de la nouvelle liste
            current = current.next
        return clone_lst

    def __add__(self, l2: 'Liste') -> 'Liste':
        """Renvoie la concaténation de self et de l2.
        
        >>> lst1 = Liste()
        >>> lst1.ajouter_tete(1)
        >>> lst1.ajouter_tete(2)
        >>> lst1.ajouter_tete(3)
        >>> lst2 = Liste()
        >>> lst2.ajouter_tete(4)
        >>> lst2.ajouter_tete(5)
        >>> lst2.ajouter_tete(6)
        >>> lst3 = lst1 + lst2
        >>> print(lst3)
        3 -> 2 -> 1 -> 6 -> 5 -> 4 -> _|_
        >>> len(lst3)
        6
        """
        result = self.clone()  # Clone de la première liste
        current = l2.next  # Commence à partir de la première élément de l2
        while current is not l2:  # Continue jusqu'à la sentinelle
            result.ajouter_fin(current.data)  # Ajoute chaque élément à la fin de la liste résultat
            current = current.next
        return result

    def extend(self, l2: 'Liste'):
        """Rajoute à self les maillons de l2.
        
        >>> lst = Liste()
        >>> lst.ajouter_tete(3)
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(1)
        >>> lst2 = Liste()
        >>> lst2.ajouter_tete(6)
        >>> lst2.ajouter_tete(5)
        >>> lst2.ajouter_tete(4)
        >>> lst.extend(lst2)
        >>> print(lst)
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> _|_
        """
        current = l2.next  # Commence à partir du premier maillon de l2
        while current is not l2:  # Continue jusqu'à la sentinelle
            self.ajouter_fin(current.data)  # Ajoute chaque élément à la fin de la liste actuelle
            current = current.next

    def __get_n(self, n: int) -> Maillon:
        """
        Renvoie le maillon d'indice n.
        Raise une IndexError si n n'est pas dans les indices valides.
        
        >>> lst = Liste()
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(3)
        >>> lst.ajouter_tete(89)
        >>> lst._Liste__get_n(0).data
        89
        >>> lst._Liste__get_n(1).data
        3
        >>> lst._Liste__get_n(2).data
        2
        >>> lst._Liste__get_n(3).data
        Traceback (most recent call last):
        IndexError
        >>> lst._Liste__get_n(-1).data
        Traceback (most recent call last):
        IndexError
        """
        if n < 0 or n >= self.__taille:
            raise IndexError
        current = self.next  # Commence à partir du premier maillon
        for _ in range(n):  # Parcours jusqu'à l'indice n
            current = current.next
        return current

    def __getitem__(self, n: int) -> int:
        """
        Renvoie l'élément d'indice n de la liste.
        Grâce à la syntaxe en dunder, on peut maintenant utiliser la syntaxe entre crochets.
        Le chaînon lui-même est à 0.
        
        >>> lst = Liste()
        >>> lst.ajouter_tete(2)
        >>> lst.ajouter_tete(3)
        >>> lst.ajouter_tete(89)
        >>> lst.__getitem__(0)
        89
        >>> lst[0]
        89
        >>> lst[1]
        3
        >>> lst[2]
        2
        >>> lst[3]
        Traceback (most recent call last):
        IndexError
        >>> lst[-1]
        Traceback (most recent call last):
        IndexError
        """
        return self.__get_n(n).data 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
