#### Imports et définition des variables globales
import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode = 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        l = [[int(i) for i in line.split(';')] for line in lines]
    return l

def get_list_k(data, k):
     if k < 0 or k >= len(data):
        raise IndexError("Indice hors limite".format(len(data)-1))
     l = data[k]
     return l

def get_first(l):
    if len(l) == 0:
        return None
    else:
        return l[0]

def get_last(l):
    if len(l) == 0:
        return None
    else:
        return l[-1]

def get_max(l):
    if len(l) == 0:
        return None
    else:
        return max(l)

def get_min(l):
    if len(l) == 0:
        return None
    else:
        return min(l)

def get_sum(l):
    if len(l) == 0:
        return None
    else:
        return sum(l)


#### Fonction principale


def main():
    pass
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))
    try:
        data = read_data(FILENAME)
        print("Données qui seront lues depuis le fichier :", data)

        if data:
            print("Liste à l'indice 0:", get_list_k(data, 0))
            print("Premier élément de la première liste :", get_first(data[0]))
            print("Dernier élément de la première liste :", get_last(data[0]))
            print("Maximum de la première liste :", get_max(data[0]))
            print("Minimum de la première liste :", get_min(data[0]))
            print("Somme :", get_sum(data[0]))
        else:
            print("Le fichier est vide")

    except FileNotFoundError:
        print(f"Erreur : le fichier '{FILENAME}' n'a pas été trouvé.")
    except IndexError as e:
        print(e)




if __name__ == "__main__":
    main()
