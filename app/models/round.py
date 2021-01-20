# round.py
# Created at: Wed Jan 20 2021 17:16:22 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
round.py
INSERT docstring paragraph

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


class Round:
    """Round.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, name, start_date_time, end_date_time, matches):
        """Summary of __init__.

        Args:
            name
            start_date_time
            end_date_time
            matches
        """
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.matches = matches

    def to_json(self) -> str:
        """Summary of to_json.

        Returns:
            str: json string of self
        """
        return json.dumps(self, default=round_to_dict,
                          sort_keys=True, indent=None)


def round_to_dict(obj) -> dict:
    """Summary of play_or_roun_to_dict.

    Args:
        obj

    Returns:
        dict: either player dict or round dict

    Raises:
        TypeError
    """
    if isinstance(obj, Round):
        return {
            'name': obj.name,
            'start_date_time': obj.start_date_time,
            'end_date_time': obj.end_date_time,
            'matches': obj.matches
        }
    raise TypeError
