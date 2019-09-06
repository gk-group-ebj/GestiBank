from user import User
from connection import connect, cnx
import mysql.connector
from mysql.connector import Error

class Manager(User):
    def __init__(self, id, name, surname, address,
                 email, password, pro_id, date_beginning_contract,
                 date_end_contract, phone=None, user_type=None):
        User.__init__(self, id, name, surname, address,
                      email, password, phone=None, user_type=None)
        self.pro_id = id
        self.date_beginning_contract = beginning_contract
        self.date_end_contract = end_contract



    def account_creation():
        connect()


def login(self):
    count = 0

    connect()

    cursor = cnx.cursor()
    cursor.execute(select_email)

    #rows_email = cursor.fetchall()

    cursor.execute(select_password)

    # rows_password = cursor.fetchall()

    print(rows_email)
    print(rows_password)

    while True:
        print(rows)

        input_email = input("Entrez votre email \n: ")
        input_password = input("Entrez votre mot de passe \n: ")

        count += 1
        try_number = 3 - count

        if count == 3:
            # Identification refusée
            print("Vos identifiants sont incorrects. Contactez votre agence GestiBank")
            # exit
            break
        else:
            if input_email == self.email and input_password == self.password and input_global_name == self.global_name:
                # Identification réussie
                print("Identification réussie")
                break  # Il faudra faire une redirection avec le user_type
            else:
                # Erreur d'identification, Nouvelle tentative
                print(
                "Nom d'utilisateur, email ou mot de passe erronés \nNombre de tentatives restantes : " + str(try_number) + "\nIdentifiez vous")

    cnx.close()

if __name__ == "__main__":

    # TODO : Bien implémenter le code connexion dans les classes correspondantes.
    connect()

    input_email = input("Entrez votre email \n: ")
    input_password = input("Entrez votre mot de passe \n: ")
    try :
        select_email = ("SELECT id FROM manager WHERE password ='"+input_password+"' and email='"+input_email+"'")

        #select_password = "SELECT "+ input_password +" FROM manager"
        print(select_email)
        cursor = cnx.cursor()
        mail = cursor.execute(select_email)
        valeur = cursor.fetchone()
        print(valeur)
        if valeur != None:
            print("connection reussi")
        else:
            print("connection rate")
    except:
        print("connection ratett")

    cnx.close()
