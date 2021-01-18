"""The model file needs abstract and backend logic"""
from abc import ABC
import json
from backports.strenum import StrEnum
import tinydb_backend

class ModelTinydbCarrier(ABC):
    """tinydb model class"""
    def __init__(self):
        self._connection = tinydb_backend.connect_to_db(tinydb_backend.DB_NAME)

        tinydb_backend.create_table(self.connection, self._item_type)

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

    def __init__(self):
        self._item_type = tinydb_backend.TOURNAMENT
        super().__init__()

class PlayerCarrier(ModelTinydbCarrier):
    """Player Carrier class
    Establishes connection with the db and R/W one to many players
    into it
    """

    def __init__(self):
        self._item_type = tinydb_backend.PLAYER
        super().__init__()

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
    # pylint: disable=too-few-public-methods
    def __init__(self, name, place, date, rounds, players, time_control,
                 description, round_count=4):
        self.name = name
        self.place = place
        self.date = date
        self.round_count = round_count
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description

class Player:
    """player model class
    Player :
        - Last_name
        - First_name
        - Birth_date
        - Gender
        - Ranking
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, last_name, first_name, birth_date, gender, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

    def to_json(self):
        """to json"""
        return json.dumps(self, default=play_or_roun_to_dict,
            sort_keys=True, indent=None)

class TimeControl(StrEnum):
    """time_control enum"""
    BULLET = 'bullet'
    BLITZ = 'blitz'
    RAPID = 'rapid'

    @classmethod
    def has_value(cls, value):
        """checks if has value"""
        return value in cls._value2member_map_

class Gender(StrEnum):
    """gender enum"""
    MALE = 'homme'
    FEMALE = 'femme'
    OTHER = 'autre'

    @classmethod
    def has_value(cls, value):
        """checks if has value"""
        return value in cls._value2member_map_

class Round:
    """round model class
    Round :
        - Name
        - Start_date_time (constructed)
        - End_date_time (set when user creates a round and sets it as finished)
        - List of matches
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, name, start_date_time, end_date_time, matches):
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matches = matches

    def to_json(self):
        """to json"""
        return json.dumps(self, default=play_or_roun_to_dict,
            sort_keys=True, indent=None)


class Match:
    """match model class
    Match :
        - p1 = (player, score)
        - p2 = (player, score)
        - contains tuple(p1, p2)
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, pone_name, pone_score, ptwo_name, ptwo_score):
        self.tuple = ([pone_name, pone_score], [ptwo_name, ptwo_score])

def play_or_roun_to_dict(obj):
    """to dict"""
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
