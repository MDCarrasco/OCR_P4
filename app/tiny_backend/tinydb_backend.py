# tinydb_backend.py
# Created at: Tue Jan 19 2021 19:10:12 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
tinydb_backend.py
INSERT docstring paragraph

Example:
        INSERT example

Todo:
        * INSERT TODO lines
        *

.. _Google Python Style Guide (reference):
http://google.github.io/styleguide/pyguide.html
"""

# Futures

# Generic/Built-in

# Other Libs
from typing import Callable
from tinydb import TinyDB
from tinydb import where

# Owned
import exceptions.mvc_exceptions as mvc_exc

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


DB_NAME = 'myDB'
PLAYER = 'player'
TOURNAMENT = 'tournament'


def connect_to_db(name=DB_NAME) -> TinyDB:
    """Summary of connect_to_db.
    Connect to a tinyDB. Create the database if there isn't one yet.
    Open a connection to a tinyDB
    When a database is accessed by multiple connections, and one of the
    processes modifies the database, the tinyDB is locked until that
    transaction is committed.

    Args:
        name Default to DB_NAME

    Returns:
        TinyDB: db object
    """
    mydb = TinyDB('{}.json'.format(name))
    TinyDB.DEFAULT_TABLE = 'my-default'
    TinyDB.DEFAULT_TABLE_KWARGS = {'cache_size': 0}
    print('New connection to tinyDB...')
    return mydb


def connect(func) -> Callable:
    """Summary of connect.
    Tries a very fast query to make sure the db is here.
    else it creates it.

    Args:
        func

    Returns:
        Callable: inner_func()
    """
    def inner_func(mydb, *args, **kwargs):
        try:
            mydb.tables()
        except ValueError:
            mydb = connect_to_db()
        return func(mydb, *args, **kwargs)
    return inner_func


def disconnect_from_db(mydb=None):
    """Summary of disconnect_from_db.

    Args:
        mydb Default to None
    """
    if mydb is not None:
        mydb.close()
        print('Disconnecting from tinyDB...')


def scrub(input_string) -> str:
    """Summary of scrub.
    Clean an input string

    Args:
        input_string

    Returns:
        str: Description of return value
    """
    return ''.join(k for k in input_string if k.isalnum())


@connect
def create_table(mydb, table_name):
    """Summary of create_table.

    Args:
        mydb
        table_name
    """
    table_name = scrub(table_name)
    mydb.table(table_name)


@connect
def insert_one(mydb, item, table_name):
    """Summary of insert_one.
    Inserts one item checking if it is not already there

    Args:
        mydb
        item
        table_name

    Raises:
        mvc_exc: ItemAlreadyStored
    """
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if table_name == PLAYER:
        if table.search(((where('first_name') == item.first_name) &
                         (where('last_name') == item.last_name))):
            raise mvc_exc.ItemAlreadyStored(
                'Integrity error: "{}" already stored in table "{}"'
                .format(item.first_name + ' ' + item.last_name, table_name))
        table.insert(
            {'first_name': item.first_name, 'last_name': item.last_name,
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
             'rounds': rounds, 'players': players,
             'time_control': item.time_control,
             'description': item.description})


@connect
def insert_many(mydb, items, table_name):
    """Summary of insert_many.

    Args:
        mydb
        items
        table_name

    Raises:
        mvc_exc: ItemAlreadyStored
    """
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    for item in items:
        if table_name == PLAYER:
            if table.search(((where('first_name') == item.first_name) &
                            (where('last_name') == item.last_name))):
                raise mvc_exc.ItemAlreadyStored(
                    'Integrity error: "{}" already stored in table "{}"'
                    .format(item.name if item.name else
                            item.name + item.name, table_name))
            table.insert(
                {'first_name': item.first_name, 'last_name': item.last_name,
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
                 'rounds': rounds, 'players': players,
                 'time_control': item.time_control,
                 'description': item.description})


@connect
def select_one(mydb, item_name, table_name):
    """Summary of select_one.

    Args:
        mydb
        item_name
        table_name

    Raises:
        mvc_exc: ItemNotStored
    """
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if table_name == PLAYER:
        item = table.search((where('first_name') == item_name.split(' ')[0]) &
                            (where('last_name') == item_name.split(' ')[1]))
    else:
        item = table.search(where('name') == item_name)
    if item:
        return item[0]
    raise mvc_exc.ItemNotStored(
        'Can\'t read "{}" because it\'s not stored in table "{}"'
        .format(item_name, table_name))


@connect
def select_all(mydb, table_name) -> str:
    """Summary of select_all.
    Read whole table

    Args:
        mydb
        table_name

    Returns:
        str: Description of return value
    """
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    return table.all()


@connect
def update_one(mydb, item, table_name):
    """Summary of update_one.

    Args:
        mydb
        item
        table_name

    Raises:
        mvc_exc: ItemNotStored
    """
    table_name = scrub(table_name)
    table = mydb.table(table_name)
    if table_name == PLAYER:
        if not table.update(
                {'first_name': item.first_name, 'last_name': item.last_name,
                 'birth_date': item.birth_date, 'gender': item.gender,
                 'ranking': item.ranking},
                ((where('first_name') == item.first_name) &
                 (where('last_name') == item.last_name))):
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored '
                'in the table "{}"'.format(item.first_name + ' ' +
                                           item.last_name, table_name))
    else:
        rounds = []
        for roun in item.rounds:
            rounds.append(roun.to_json())
        players = []
        for play in item.players:
            players.append(play.to_json())
        if not table.update(
                {'name': item.name, 'place': item.place, 'date': item.date,
                 'round_count': item.round_count, 'rounds': rounds,
                 'players': players, 'time_control': item.time_control,
                 'description': item.description}, where('name') == item.name):
            raise mvc_exc.ItemNotStored(
                'Can\'t update "{}" because it\'s not stored '
                'in the table "{}"'.format(item.name, table_name))
