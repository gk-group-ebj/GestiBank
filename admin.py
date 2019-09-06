from mysql.connector import Error, connection
from user import User
from connection import connect, cnx
from database_operation import *
#from manager import Manager
from import_files import *


class Admin(User):
    def __init__(self, id, name, surname, address, email, password, phone,  pro_id, user_type):
        self.pro_id = pro_id

        User.__init__(self, id, name, surname, name+surname, address, email, password, phone=phone, user_type=user_type)

        # Méthode retourne les valeurs des attributs utiles pour la BD de l'objet de type admin
    def get_utile_attr_admin(self):
        return (self.surname, self.name, self.address, self.email, self.password, self.phone, self.pro_id,
                self.user_type)

      # Méthode retourne les valeurs des attributs utiles pour la BD de l'objet de type manager
    def get_utile_attr_manager(self):
        return (self.surname, self.name, self.address, self.email, self.password, self.phone, self.pro_id,
                self.user_type)

    """méthode de création de compte Admin """


    #def creation_account_admin(self):
        # id = input("entrer id : ")
       #self.name = input("entrer name : ")
       #self.surname = input("entrer surname  : ")
       #self.address = input("entrer address : ")
       #self.email = input("entrer email : ")
       #self.password = input("entrer password : ")
       #self.phone = input("entrer phone : ")
       #self.user_type = "Admin"
       #self.pro_id = input("entrer matricule : ")

        #path = "C:/Users/kardaoui/Desktop/fichier d'entrée/manager.txt"
        #data = import_file(path)
        #create_client_profile(data, "manager")



    """méthode supression de compte Admin """

    def del_account_admin(self):
        connect()
        cursor = cnx.cursor()
        sql_Delete_query = """Delete from admin where id = %s"""
        del_Id = input("quel admin sup : ")
        cursor.execute(sql_Delete_query, (del_Id,))
        cnx.commit()
        cnx.close()





"""test de connexion a la base de données"""
#try:
#    connection = connection.MySQLConnection(host='localhost',
#                                            database='gesti_bank',
#                                            user='root')
#    if connection.is_connected():
#        cursor = connection.cursor()
#        cursor.execute("select database();")
#        record = cursor.fetchone()
#        print("Your connected to database: ", record)
#
#except Error as e:
#    print("Error while connecting to MySQL", e)
#finally:
#    if (connection.is_connected()):
#        connection.close()
#        print("MySQL connection is closed")


if __name__ == "__main__":
   # a1 = Admin(a, b, c, d, e, f, k)
   # lst = []
   # data = a1.get_utile_attr_admin()
   # dat = [data]
   # user_type = k
   # #print(dat)

# admin1 = Admin("2", "bob", "bach", "paris", "sonMail", "passe", "06458 ","185-45",2)
# print("{0} admin {1} matricule {2}".format(admin1.name, admin1.id, admin1.pro_id))
# Admin.creation_account_admin(admin1)
# Admin.del_account_admin(admin1)
#create_client_profile(dat, user_type)

#admin1 = Admin("2", "1er admin", "bach", "paris", "premieradmin@gmail.com", "passe", "06458 ","18545","admin")
    admin1 = Admin(2, "admin", "bach", "paris", "admin@gmail.com", "passe", "06458 ", "18545", "admin")
    lst = []
    data = admin1.get_utile_attr_admin()
    dat = [data]
    create_client_profile(dat,"admin")
    create_client_profile(dat, "admin")
    create_client_profile(dat, "admin")


