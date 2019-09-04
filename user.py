class User:

    def __init__(self, id, name, surname, address, email, password, phone=None, user_type=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email
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
                if input_email is self.email and input_password is self.password:
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
    def update_profile(self):

        ask_password = input("Voulez-vous modifier votre mot de passe ? \n\noui ou non: ")
        if ask_password == "oui":
            new_password = input("Renseigneze \n\nnouveau mot de passe: ")
            self.password = new_password
        else:
            pass

        ask_email = input("Voulez-vous modifier votre email ? \n\noui ou non: ")
        if ask_email == "oui":
            new_email = input("Renseignez \n\nnouvel email: ")
            self.email = new_email
        else:
            pass

        ask_phone = input("Voulez-vous modifier votre numéro de téléphone ? \n\noui ou non: ")
        if ask_phone == "oui":
            new_phone = input("Renseignez \n\nnouveau numéro: ")
            self.phone = new_phone
        else:
            pass

        ask_address = input("Voulez-vous modifier votre adresse ? \n\noui ou non: ")
        if ask_address == "oui":
            new_address = input("Renseignez \n\nnouvelle adresse: ")
            self.address = new_address
        else:
            pass

        print("Vos données ont été mises à jour")




# Partie test

#u1 = User(5, "John", "Smith", "la matrice","a","b")

#u1.login()
#u1.update_profile()
#print("new mdp : "+u1.password+"\nnew email : "+u1.email+"\nnouveau numéro :"+u1.phone+"\nnew adresse :"+u1.address)
