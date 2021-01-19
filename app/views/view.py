# app/views/view.py
# Created at: Tue Jan 19 2021 18:26:15 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/views/view.py
This is the database actions view file

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
import json

# Other Libs

# Owned

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class View():
    """View.
    """

    @staticmethod
    def show_bullet_point_list(item_type, items):
        """Summary of show_bullet_point_list.

        Args:
            item_type
            items
        """
        print('--- {} LIST ---'.format(item_type.upper()))
        for item in items:
            print('* {}'.format(item))

    @staticmethod
    def show_number_point_list(item_type, items):
        """Summary of show_number_point_list.

        Args:
            item_type
            items
        """
        print('--- {} LIST ---'.format(item_type.upper()))
        for i, item in enumerate(items):
            print('{}. {}'.format(i+1, item))

    @staticmethod
    def show_item(item_type, item, item_info):
        """Summary of show_item.

        Args:
            item_type
            item
            item_info
        """
        print('//////////////////////////////////////////////////////////////')
        print('Good news, we have some {}!'.format(item.upper()))
        print('{} INFO: {}'.format(item_type.upper(), item_info))
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err):
        """Summary of display_missing_item_error.

        Args:
            item
            err
        """
        print('**************************************************************')
        print('We are sorry, we have no {}!'.format(item.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        """Summary of display_item_already_stored_error.

        Args:
            item
            item_type
            err
        """
        print('**************************************************************')
        print('Hey! We already have {} in our {} list!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        """Summary of display_item_not_yet_stored_error.

        Args:
            item
            item_type
            err
        """
        print('**************************************************************')
        print('We don\'t have any {} in our {} list. Please insert it first!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, item_type):
        """Summary of display_item_stored.

        Args:
            item
            item_type
        """
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! We have just added some {} to our {} list!'
              .format(item.upper(), item_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older, newer):
        """Summary of display_change_item_type.

        Args:
            older
            newer
        """
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change item tye from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_tournament_updated(
            item, o_place, o_date, o_round_count, o_rounds, o_players,
            o_time_control, o_description, n_place, n_date, n_round_count,
            n_rounds, n_players, n_time_control, n_description):
        """Summary of display_tournament_updated.

        Args:
            item
            o_place
            o_date
            o_round_count
            o_rounds
            o_players
            o_time_control
            o_description
            n_place
            n_date
            n_round_count
            n_rounds
            n_players
            n_time_control
            n_description
        """

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
        """Summary of display_player_updated.

        Args:
            item
            o_birth_date
            o_gender
            o_ranking
            n_birth_date
            n_gender
            n_ranking
        """

        # pylint: disable=too-many-arguments
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} birth date: {} --> {}'
              .format(item, o_birth_date, n_birth_date))
        print('Change {} gender: {} --> {}'
              .format(item, o_gender, n_gender))
        print('Change {} ranking: {} --> {}'
              .format(item, o_ranking, n_ranking))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
