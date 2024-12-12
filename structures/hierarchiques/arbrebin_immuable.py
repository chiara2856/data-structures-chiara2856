
# On modélise le vide par un tuple vide. Donc le type vide est le type du tuple vide.
type vide = tuple[()]
# Un arbre est vide ou c'est un tuple constitué d'une clé et de 2 arbres, le sag et le sad.
type arbrebin[T] = vide|tuple[T, arbrebin[T], arbrebin[T]] 

ARBRE_VIDE = ()

def cle[T](a: arbrebin[T]) -> T:
    assert len(a)==3, "L'arbre est vide"
    return a[0]
        
def sag[T](a: arbrebin[T]) -> arbrebin[T]:
    assert len(a)==3, "L'arbre est vide"
    return a[1]

def sad[T](a: arbrebin[T]) -> arbrebin[T]:
    assert len(a)==3, "L'arbre est vide"
    return a[2]

def creer[T](e: T, gauche: arbrebin[T], droite: arbrebin[T]) -> arbrebin[T]:
    return (e, gauche, droite)

def creer_feuille[T](e: T) -> arbrebin[T]:
    return (e, ARBRE_VIDE, ARBRE_VIDE)

def est_vide[T](a: arbrebin[T]) -> bool:
    return len(a) == 0

def hauteur[T] (a:arbrebin[T]) -> arbrebin[T] :
    if est_vide(a):
        return 0
    else:
        return 1+max(hauteur(sag(a)), hauteur (sad(a)))
    
def taille [T](a:arbrebin[T]) -> arbrebin [T]:
    if est_vide(a):
        return 0
    else:
        return 1+ taille(sag(a))+taille(sad(a))

def somme [T] (a: arbrebin [T]) -> arbrebin[T]:
    if est_vide(a):
        return 0
    return cle(a)+somme(sag(a))+somme(sad(a))

def to_str(a:arbrebin) -> arbrebin :
    if est_vide(a):
        return 0

def maximum(a:arbrebin) -> arbrebin :
    assert not est_vide(a)," L'arbre est vide" 
    if est_vide(sad(a),sag(a)):
        return cle(a)
    if est_vide(sag(a)):
        return maximum (sag(a), cle(a))
    if est_vide(sad(a)):
        return maximum (sad(a), cle(a))

def minimum(a:arbrebin) -> arbrebin :
    assert not est_vide(a),"L'arbre est vide"
    if est_vide(sad(a), sag(a)):
        return cle(a)
    if est_vide(sag(a)):
        return minimum (sag(a), cle(a))
    if est_vide(sag(a)):
        return minimum (sad(a),cle (a))
    
def sont_egaux(a1:arbrebin, a2: arbrebin) -> bool:
    if est_vide(a1)and est_vide(a2):
        return True
    if est_vide(a1)or est_vide(a2):
        return False 
    else:
        return (cle(a1)==cle(a2)and sont_egaux(sag(a1)),(sag(a2)) and sont_egaux(sad(a1),sad(a2)))


#! A partir de maintenant, nous n'utiliserons plus les tuples.

def exemple() -> arbrebin[int]:
    a = creer(11, creer_feuille(9), ARBRE_VIDE)
    b = creer(18, creer_feuille(15), creer_feuille(19))
    f = creer(14, a, b)
    g = creer_feuille(25)
    h = creer_feuille(12)
    i = creer(28, g, h)
    return creer(21, f, i)


if __name__ == "__main__":

    import doctest
    from . import dessin

    print(f"Début des tests pour {__file__}")
    res = doctest.testmod()
    print(f"Fin des tests pour {__file__}")

    dessin.show(exemple())