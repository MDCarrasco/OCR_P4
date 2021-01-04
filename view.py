"""view"""
class View():
    """view class"""

    @staticmethod
    def show_bullet_point_list(item_type, items):
        """shows list with bulletpoints"""
        print('--- {} LIST ---'.format(item_type.upper()))
        for item in items:
            print('* {}'.format(item))

    @staticmethod
    def show_number_point_list(item_type, items):
        """shows list with numberpoints"""
        print('--- {} LIST ---'.format(item_type.upper()))
        for i, item in enumerate(items):
            print('{}. {}'.format(i+1, item))

    @staticmethod
    def show_item(item_type, item, item_info):
        """shows item"""
        print('//////////////////////////////////////////////////////////////')
        print('Good news, we have some {}!'.format(item.upper()))
        print('{} INFO: {}'.format(item_type.upper(), item_info))
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err):
        """displays missing item error message"""
        print('**************************************************************')
        print('We are sorry, we have no {}!'.format(item.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        """displays item already stored error message"""
        print('**************************************************************')
        print('Hey! We already have {} in our {} list!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        """displays item not yet stored error message"""
        print('**************************************************************')
        print('We don\'t have any {} in our {} list. Please insert it first!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, item_type):
        """displays item stored"""
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! We have just added some {} to our {} list!'
              .format(item.upper(), item_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older, newer):
        """displays item type change"""
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change item tye from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity):
        """displays update of an item"""
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} price: {} --> {}'
              .format(item, o_price, n_price))
        print('Change {} quantity: {} --> {}'
              .format(item, o_quantity, n_quantity))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
