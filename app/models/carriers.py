# carriers.py
# Created at: Wed Jan 20 2021 17:04:01 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
carriers.py

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
from abc import ABC

# Other Libs
from tinydb import TinyDB

# Owned
from tiny_backend import tinydb_backend

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class ModelTinydbCarrier(ABC):
    """ModelTinydbCarrier.
    """

    def __init__(self, db_name):
        """__init__.
        """
        self._db_name = db_name
        self._connection = tinydb_backend.connect_to_db(self._db_name)
        tinydb_backend.create_table(self._connection, self._item_type)

    @property
    def connection(self) -> TinyDB:
        """Summary of connection.

        Returns:
            TinyDB: connection to myDB.json
        """
        return self._connection

    @property
    def item_type(self) -> str:
        """Summary of item_type.

        Returns:
            str: item type
        """
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        """Summary of item_type.

        Args:
            new_item_type
        """
        self._item_type = new_item_type

    def create_item(self, item):
        """Summary of create_item.

        Args:
            item
        """
        tinydb_backend.insert_one(self.connection, item,
                                  table_name=self.item_type)

    def create_items(self, items):
        """Summary of create_items.

        Args:
            items
        """
        tinydb_backend.insert_many(self.connection, items,
                                   table_name=self.item_type)

    def read_item(self, name) -> str:
        """Summary of read_item.

        Args:
            name

        Returns:
            str: json string of item that has name as value for 'name' field
        """
        return tinydb_backend.select_one(self.connection, name,
                                         table_name=self.item_type)

    def read_item_by_rank(self, rank) -> str:
        """Summary of read_item by rank.

        Args:
            rank

        Returns:
            str: json string of item that has name as value for 'rank' field
        """
        return tinydb_backend.select_one_by_rank(self.connection, rank,
                                                 table_name=self.item_type)


    def read_items(self) -> str:
        """Summary of read_items.

        Returns:
            str: json string of all items
        """
        return tinydb_backend.select_all(self.connection,
                                         table_name=self.item_type)

    def update_item(self, item):
        """Summary of update_item.

        Args:
            item
        """
        tinydb_backend.update_one(self.connection, item,
                                  table_name=self.item_type)

    def disconnect(self):
        """disconnect.
        """
        tinydb_backend.disconnect_from_db(self.connection)


class TournamentCarrier(ModelTinydbCarrier):
    """TournamentCarrier.
    """

    def __init__(self, db_name):
        """__init__.
        """
        self._item_type = tinydb_backend.TOURNAMENT
        super().__init__(db_name)


class PlayerCarrier(ModelTinydbCarrier):
    """PlayerCarrier.
    """

    def __init__(self, db_name):
        """__init__.
        """
        self._item_type = tinydb_backend.PLAYER
        super().__init__(db_name)
