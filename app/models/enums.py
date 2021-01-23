# enums.py
# Created at: Wed Jan 20 2021 17:06:36 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
enums.py

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
from backports.strenum import StrEnum

# Owned

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class TimeControl(StrEnum):
    """TimeControl.
    """

    BULLET = 'Bullet'
    BLITZ = 'Blitz'
    RAPID = 'Rapid'

    # pylint: disable=no-member
    @classmethod
    def has_value(cls, value) -> bool:
        """Summary of has_value.

        Args:
            value

        Returns:
            bool: has value or not
        """
        return value in cls._value2member_map_


class Gender(StrEnum):
    """Gender.
    """

    MALE = 'Homme'
    FEMALE = 'Femme'
    OTHER = 'Autre'

    # pylint: disable=no-member
    @classmethod
    def has_value(cls, value) -> bool:
        """Summary of has_value.

        Args:
            value

        Returns:
            bool: has value or not
        """
        return value in cls._value2member_map_
