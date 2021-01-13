"""needs tinydb imports"""
from tinydb import TinyDB
from tinydb import Query
from tinydb import where
import mvc_exceptions as mvc_exc
import json

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
            mydb.tables()
        except ValueError:
            mydb = connect_to_db()
        return func(mydb, *args, **kwargs)
    return inner_func

def disconnect_from_db(mydb=None):
    """disconnects from DB"""
    if mydb is not None:
        mydb.close()
        print('Disconnecting from tinyDB...')

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
    print(table_name)
    mydb.table(table_name)

@connect
def insert_one(mydb, item, table_name):
    """inserts one item checking if it is not already there"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if table_name == 'player':
        exists = table.search((where('first_name') == item.first_name) &
                              (where('last_name') == item.last_name))
    else:
        exists = table.search(where('name') == item.name)
    if exists:
        raise mvc_exc.ItemAlreadyStored(
            'Integrity error: "{}" already stored in table "{}"'
            .format(item.name, table_name))
    if table_name == 'player':
        table.insert(
            {'first_name': item.first_name, 'last_name': item.last_name,
             'birth_date': item.birth_date, 'gender': item.gender,
             'ranking': item.ranking})
    else:
        table.insert(
            {'name': item.name, 'place': item.place, 'date': item.date,
             'round_count': item.round_count, 'rounds':item.rounds,
             'players': item.players, 'time_control': item.time_control,
             'description': item.description})

@connect
def insert_many(mydb, items, table_name):
    """inserts multiple items"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    for item in items:
        if table_name == 'player':
            if table.search(((where('first_name') == item.first_name) &
                            (where('last_name') == item.last_name))):
                raise mvc_exc.ItemAlreadyStored(
                    'Integrity error: "{}" already stored in table "{}"'
                    .format(item.name if item.name else
                            item.name + item.name, table_name))
            table.insert(
                {'fist_name': item.first_name, 'last_name': item.last_name,
                 'birth_date': item.birth_date, 'gender': item.gender,
                 'ranking': item.ranking})
        else:
            if table.search(where('name') == item.name):
                raise mvc_exc.ItemAlreadyStored(
                    'Integrity error: "{}" already stored in table "{}"'
                    .format(item.name if item.name else
                            item.name + item.name, table_name))
            rounds = []
            for roun in item.rounds:
                rounds.append(roun.to_json())
            players = []
            for play in item.players:
                players.append(play.to_json())
            table.insert(
                {'name': item.name, 'place': item.place, 'date': item.date,
                 'round_count': item.round_count,
                 'rounds':rounds, 'players': players,
                 'time_control': item.time_control,
                 'description': item.description})

@connect
def select_one(mydb, item_name, table_name):
    """read one item"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if table_name == 'player':
        item = table.search((where('first_name') == item_name.split(' ')[0]) &
                            (where('last_name') == item_name.split(' ')[1]))
    else:
        item_name = scrub(item_name)
        item = table.search(where('name') == item_name)
    if item:
        return item[0]
    raise mvc_exc.ItemNotStored(
        'Can\'t read "{}" because it\'s not stored in table "{}"'
        .format(item_name, table_name))

@connect
def select_all(mydb, table_name):
    """read whole table"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    return table.all()

@connect
def update_one(mydb, item, table_name):
    """update one item"""
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if table_name == 'player':
        if not table.update(
                {'fist_name': item.first_name, 'last_name': item.last_name,
                 'birth_date': item.birth_date, 'gender': item.gender,
                 'ranking': item.ranking}, Query().name == item.fist_name +
                ' ' + item.last_name):
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored '
                'in the table "{}"'.format(item.first_name + ' ' +
                                           item.last_name, table_name))
    else:
        if not table.update(
                {'name': item.name, 'place': item.place, 'date': item.date,
                 'round_count': item.round_count, 'rounds':item.rounds,
                 'players': item.players, 'time_control': item.time_control,
                 'description': item.description}, Query().name == item.name):
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored '
                'in the table "{}"'.format(item.name, table_name))

#pylint: disable=pointless-string-statement
'''
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
'''
