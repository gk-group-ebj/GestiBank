from connection import connect, cnx
def creation_account_admin():
    connect()
    mySql_insert_query = 'INSERT INTO admin (name, surname, address, email, password, phone, user_type, pro_id)' \
                         '  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    with open("C:/Users/kardaoui/Desktop/fichier d'entrée/clients.txt", "r") as f:
        for line in f.readlines():
            admin = line
            mots = str.split(admin, ", ")
            mots[-1] = mots[-1][:-1]

            cursor = cnx.cursor()
            result = cursor.execute(mySql_insert_query, mots)
    cnx.commit()
    cnx.close()

creation_account_admin()