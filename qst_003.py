from qst_001 import pp_list


def afficher_pp_list_fstr():
    for produit, prix in pp_list:
        print(f"{produit} coute: {prix} dh")

