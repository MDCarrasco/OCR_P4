"""The model file needs abstract and backend logic"""
from abc import ABC
import tinydb_backend

class ModelTinydbCarrier(ABC):
    """tinydb model class"""
    def __init__(self, application_items):
        self._item_type = None
        self._connection = tinydb_backend.connect_to_db(tinydb_backend.DB_NAME)

        tinydb_backend.create_table(self.connection, self._item_type)
        self.create_items(application_items)

    @property
    def connection(self):
        """get connection (mydb)"""
        return self._connection

    @property
    def item_type(self):
        """get item type"""
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, item):
        """inserts an item into db"""
        tinydb_backend.insert_one(self.connection, item,
                                  table_name=self.item_type)

    def create_items(self, items):
        """inserts many items into db"""
        tinydb_backend.insert_many(self.connection, items,
                                   table_name=self.item_type)

    def read_item(self, name):
        """selects an item from db"""
        return tinydb_backend.select_one(self.connection, name,
                                         table_name=self.item_type)

    def read_items(self):
        """selects a table from db"""
        return tinydb_backend.select_all(self.connection,
                                         table_name=self.item_type)

    def update_item(self, item):
        """updates an item in db"""
        tinydb_backend.update_one(self.connection, item,
                                  table_name=self.item_type)


class TournamentCarrier(ModelTinydbCarrier):
    """Tournament Carrier class
    Establishes connection with the db and R/W one to many tournaments
    into it
    """

    def __init__(self, tournament_items):
        self.__item_type = 'tournament'
        super().__init__(tournament_items)

    def method1(self, arg1=None):
        """method1"""
    def method2(self, arg1=None):
        """method2"""

class Tournament:
    """ Tournament :
            - Name
            - Place
            - Date
            - Round_count
            - Rounds
            - Players
            - Time_control (bullet, blitz, rapid)
            - Description
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    def __init__(self, name, place, date, round_count, rounds, players,
                 time_control, description):
        self.__name = name
        self.__place = place
        self.__date = date
        self.__round_count = round_count
        self.__rounds = rounds
        self.__players = players
        self.__time_control = time_control
        self.__description = description

    def method1(self, arg1=None):
        """method1"""
    def method2(self, arg1=None):
        """method2"""


class Player:
    """player model class
    Player :
        - Last_name
        - First_name
        - Birth_date
        - Sex
        - Ranking
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes

    def __init__(self, first_name, last_name, birth_date, sex, ranking):
        self.__item_type = 'player'
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__sex = sex
        self.__ranking = ranking

    def method1(self, arg1=None):
        """method1"""
    def method2(self, arg1=None):
        """method2"""

class Round:
    """round model class
    Round :
        - Name
        - Start_date_time (constructed)
        - End_date_time (set when user creates a round and sets it as finished)
        - List of matches
    """
    def __init__(self):
        pass
    def method1(self, arg1=None):
        """method1"""
    def method2(self, arg1=None):
        """method2"""

class Match:
    """match model class
    Match :
        - list of tuples (tuple = (player, player))
        - list of tuples (tuple = (score, score))
    """
    def __init__(self):
        pass
    def method1(self, arg1=None):
        """method1"""
    def method2(self, arg1=None):
        """method2"""

class Log:
    """log model class
    Log:
        - list of all actors :
            . alphabetical order ;
            . ranking order.
        - list of all players in a tournament :
            . alphabetical order ;
            . ranking order.
        - list of all tournaments.
        - list of all rounds in a tournament.
        - list of all matches in a tournament.
    """
    def __init__(self):
        pass
    def method1(self, arg1=None):
        """method1"""
    def method2(self, arg1=None):
        """method2"""
