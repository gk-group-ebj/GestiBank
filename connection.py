from errno import errorcode

import mysql.connector

cnx= mysql.connector.connect(host='localhost',
                              database='gesti_bank',
                              user='root',
                              password='')


def connect():
    try:
        if not cnx.is_connected():
            cnx.connect()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Il y a un problème avec votre user name ou password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base n’existe pas")
        else:
            print(err)
    else:
        pass
