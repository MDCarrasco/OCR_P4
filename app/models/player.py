# player.py
# Created at: Wed Jan 20 2021 17:11:35 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
player.py

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


class Player:
    """Player.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, last_name, first_name, birth_date, gender, rank):
        """Summary of __init__.

        Args:
            last_name
            first_name
            birth_date
            gender
            ranking
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank

    def to_json(self) -> str:
        """Summary of to_json.

        Returns:
            str: json string of self
        """
        return json.dumps(self, default=player_to_dict,
                          sort_keys=True, indent=None)


def player_to_dict(obj) -> dict:
    """Summary of play_or_roun_to_dict.

    Args:
        obj

    Returns:
        dict: player dict

    Raises:
        TypeError
    """
    if isinstance(obj, Player):
        return {
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'birth_date': obj.birth_date,
            'gender': obj.gender,
            'rank': obj.rank
        }
    raise TypeError
