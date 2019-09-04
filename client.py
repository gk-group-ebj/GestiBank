# Classe Client, heritage de la classe mère User

from user import User


class Client(User):

    def __init__(self, id, surname, name, address, email, password, b_account_num=None,
                 children_nb=None, marital_status=None, phone=None, user_type=None):
        User.__init__(self, id, surname, name, address, email, password, phone=None, user_type=None)
        self.b_account_num = b_account_num
        self.children_nb = children_nb
        self.marital_status = marital_status

    # Méthode affichage attributs de l'objet de type client
    def __str__(self):
        return "id:{}, nom:{}, prénon:{}, nbe enfants:{}, statut marital:{}".format(self.id, self.surname, self.name,
                                                                                    self.children_nb,
                                                                                    self.marital_status)

    # Méthode mise à jour des informations Client
    def update_client_profile(self):
        input_children_nb = input("Entrez le nombre d'enfants à charge \n: ")
        self.children_nb = input_children_nb
        input_marital_status = input("Entrez votre situation familiale \n: ")
        self.marital_status = input_marital_status

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
    c1 = Client(1, "aa", "bb", "mars", "c", "d")
    print(c1)
    c1.update_client_profile()
    print(c1)