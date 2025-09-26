from qst_001 import pp_list

def chercher_produit(nom_produit):
    for produit, prix in pp_list:
        if produit.lower() == nom_produit.lower():
            return prix
    return None 

def afficher_prix_produit(nom_produit):
    prix = chercher_produit(nom_produit)
    if prix is not None:
        print(f"Le prix de '{nom_produit}' est de {prix} DH.")
    else:
        print(f"Produit '{nom_produit}' non trouve.")

produit=input("Entrez le nom du produit pour chercher son prix : ")
afficher_prix_produit(produit)