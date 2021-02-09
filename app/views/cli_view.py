# app/views/cli_view.py
# Created at: Fri Jan 22 2021 14:26:16 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/views/cli_view.py
Command line interface view

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
import os
from time import sleep
from time import time

# Other Libs
from pyfiglet import Figlet

# Owned

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"

class CliView():
    """CliView.
    """
    def __init__(self, app_title):
        """Summary of __init__.

        Args:
            app_title
        """
        self.figlet_font = "slant"
        self.skhs = ("fg_yellow",)
        self.app_title = app_title
        self.app_title_f = Figlet(font=self.figlet_font)

    def title_string(self, string) -> str:
        """Summary of title_string.

        Args:
            string

        Returns:
            str: Description of return value
        """
        return "{}\n  {}\n".format(self.app_title_f
                                   .renderText(self.app_title), string)


    @staticmethod
    def printd(text, duration=4, delay=.5):
        """Summary of printd.

         Args:
             text
             duration Default to 4
             delay Default to .5
         """
        print(end=text)
        t_end = time() + duration
        n_dots = 0

        while time() < t_end:
            if n_dots == 3:
                print(end='\b\b\b', flush=True)
                print(end='   ',    flush=True)
                print(end='\b\b\b', flush=True)
                n_dots = 0
            else:
                print(end='.', flush=True)
                n_dots += 1
            sleep(delay)

    @staticmethod
    def clear():
        """clear.
        """
        os.system('clear')
