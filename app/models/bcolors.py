# app/models/bcolors.py
# Created at: Wed Feb 03 2021 15:59:30 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/models/bcolors.py
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

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class Bcolors:
    """Bcolors.
    """
    # pylint: disable=too-few-public-methods
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def apply_header(cls, string) -> str:
        """Summary of apply_header.

        Args:
            string

        Returns:
            str: Description of return value
        """
        return "{}{}{}".format(cls.HEADER, string, cls.ENDC)

    @classmethod
    def apply_blue(cls, string) -> str:
        """Summary of apply_blue.

        Args:
            string

        Returns:
            str: Description of return value
        """
        return "{}{}{}".format(cls.OKBLUE, string, cls.ENDC)

    @classmethod
    def apply_cyan(cls, string) -> str:
        """Summary of apply_cyan.

        Args:
            string

        Returns:
            str: Description of return value
        """
        return "{}{}{}".format(cls.OKCYAN, string, cls.ENDC)

    @classmethod
    def apply_green(cls, string) -> str:
        """Summary of apply_green.

        Args:
            string

        Returns:
            str: Description of return value
        """
        return "{}{}{}".format(cls.OKGREEN, string, cls.ENDC)

    @classmethod
    def apply_warning(cls, string) -> str:
        """Summary of apply_warning.

        Args:
            string

        Returns:
            str: Description of return value
        """
        return "{}{}{}".format(cls.WARNING, string, cls.ENDC)
    # etc etc etc
