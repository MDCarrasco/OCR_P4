"""needs exceptions"""
import mvc_exceptions as mvc_exc

class Controller():
    """contoller class"""

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self, bullet_points=False):
        """shows items"""
        items = self.model.read_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list(item_type, items)

    def show_item(self, item_name):
        """shows item"""
        try:
            item = self.model.read_item(item_name)
            item_type = self.model.item_type
            self.view.show_item(item_type, item_name, item)
        except mvc_exc.ItemNotStored as exc:
            self.view.display_missing_item_error(item_name, exc)

    def insert_item(self, name, price, quantity):
        """inserts item"""
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type
        try:
            self.model.create_item(name, price, quantity)
            self.view.display_item_stored(name, item_type)
        except mvc_exc.ItemAlreadyStored as exc:
            self.view.display_item_already_stored_error(name, item_type, exc)

    def update_item(self, name, price, quantity):
        """updates item"""
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type
        try:
            older = self.model.read_item(name)
            self.model.update_item(name, price, quantity)
            self.view.display_item_updated(
                name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as exc:
            self.view.display_item_not_yet_stored_error(name, item_type, exc)
            # if the item is not yet stored and we performed an update,
            # we have 2 options : do nothing or call insert_item to add
            # it. self.insert_item(name, price, quantity)

    def update_item_type(self, new_item_type):
        """updates item type"""
        old_item_type = self.model.item_type
        self.model.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)
