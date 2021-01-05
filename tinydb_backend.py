"""needs tinydb imports"""
from tinydb import TinyDB #pylint: disable=E0401
from tinydb import Query #pylint: disable=E0401
from tinydb import where #pylint: disable=E0401
import mvc_exceptions as mvc_exc

DB_NAME = 'myDB'

def connect_to_db(name=DB_NAME):
    """Connect to a tinyDB. Create the database if there isn't one yet.
    Open a connection to a tinyDB
    When a database is accessed by multiple connections, and one of the
    processes modifies the database, the tinyDB is locked until that
    transaction is committed.

    Parameters
    ----------
    name : str
        database name (without .json extension).

    Returns
    -------
    mydb:
        db object
    """
    mydb = TinyDB('{}.json'.format(name))
    TinyDB.DEFAULT_TABLE = 'my-default'
    TinyDB.DEFAULT_TABLE_KWARGS = {'cache_size': 0}
    print('New connections to tinyDB...')
    return mydb

def connect(func):
    """Tries a very fast query to make sure the db is here.
    else it creates it.
    """
    def inner_func(mydb, *args, **kwargs):
        try:
            res = mydb.search(Query().type == 'table')
        except not res:
            mydb = connect_to_db()
        return func(mydb, *args, **kwargs)
    return inner_func

def disconnect_from_db(mydb=None):
    """disconnects from DB"""
    if mydb is not None:
        mydb.close()

def scrub(input_string):
    """Clean an input string

    Parameters
    ----------
    input_string : str

    Returns
    -------
    str
    """
    return ''.join(k for k in input_string if k.isalnum())

@connect
def create_table(mydb, table_name):
    """creates a table"""
    table_name = scrub(table_name)
    mydb.table(table_name)

@connect
def insert_one(mydb, name, price, quantity, table_name):
    """inserts one item checking if it is not already there"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if table.search(where('name') == name):
        raise mvc_exc.ItemAlreadyStored(
            'Integrity error: "{}" already stored in table "{}"'
            .format(name, table_name))
    table.insert({'name': name, 'price': price, 'quantity': quantity})

@connect
def insert_many(mydb, items, table_name):
    """inserts multiple items"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    for item in items:
        if table.search(where('name') == item['name']):
            raise mvc_exc.ItemAlreadyStored(
                'Integrity error: "{}" already stored in table "{}"'
                .format(item['name'], table_name))
        table.insert(
            {'name': item['name'],
             'price': item['price'],
             'quantity': item['quantity']})

@connect
def select_one(mydb, item_name, table_name):
    """read one item"""
    table_name = scrub(table_name)
    item_name = scrub(item_name)
    table = mydb.table(table_name)
    item = table.search(where('name') == item_name)
    if item:
        return item
    raise mvc_exc.ItemNotStored(
        'Can\'t read "{}" because it\'s not stored in table "{}"'
        .format(item_name, table_name))

@connect
def select_all(mydb, table_name):
    """read whole table"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    return list(table)

@connect
def update_one(mydb, name, price, quantity, table_name):
    """update one item"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if not table.update({'name': name, 'price': price,
                         'quantity': quantity},
                        Query().name == name):
        raise mvc_exc.ItemNotStored(
            'Can\'t update "{}" because it\'s not stored '
            'in the table "{}"'.format(name, table_name))

def main():
    """main function"""
    table_name = 'items'
    mydb = connect_to_db()
    create_table(mydb, table_name)
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5}
    ]

    # CREATE
    insert_many(mydb, my_items, table_name)
    insert_one(mydb, 'beer', price=2.0, quantity=5, table_name='items')
    # test item already stored exception
    # insert_one(mydb, 'milk', price=1.0, quantity=3, table_name='items')

    # READ
    print('SELECT milk')
    print(select_one(mydb, 'milk', table_name='items'))
    print('SELECT all')
    print(select_all(mydb, table_name='items'))
    # if we try to select an object not stored we get an ItemNotStored
    # exception
    # print(select_one(mydb, 'pizza', table_name='items'))

    # UPDATE
    print('UPDATE bread, SELECT bread')
    update_one(mydb, 'bread', price=1.5, quantity=5, table_name='items')
    print(select_one(mydb, 'bread', table_name='items'))
    # if we try to update an object not stored we get an ItemNotStored
    # exception
    # print('UPDATE pizza')
    # update_one(mydb, 'pizza', price=1.5, quantity=5, table_name='items')

    # close connection
    disconnect_from_db(mydb)

if __name__ == '__main__':
    main()
