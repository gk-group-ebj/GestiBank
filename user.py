

class User:

    def __init__(self, mail, password):
        self.password = password
        self.mail = mail


    def login(self, mail, password):

        if(self.mail is temp_mail and self.password is temp_password):
            print("Success")
        else:
            print("Utilisateur non identifié")


u1 = User("test@test.com", "test")
temp_mail = input("Veuillez entrer votre mail : ")
temp_password = input("Veuillez entrer votre mot de passe : ")
u1.login("test@test.com", "test")