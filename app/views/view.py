"""needs json import"""
import json

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
    def display_tournament_updated(
            item, o_place, o_date, o_round_count, o_rounds, o_players,
            o_time_control, o_description, n_place, n_date, n_round_count,
            n_rounds, n_players, n_time_control, n_description):
        """displays update of an tournament"""

        # pylint: disable=too-many-arguments
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} place: {} --> {}'
              .format(item, o_place, n_place))
        print('Change {} date: {} --> {}'
              .format(item, o_date, n_date))
        print('Change {} round count: {} --> {}'
              .format(item, o_round_count, n_round_count))
        print('Change {} rounds: {} --> {}'
              .format(item, o_rounds, json.dumps([
                  roun.__dict__ for roun in n_rounds])))
        print('Change {} players: {} --> {}'
              .format(item, o_players, json.dumps([
                  play.__dict__ for play in n_players])))
        print('Change {} time control: {} --> {}'
              .format(item, o_time_control, n_time_control))
        print('Change {} description: {} --> {}'
              .format(item, o_description, n_description))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_player_updated(
            item, o_birth_date, o_gender, o_ranking, n_birth_date,
            n_gender, n_ranking):
        """displays update of an tournament"""

        # pylint: disable=too-many-arguments
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} birth date: {} --> {}'
              .format(item, o_birth_date, n_birth_date))
        print('Change {} gender: {} --> {}'
              .format(item, o_gender, n_gender))
        print('Change {} ranking: {} --> {}'
              .format(item, o_ranking, n_ranking))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
