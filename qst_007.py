from qst_006 import tuple_of_pps

def min_max_price(tup):
    min_price =tuple_of_pps[len(tup)-2]
    max_price = tuple_of_pps[-1]
    return min_price, max_price
def afficher_min_max_price():
    min_price, max_price = min_max_price(tuple_of_pps)
    print(f"Produit avec le plus cher: {max_price}")
    print(f"Produit avec le plus cher de ceux qui reste : {min_price}")