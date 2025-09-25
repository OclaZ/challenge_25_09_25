from variables import produits, prix

def zip_produits_prix(produits, prix):
    return list(zip(produits, prix))

pp_list = zip_produits_prix(produits, prix)

def afficher_pp_list():
    print(pp_list)

