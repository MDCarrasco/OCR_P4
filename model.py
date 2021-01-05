"""The model file needs backend logic"""
import tinydb_backend

class ModelTinydb():
    """tinydb model class"""
    def __init__(self, application_items):
        self._item_type = 'product'
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

    def create_item(self, name, price, quantity):
        """inserts an item into db"""
        tinydb_backend.insert_one(self.connection, name, price, quantity,
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

    def update_item(self, name, price, quantity):
        """updates an item into db"""
        tinydb_backend.update_one(self.connection, name, price, quantity,
                                  table_name=self.item_type)

class Tournament:
    """tournament model class
    Tournament :
        - Name
        - Place
        - Date
        - Round_count
        - Rounds
        - Players
        - Time_control (bullet, blitz, rapid)
        - Description
    """
    def __init__(self):
        pass
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
    def __init__(self):
        pass
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
