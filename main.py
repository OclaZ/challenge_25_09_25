from qst_001 import afficher_pp_list
from qst_002 import afficher_filtered_pp_list
from qst_003 import afficher_pp_list_fstr
from qst_005 import afficher_min_max
from qst_006 import afficher_tuple
from qst_007 import afficher_min_max_price
from qst_008 import affixher_luxe




def main():
    print("Liste des produits et leurs prix :")
    afficher_pp_list()
    print("\n")
    
    print("liste des produits dont le prix est superieur ou egal a 30 :")
    afficher_filtered_pp_list()
    print("\n")

    print("chaine de de produit coute X dhs")
    afficher_pp_list_fstr()
    print("\n")


    print("Liste des produits triés par prix (du moins cher au plus cher) :")
    afficher_min_max() 
    print("\n")

    print("Liste des produits sous forme de tuples :")
    afficher_tuple()
    print("\n")

    print("Produit avec le prix minimum et maximum :")
    afficher_min_max_price()
    print("\n")

    print("Liste des produits de luxe (prix > 1000) :")
    affixher_luxe()
    print("\n")

    

if __name__ == "__main__":
    main()
