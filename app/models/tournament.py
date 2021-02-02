# tournament.py
# Created at: Wed Jan 20 2021 17:09:34 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
tournament.py

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

    def __str__(self) -> str:
        """Summary of __str__.

        Returns:
            str: Description of return value
        """
        return ('\nTournoi: {}\nLieu: {}\nDate: {}\nNombre de tours: {}\n'
                'Vitesse: {}\nDescription: {}\n'.format(self.name, self.place,
                                                        self.date,
                                                        self.round_count,
                                                        self.time_control,
                                                        self.description))
