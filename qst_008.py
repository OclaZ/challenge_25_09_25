

from variables import produits, prix
from qst_001 import pp_list

def ajouter_luxe(pp):
    produit, p = pp
    if p > 1000:
        return f"Produit coûte {p} DH (LUXE)"
    else:
        return f"Produit coûte {p} DH"

def map_luxe():
    add_luxe = list(map(ajouter_luxe, pp_list))
    return add_luxe

def affixher_luxe():
    print(map_luxe())

