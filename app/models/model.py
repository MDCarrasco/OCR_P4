# app/models/model.py
# Created at: Tue Jan 19 2021 18:30:58 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/models/model.py

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
import json

# Other Libs
from backports.strenum import StrEnum
from tinydb import TinyDB

# Owned
import tinydb_backend

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

    def __init__(self):
        """__init__.
        """
        self._connection = tinydb_backend.connect_to_db(tinydb_backend.DB_NAME)

        tinydb_backend.create_table(self.connection, self._item_type)

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


class TournamentCarrier(ModelTinydbCarrier):
    """TournamentCarrier.
    """

    def __init__(self):
        """__init__.
        """
        self._item_type = tinydb_backend.TOURNAMENT
        super().__init__()


class PlayerCarrier(ModelTinydbCarrier):
    """PlayerCarrier.
    """

    def __init__(self):
        """__init__.
        """
        self._item_type = tinydb_backend.PLAYER
        super().__init__()


class Tournament:
    """Tournament.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, name, place, date, rounds, players, time_control,
                 description, round_count=4):
        """Summary of __init__.

        Args:
            name
            place
            date
            rounds
            players
            time_control
            description
            round_count Default to 4
        """
        self.name = name
        self.place = place
        self.date = date
        self.round_count = round_count
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description


class Player:
    """Player.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        """Summary of __init__.

        Args:
            last_name
            first_name
            birth_date
            gender
            ranking
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def to_json(self) -> str:
        """Summary of to_json.

        Returns:
            str: json string of self
        """
        return json.dumps(self, default=play_or_roun_to_dict,
                          sort_keys=True, indent=None)


class TimeControl(StrEnum):
    """TimeControl.
    """

    BULLET = 'bullet'
    BLITZ = 'blitz'
    RAPID = 'rapid'

    # pylint: disable=no-member
    @classmethod
    def has_value(cls, value) -> bool:
        """Summary of has_value.

        Args:
            value

        Returns:
            bool: has value or not
        """
        return value in cls._value2member_map_


class Gender(StrEnum):
    """Gender.
    """

    MALE = 'homme'
    FEMALE = 'femme'
    OTHER = 'autre'

    # pylint: disable=no-member
    @classmethod
    def has_value(cls, value) -> bool:
        """Summary of has_value.

        Args:
            value

        Returns:
            bool: has value or not
        """
        return value in cls._value2member_map_


class Round:
    """Round.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, name, start_date_time, end_date_time, matches):
        """Summary of __init__.

        Args:
            name
            start_date_time
            end_date_time
            matches
        """
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matches = matches

    def to_json(self) -> str:
        """Summary of to_json.

        Returns:
            str: json string of self
        """
        return json.dumps(self, default=play_or_roun_to_dict,
                          sort_keys=True, indent=None)


class Match:
    """Match.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, pone_name, pone_score, ptwo_name, ptwo_score):
        """Summary of __init__.

        Args:
            pone_name
            pone_score
            ptwo_name
            ptwo_score
        """
        self.tuple = ([pone_name, pone_score], [ptwo_name, ptwo_score])


def play_or_roun_to_dict(obj) -> dict:
    """Summary of play_or_roun_to_dict.

    Args:
        obj

    Returns:
        dict: either player dict or round dict

    Raises:
        TypeError
    """
    if isinstance(obj, Player):
        return {
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'birth_date': obj.birth_date,
            'gender': obj.gender,
            'ranking': obj.ranking
        }
    if isinstance(obj, Round):
        return {
            'name': obj.name,
            'start_date_time': obj.start_date_time,
            'end_date_time': obj.end_date_time,
            'matches': obj.matches
        }
    raise TypeError
