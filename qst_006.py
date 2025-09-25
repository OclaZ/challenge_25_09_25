from qst_005 import filtred_pp_list

def convertir_en_tuple():
    tuple_of_pp = tuple(filtred_pp_list)
    return tuple_of_pp

def afficher_tuple():
    print(convertir_en_tuple())\

tuple_of_pps = convertir_en_tuple()
