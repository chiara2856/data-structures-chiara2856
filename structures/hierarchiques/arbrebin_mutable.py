


"""def to_str(a:arbrebin) -> arbrebin :
    if est_vide(a):
        return
    
def maximum(a:arbrebin) -> arbrebin :
    if est_vide(a):
        raise ValueError 
    if est_vide(sad(a)):
        return cle(a)
    return maximum(sag(a))

def minimum(a:arbrebin) -> arbrebin :
    if est_vide(a):
        raise ValueError 
    if est_vide(sad(a)):
        return cle(a)
    return minimum(sag(a))

def sont_egaux(a1:arbrebin, a2: arbrebin) -> bool:
    if est_vide(a1)and est_vide(a2):
        return False
    if est_vide(a1)or est_vide(a2):
        return False 
    return (cle(a1)==cle(a2)and sont_egaux(sag(a1)),(sag(a2)) and sont_egaux(sad(a1),sad(a2)))

"""