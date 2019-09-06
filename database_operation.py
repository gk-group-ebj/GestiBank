from connection import connect, cnx

# Fonction d'insertion d'un nouveau profil client /admin / manager dans la BDD associée
def create_client_profile(data, user_type):

    connect()

    # Si il s'agit d'un client de GestiBank ==> redirection vers table SQL client
    if user_type == "client":
        print('client')
        table_name = "client"
        table_format = "(surname, name, global_name, address, email, password, phone, b_account_num, " \
                       "beginning_contract, end_contract, marital_status, children_nb, user_type)"

        values_format = "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        insert_stmt = ("INSERT INTO "+ table_name + table_format + " VALUES "+values_format)
        cursor = cnx.cursor()
        cursor.executemany(insert_stmt, data)


    # Si il s'agit d'un admin de GestiBank ==> redirection vers table SQL admin
    elif user_type == "admin":
        print('admin')
        table_name = "admin"
        table_format = "(surname, name, address, email, password, phone, pro_id, user_type)"
        values_format = "(%s, %s, %s, %s, %s, %s, %s, %s)"

        insert_stmt = ("INSERT INTO " + table_name + table_format + " VALUES " + values_format)

        cursor = cnx.cursor()
        cursor.executemany(insert_stmt, data)


    # Si il s'agit d'un managert de GestiBank ==> redirection vers table SQL manager
    elif user_type == "manager":
        print('agent')

        table_name = "manager"
        table_format = "(surname, name, address, email, password, phone, pro_id, user_type)"
        values_format = "(%s, %s, %s, %s, %s, %s, %s, %s)"

        insert_stmt = ("INSERT INTO " + table_name + table_format + " VALUES " + values_format)
        cursor = cnx.cursor()
        cursor.executemany(insert_stmt, data)


    else:
        print("Type d'utilisiteur inconnu")
        pass


    cnx.close()
