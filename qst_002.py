from qst_001 import pp_list

filtred_pp_list = list(filter(lambda p: p[1] >= 30, pp_list))
def afficher_filtered_pp_list():
    print(filtred_pp_list)