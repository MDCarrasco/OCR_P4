"""The model file needs backend logic"""
import tinydb_backend

class ModelTinydb():
    """basic model class"""
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
