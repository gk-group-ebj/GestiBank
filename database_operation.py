from connection import connect, cnx

# Fonction de sauvegarde des infos mises à jour dans la BDD table clients
def create_client_profile(data, table_name, table_format, values_format):

    connect()

    insert_stmt = ("INSERT INTO "+ table_name + table_format + " VALUES "+values_format)

    cursor = cnx.cursor()
    cursor.executemany(insert_stmt, data)
    cnx.close()
