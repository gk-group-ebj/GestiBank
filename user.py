class User:

    def __init__(self, id, name, surname, address, mail, password, phone=None, user_type=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.address = address
        self.mail = mail
        self.password = password

    # Méthode d'identification de l'utilisateur pour connexion et redirection
    def login(self):

        count = 0
        while True:

            input_mail = input("Entrez votre identifiant \n\nemail: ")
            input_password = input("Entrez votre mot de passe \n\nmdp: ")
            count += 1
            try_number = 3 - count

            if count == 3:
                # Identification refusée
                print("Vos identifiants sont incorrects. Contactez votre agence GestiBank")
                # exit
                break
            else:
                if input_mail is self.mail and input_password is self.password:
                    # Identification réussie
                    print("Identification réussie")
                    break  # Il faudra faire une redirection avec le user_type
                else:
                    # tell them it is wrong and have them retry, stay in loop
                    print(
                        "Email ou mot de passe erroné \nNombre de tentatives restantes : " + str(try_number) + "\nIdentifiez vous")

    # Méthode de déconnexion
    # Déconnexion par choix ou par timer
    def logout(self):

        print("Vous êtes déconnecté")

    # Méthode de mise à jour de profil utilisateur
    def update_profile(self, password, email, phone, address):

        ask_password = input("Voulez-vous modifier votre mot de passe ? \n\noui ou non: ")
        if ask_password is "oui":
            password = input("Renseigneze \n\nnouveau mot de passe: ")
        else:
            pass

        ask_mail = input("Voulez-vous modifier votre email ? \n\noui ou non: ")
        if ask_mail is "oui":
            mail = input("Renseignez \n\nnouvel email: ")
        else:
            pass

        ask_phone = input("Voulez-vous modifier votre numéro de téléphone ? \n\noui ou non: ")
        if ask_phone is "oui":
            phone = input("Renseignez \n\nnouveau numéro: ")
        else:
            pass

        ask_address = input("Voulez-vous modifier votre adresse ? \n\noui ou non: ")
        if ask_address is "oui":
            address = input("Renseignez \n\nnouvelle adress: ")
        else:
            pass

        print("Vos données ont été mises à jour")




# Partie test

# u1 = User(5, "John", "Smith", "la matrice","a","b")

# u1.login()
