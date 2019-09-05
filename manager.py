import mysql.connector
from user import User
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



    # def account_creation(self):



try:
    cnx = mysql.connector.connect(host='localhost',
                                  database='gesti_bank',
                                  user='root',
                                  password='')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Il y a un problème avec votre user name ou password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base n’existe pas")
    else: print(err)

else:

    insert_stmt = (
        "INSERT INTO account_client_request(id, surname, name, adress, proof_of_address)"
        "VALUES (%s, %s, %s, %s, %s)"
    )

    data = [
        (735, 'Sarpi', 'Brice', '636 avenue du Professeur Layton', 'test'),
        (736, 'Joshua', 'Vegas', '93 avenue Victor Hugo', "test2")
    ]

    cursor = cnx.cursor()
    cursor.executemany(insert_stmt, data)


    """select_stmt = "SELECT * FROM annuaire WHERE nom= %(emp_nom)s"
    cursor.execute(select_stmt, { 'emp_nom': 'Doe' })"""

    cnx.close()
