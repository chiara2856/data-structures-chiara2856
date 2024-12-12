#type: ignore
from . import arbrebin_immuable as ab

from graphviz import Digraph

def show(arbre: ab.arbrebin, viewer: bool = False):
    def ajoute(arbre: ab.arbrebin, graphe: Digraph):
        if arbre != ab.ARBRE_VIDE:
            node_id = str(id(arbre))
            value = str(ab.cle(arbre))  

            graphe.node(node_id, label=value) 

            # Ajouter les liens pour le sous-arbre gauche et droit
            for enfant, label in zip((ab.sag(arbre), ab.sad(arbre)), ("G", "D")):
                if enfant != ab.ARBRE_VIDE:
                    enfant_id = str(id(enfant))
                    graphe.edge(node_id, enfant_id, label=label)
                    ajoute(enfant, graphe)

    # Créer un graphe orienté
    graphe = Digraph(format='png')
    graphe.attr('node', shape='circle')

    # Ajouter les nœuds et les arêtes
    ajoute(arbre, graphe)

    # Afficher le graphe (par défaut, sauvegarde dans un fichier temporaire et affiche)
    if viewer:
        graphe.view(cleanup=True)
    else:
        graphe.render(cleanup=True)
