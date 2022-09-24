import psycopg2

conn = psycopg2.connect(database="lesson_5_sql", user="postgres", password="------")

def create_new_tables():
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS FN_Client (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(40) UNIQUE NOT NULL);
            """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS SN_Client (
            id SERIAL PRIMARY KEY,
            second_name VARCHAR(40) UNIQUE NOT NULL,
            email VARCHAR(40) UNIQUE NOT NULL,
            FN_Client_id INTEGER REFERENCES FN_Client(id) ON DELETE CASCADE);
            """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Phone_number (
            id SERIAL PRIMARY KEY,
            phone_number_1 VARCHAR(40) UNIQUE,
            SN_Client_id INTEGER REFERENCES SN_Client(id) ON DELETE CASCADE);
            """)

    conn.commit()

def insert_new_client(f_name, s_name, email_1, f_client_id, phone_num, client_id):
    with conn.cursor() as cur:
        cur.execute(f"""
            INSERT INTO FN_Client(first_name)
            VALUES('{f_name}');
            """)

        cur.execute(f"""
            INSERT INTO SN_Client(second_name, email, FN_Client_id)
            VALUES('{s_name}', '{email_1}', '{f_client_id}');
            """)

        cur.execute(f"""
            INSERT INTO Phone_number(phone_number_1, SN_Client_id)
            VALUES('{phone_num}', '{client_id}');
            """)

    conn.commit()

def insert_new_phone_number(phone, client_id):
    with conn.cursor() as cur:
        cur.execute(f"""
            INSERT INTO Phone_number(phone_number_1, SN_Client_id)
            VALUES({phone}, {client_id});
            """)

    conn.commit()

def update_some_info(table_name, field_name, value_name, num_id):
    with conn.cursor() as cur:
        cur.execute(f"""
            UPDATE {table_name} SET {field_name} = '{value_name}' 
            WHERE id = {num_id};
            """)

    conn.commit()

def del_phone_num(num_id, num_client_id):
    with conn.cursor() as cur:
        cur.execute(f"""
            DELETE FROM phone_number 
            WHERE id = {num_id} and sn_client_id = {num_client_id}; 
            """)

    conn.commit()

def del_client(num_client_id):
    with conn.cursor() as cur:
        cur.execute(f"""
            DELETE FROM FN_Client 
            WHERE id = {num_client_id}; 
            """)

    conn.commit()

def find_client(first_name=None, second_name=None, par_email=None, phone_num=None):
    with conn.cursor() as cur:
        cur.execute(f"""
            SELECT *
            FROM FN_Client
            JOIN SN_Client ON fn_client_id = fn_client.id
            JOIN Phone_number ON sn_client_id = sn_client.id
            WHERE first_name = '{first_name}' 
                OR second_name = '{second_name}' 
                OR email = '{par_email}' 
                OR phone_number_1 = '{phone_num}'; 
            """)
        print(cur.fetchone())


# create_new_tables()

# insert_new_client('Aleks', 'Ermakov', 'lerma90@bk.ru', '1', '78219990077', '1')
# insert_new_client('Tom', 'Hardi', 'tom7787@mail.ru', '2', '78913324455', '2')
# insert_new_client('Julia', 'Light', 'ula77@bk.ru', '3', '79117777777', '3')
# insert_new_client('James', 'Bond', 'XXX@yyy.com', '4', '70000000000', '4')
# insert_new_client('Man', 'Withoutphone', 'test@yyy.com', '5', ' ', '5')

# insert_new_phone_number('89112345566', '1')
# insert_new_phone_number('2222222222', '1')
# insert_new_phone_number('7777777777', '1')

# update_some_info('FN_Client', 'first_name', 'Genry', '3')
# update_some_info('SN_Client', 'email', 'lexalexa@ya.com', '4')

# del_phone_num('8', '1')
# del_phone_num('2', '2')

# del_client('2')
# del_client('4')

# find_client('Aleks')
# find_client(' ', '79117777777', ' ', ' ')

conn.close()

