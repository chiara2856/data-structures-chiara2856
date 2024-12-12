from random import randint
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

def est_feuille[T](a : arbrebin) -> bool:
    if est_vide (a):
        return False 
    return est_vide(sag(a)) and est_vide(sad(a))



### exos basique 
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
    else: 
        cle(a)+ to_str(sag(a))+ to_str(sad(a))


def maximum(a:arbrebin) -> arbrebin :
    assert not est_vide(a)," L'arbre est vide" 
    if est_vide(sad(a),sag(a)):
        return cle(a)
    if est_vide(sag(a)):
        return maximum (sag(a), cle(a))
    if est_vide(sad(a)):
        return maximum (sad(a), cle(a))
    else:
        return maximum( sad(a),sag(a))

def minimum(a:arbrebin) -> arbrebin :
    assert not est_vide(a),"L'arbre est vide"
    if est_vide(sad(a), sag(a)):
        return cle(a)
    if est_vide(sag(a)):
        return minimum (sag(a), cle(a))
    if est_vide(sad(a)):
        return minimum (sag(a),cle (a))
    else:
        return minimum( sad(a),sag(a))
    
def sont_egaux(a1:arbrebin, a2: arbrebin) -> bool:
    if est_vide(a1)and est_vide(a2):
        return True
    if est_vide(a1)or est_vide(a2):
        return False 
    else:
        return (cle(a1)==cle(a2)and sont_egaux(sag(a1)),(sag(a2)) and sont_egaux(sad(a1),sad(a2)))
    


### arbre equilibres 

def est_equilibres (a:arbrebin):
    if est_vide(a):
        return True 
    else:
        return hauteur(sag(a))-hauteur(sad(a))<=1 and est_equilibres(sad(a)) and est_equilibres(sag(a))
    


#### parcours 

def p1( a: arbrebin):
    if not est_vide(a):
        print(cle(a))
        p1(sag(a))
        p1(sad(a))


def p2( a: arbrebin):
    if not est_vide(a):
        p2(sag(a))
        print(cle(a))
        p2(sad(a))


def p3( a: arbrebin):
    if not est_vide(a):
        p3(sag(a))
        p3(sad(a))
        print(cle(a))




### arbre aleatoire 


def genre_alea(h: int) -> arbrebin[int]:
    if h==0:
        return ARBRE_VIDE
    else:
        return creer(randint[1,100], genre_alea(h-1),genre_alea(h-1))
    


from ..lineaires import file 
def bfs [T]( a: arbrebin[T]):
    if est_vide(a):
        return 0
    f= file.creer()
    file.enfiler(f,a)
    while not file.estvide(f):
        p=file.defiler(f)
        print(p)
        if not est_vide(sag(p)):
            file.emfiler(f,sag(p))
        if not est_vide(sag(p)):
            file.emfiler(f,sad(p))



#### est_abr
def est_abr(a:arbrebin) -> bool:
    if est_vide(a):
        return False
    elif est_feuille(a):
        return True 
    elif est_vide(sag(a)):
        return minimum(sad(a))> cle(a) and est_abr(sad(a))
    elif est_vide(sad(a)):
        return minimum(sag(a))> cle(a) and est_abr(sag(a))
    else:
        return maximum(sag(a))<cle(a)< minimum(sad(a)) and est_abr(sag(a)) and est_abr(sad(a))
    

def recherche_abr[T]( e: T, a : arbrebin [T])->bool:
    if est_vide(a):
        return False 
    elif est_feuille(a) ==e:
        return True 
    elif est_vide(sag(a)) and sad (a)==e :
        return True 
    elif est_vide(sad(a)) and sag (a)==e :
        return True 
    else: 
        return recherche_abr(e, sag(a)) and recherche_abr(e, sad((a)))
    
    
def inserer_abr[T](e:T, a: arbrebin [T]) -> arbrebin :
    if est_vide(a):
        return creer_feuille(e)
    if e<cle(a):
        return creer(cle(a), sag(a), inserer_abr(e,sad(a)))
    if e>cle(a):
        return creer(cle(a), sag(a), inserer_abr(e,sad(a)))
    else:
        return e== recherche_abr(e)

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