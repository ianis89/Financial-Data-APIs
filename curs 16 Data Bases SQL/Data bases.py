import sqlite3


def create_table():
    # let's  connect  and create the databases
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    #        CREATE TABLE is the command, crypto is the name of the table, name & price are the columns' names
    cursor.execute("CREATE TABLE crypto ('name' TEXT, 'price' INTEGER)")
    # to save the changes to the database
    connection.commit()
    # we have to close the connection
    connection.close()


def add_coin(name: str, price: int):
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    # INSERT to add a new row, INTO <table_name>
    cursor.execute("INSERT INTO crypto (name, price) VALUES ('" + name + "'," + str(price) + ")")
    connection.commit()
    connection.close()

#add_coin ("bitcoin", 38000)

def read_all():
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    # * means all, SELECT is used for query/read
    cursor.execute("SELECT * FROM crypto")
    info = cursor.fetchall()
    connection.close()
    print(info)

#   read_all()

def read_columns(columns: list[str]):
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    cursor.execute("SELECT " + ",".join(columns) + " FROM crypto")
    info = cursor.fetchall()
    connection.close()
    print(info)

#read_columns(["price"])

def read_with_filter():
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    #             here * means all columns  ;  name of the column = <value>, between '' if TEXT
    cursor.execute("SELECT * FROM crypto WHERE price < 1")
    # we can put multiple conditions after WHERE with AND OR just like in python
    info = cursor.fetchall()
    connection.close()
    print(info)

#read_with_filter()

def delete_row():
    connection = sqlite3.connect("first.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM crypto WHERE name = 'bitcoin'")
    connection.commit()
    connection.close()

#delete_row()

def update_row():
    # command to update a row, SET to change, WHERE to find
    # UPDATE crypto SET price = 39000 WHERE name = 'bitcoin'
    pass

