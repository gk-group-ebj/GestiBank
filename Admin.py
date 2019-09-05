from mysql.connector import Error, connection
from user import User
from connection import connect, cnx


class Admin(User):
    def __init__(self, id, name, surname, address, email, password, pro_id, phone, user_type):
        self.pro_id = pro_id
        User.__init__(self, id, name, surname, address, email, password , phone, user_type)

    """méthode de création de compte Admin """

    def creation_account_admin(self):
        # id = input("entrer id : ")
        self.name = input("entrer name : ")
        self.surname = input("entrer surname  : ")
        self.address = input("entrer address : ")
        self.email = input("entrer email : ")
        self.password = input("entrer password : ")
        self.phone = input("entrer phone : ")
        self.user_type = "Admin"
        self.pro_id = input("entrer matricule : ")

        connect()
        mySql_insert_query = 'INSERT INTO admin (name, surname, address, email, password, phone, user_type, pro_id)' \
                             '  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

        data = (self.name, self.surname, self.address, self.email, self.password, self.phone, self.user_type, self.pro_id)
        cursor = cnx.cursor()
        result = cursor.execute(mySql_insert_query, data)
        cnx.commit()
        cnx.close()

    """méthode supression de compte Admin """

    def del_account_admin(self):
        connect()
        cursor = cnx.cursor()
        sql_Delete_query = """Delete from admin where id = %s"""
        de_Id = input("quel admin sup : ")
        cursor.execute(sql_Delete_query, (de_Id,))
        cnx.commit()
        cnx.close()




admin1 = Admin("2", "bob", "bach", "paris", "sonMail", "passe", "06458 ","185-45",2)
#print("{0} admin {1} matricule {2}".format(admin1.name, admin1.id, admin1.pro_id))
Admin.creation_account_admin(admin1)
#Admin.del_account_admin(admin1)






"""test de connexion a la base de données"""
try:
    connection = connection.MySQLConnection(host='localhost',
                                            database='gesti_bank',
                                            user='root')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

