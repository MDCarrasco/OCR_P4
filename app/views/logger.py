# app/views/logger.py
# Created at: Tue Jan 19 2021 18:26:15 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/views/logger.py
This is the database actions logger file

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
from time import strftime

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


class Logger():
    """Logger.
    """
    def __init__(self, db_name):
        self.logs_folder = './logs/'
        self.start_datetime = strftime('%d/%m/%Y_%T')
        self.logfile = '{}info_{}.log'.format(self.logs_folder,
                                              self.start_datetime)
        self.file = open(self.logfile, 'a')
        text = ('Started session on {} using {} database...'
                .format(self.start_datetime, db_name))
        self.file.write("{}\n\n".format(text))

    def log_bullet_point_list(self, item_type, items):
        """Summary of log_bullet_point_list.

        Args:
            item_type
            items
        """
        text = '--- {} LIST ---'.format(item_type.upper())
        self.file.write("{}\n".format(text))
        for item in items:
            text = '* {}'.format(item)
            self.file.write("{}\n".format(text))

    def log_number_point_list(self, item_type, items):
        """Summary of log_number_point_list.

        Args:
            item_type
            items
        """
        text = '--- {} LIST ---'.format(item_type.upper())
        self.file.write("{}\n".format(text))
        for i, item in enumerate(items):
            text = '{}. {}'.format(i+1, item)
            self.file.write("{}\n".format(text))

    def log_item(self, item_type, item, item_info):
        """Summary of log_item.

        Args:
            item_type
            item
            item_info
        """
        text = '//////////////////////////////////////////////////////////////'
        self.file.write("{}\n".format(text))
        text = 'Good news, we have some {}!'.format(str(item).upper())
        self.file.write("{}\n".format(text))
        text = '{} INFO: {}'.format(item_type.upper(), item_info)
        self.file.write("{}\n".format(text))
        text = '//////////////////////////////////////////////////////////////'
        self.file.write("{}\n".format(text))

    def log_missing_item_error(self, item, err):
        """Summary of log_missing_item_error.

        Args:
            item
            err
        """
        text = '**************************************************************'
        self.file.write("{}\n".format(text))
        text = 'We are sorry, we have no {}!'.format(str(item).upper())
        self.file.write("{}\n".format(text))
        text = '{}'.format(err.args[0])
        self.file.write("{}\n".format(text))
        text = '**************************************************************'
        self.file.write("{}\n".format(text))

    def log_item_already_stored_error(self, item, item_type, err):
        """Summary of log_item_already_stored_error.

        Args:
            item
            item_type
            err
        """
        text = '**************************************************************'
        self.file.write("{}\n".format(text))
        text = ('Hey! We already have {} in our {} list!'
                .format(str(item).upper(), item_type))
        self.file.write("{}\n".format(text))
        text = '{}'.format(err.args[0])
        self.file.write("{}\n".format(text))
        text = '**************************************************************'
        self.file.write("{}\n".format(text))

    def log_item_not_yet_stored_error(self, item, item_type, err):
        """Summary of log_item_not_yet_stored_error.

        Args:
            item
            item_type
            err
        """
        text = '**************************************************************'
        self.file.write("{}\n".format(text))
        text = ('We don\'t have any {} in our {} list. Please insert it first!'
              .format(str(item).upper(), item_type))
        self.file.write("{}\n".format(text))
        text = '{}'.format(err.args[0])
        self.file.write("{}\n".format(text))
        text = '**************************************************************'
        self.file.write("{}\n".format(text))

    def log_item_stored(self, item, item_type):
        """Summary of log_item_stored.

        Args:
            item
            item_type
        """
        text = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        self.file.write("{}\n".format(text))
        text = ('Hooray! We have just added some {} to our {} list!'
              .format(str(item).upper(), item_type))
        self.file.write("{}\n".format(text))
        text = '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        self.file.write("{}\n".format(text))

    def log_change_item_type(self, older, newer):
        """Summary of log_change_item_type.

        Args:
            older
            newer
        """
        text = '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --'
        self.file.write("{}\n".format(text))
        text = 'Change item tye from "{}" to "{}"'.format(older, newer)
        self.file.write("{}\n".format(text))
        text = '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --'
        self.file.write("{}\n".format(text))

    # pylint: disable=too-many-locals
    def log_tournament_updated(self, item, o_place, o_date,
                               o_round_count, o_rounds, o_players,
                               o_time_control, o_description, n_place,
                               n_date, n_round_count, n_rounds,
                               n_players, n_time_control, n_description):
        """Summary of log_tournament_updated.

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
        text = '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --'
        self.file.write("{}\n".format(text))
        text = ('Change {} place: {} --> {}'
                .format(item, o_place, n_place))
        self.file.write("{}\n".format(text))
        text = ('Change {} date: {} --> {}'
                .format(item, o_date, n_date))
        self.file.write("{}\n".format(text))
        text = ('Change {} round count: {} --> {}'
                .format(item, o_round_count, n_round_count))
        self.file.write("{}\n".format(text))
        text = ('Change {} rounds: {} --> {}'
              .format(item, o_rounds, n_rounds))
        self.file.write("{}\n".format(text))
        text = ('Change {} players: {} --> {}'
              .format(item, o_players, n_players))
        self.file.write("{}\n".format(text))
        text = ('Change {} time control: {} --> {}'
              .format(item, o_time_control, n_time_control))
        self.file.write("{}\n".format(text))
        text = ('Change {} description: {} --> {}'
              .format(item, o_description, n_description))
        self.file.write("{}\n".format(text))
        text = '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --'
        self.file.write("{}\n".format(text))

    def log_player_updated(self, item, o_birth_date, o_gender, o_ranking,
                           n_birth_date, n_gender, n_ranking):
        """Summary of log_player_updated.

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
        text = '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --'
        self.file.write("{}\n".format(text))
        text = ('Change {} birth date: {} --> {}'
              .format(item, o_birth_date, n_birth_date))
        self.file.write("{}\n".format(text))
        text = ('Change {} gender: {} --> {}'
              .format(item, o_gender, n_gender))
        self.file.write("{}\n".format(text))
        text = ('Change {} ranking: {} --> {}'
              .format(item, o_ranking, n_ranking))
        self.file.write("{}\n".format(text))
        text = '---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --'
        self.file.write("{}\n".format(text))
