# match.py
# Created at: Wed Jan 20 2021 17:18:08 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
match.py
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

# Other Libs

# Owned
from models.bcolors import Bcolors


__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class Match:
    """Match.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self, pone_name, pone_score, ptwo_name, ptwo_score):
        """Summary of __init__.

        Args:
            pone_name
            pone_score
            ptwo_name
            ptwo_score
        """
        self.tuple = ([pone_name, pone_score], [ptwo_name, ptwo_score])

    def __str__(self) -> str:
        self.color_winner()
        return ('{}({}) vs {}({})'.format(self.tuple[0][0], self.tuple[0][1],
                                          self.tuple[1][0], self.tuple[1][1]))

    def color_winner(self):
        """color_winner.
        """
        if self.tuple[0][1] > self.tuple[1][1]:
            self.tuple[0][0] = "{}{}{}".format(Bcolors.OKGREEN,
                                               self.tuple[0][0],
                                               Bcolors.ENDC)
        elif self.tuple[0][1] < self.tuple[1][1]:
            self.tuple[1][0] = "{}{}{}".format(Bcolors.OKGREEN,
                                               self.tuple[1][0],
                                               Bcolors.ENDC)
        else:
            self.tuple[0][0] = "{}{}{}".format(Bcolors.OKCYAN,
                                               self.tuple[0][0],
                                               Bcolors.ENDC)
            self.tuple[1][0] = "{}{}{}".format(Bcolors.OKCYAN,
                                               self.tuple[1][0],
                                               Bcolors.ENDC)
