from qst_001 import pp_list


while True:
    nom_produit = input("Donner le nom de votre produit : ")
    if nom_produit=='0':
        break
    prix_produit=input('Donner le prix de votre produit:')

    prix_produit=int(prix_produit)

    pp_list.append((nom_produit, prix_produit))
    print(pp_list)



    