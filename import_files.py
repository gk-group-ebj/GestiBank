from database_operation import *

def import_file(path):
    path = "C:/Users/kardaoui/Desktop/fichier d'entrée/clients.txt"
    lst = []
    with open(path, "r") as f:
        for l in f.readlines():
            mots = str.split(l, ", ")
            mots[-1] = mots[-1][:-1]
            tup=tuple(mots)
            lst.append(tup)

    return(lst)


if __name__ == "__main__":
    #path = "C:/Users/kardaoui/Desktop/fichier d'entrée/manager.txt"
    #data = import_file(path)
    #create_client_profile(data, "manager")
    path = "C:/Users/kardaoui/Desktop/fichier d'entrée/clients.txt"
    data = import_file(path)
    create_client_profile(data, "client")









