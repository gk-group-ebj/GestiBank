# Classe Client, heritage de la classe mère User

from user import User
from connection import connect, cnx


class Client(User):

    def __init__(self, id, surname, name, address, email, password, b_account_num=None,
                 children_nb=None, marital_status=None, phone=None, user_type=None):
        User.__init__(self, id, surname, name, address, email, password, phone=None, user_type=None)
        self.b_account_num = b_account_num
        self.children_nb = children_nb
        self.phone = phone
        self.user_type = user_type
        self.marital_status = marital_status

    # Méthode affichage attributs de l'objet de type client
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.id, self.surname, self.name,
                                                                 self.address, self.email, self.password,
                                                                   self.b_account_num, self.children_nb,
                                                                   self.marital_status, self.phone, self.user_type)

     # Méthode retourne les valeurs des attributs utiles pour la BD de l'objet de type client
    def get_utile_attr(self):
        return self.id, self.surname, self.name, self.address, self.email, self.password, self.b_account_num,
                self.children_nb, self.marital_status, self.phone, self.user_type
    #

    # Méthode mise à jour des informations Client
    def update_client_profile(self):
        User.update_user_profile(self)
        input_children_nb = input("Entrez le nombre d'enfants à charge \n: ")
        self.children_nb = input_children_nb
        input_marital_status = input("Entrez votre situation familiale \n: ")
        self.marital_status = input_marital_status

    # Méthode de sauvegarde des infos mises à jour dans la BDD table clients
    def save_update_client_profile(self, data):

        self.data = data
        connect()

        insert_stmt = (
            "INSERT INTO client(id, surname, name, address, email, password, b_account_num, children_nb, marital_status, phone, user_type)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )


        """= [
            (1, 'az', 'z', 're', 't'),
            (2, 'p', 'p', 'p', "p")
        ]"""

        cursor = cnx.cursor()
        cursor.executemany(insert_stmt, data)
        cnx.close()



    # Méthode demande de transfert bancaire
    def bank_transfer(self):
        pass

    # Méthode demande de chéquier
    def request_cheque_book(self):
        pass

    # Méthode demande de création de nouveau compte bancaire
    def new_bank_account(self):
        pass

    # Méthode demande de consultation du relevé de compte sur 30 jours
    def view_bank_statement(self, b_account_num):
        self.b_account_num = b_account_num


if __name__ == "__main__":
   """ c1 = Client(1, "aa", "bb", "mars", "c", "d")
    print(c1)
    c1.update_client_profile()
    print(c1)"""




a = input("entrez id : ")
b = input("entrez nom : ")
c = input("entrez prénom : ")
d = input("entrez adresse : ")
e = input("entrez email : ")
f = input("entrez mot de passe : ")
g = input("entrez n° compte : ")
h = input("entrez nombre d'enfants : ")
i = input("entrez statut marital : ")
j = input("entrez tel : ")
k = input("entrez type d'utilisateur : ")


c1 = Client(a, b, c, d, e, f, g, h, i, j, k)

lst = []



data = c1.get_utile_attr()

dat = [data]
print(dat)

c1.save_update_client_profile(dat)