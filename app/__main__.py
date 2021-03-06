# app/__main__.py
# Created at: Fri Jan 22 2021 15:30:49 GMT+0100 (Central European Standard Time)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/__main__.py

Example:
        INSERT example

Todo:
        * INSERT TODO lines
        *

.. _Google Python Style Guide (reference):
http://google.github.io/styleguide/pyguide.html
"""

# pylint: disable=import-error
# Futures

# Generic/Built-in

# Other Libs

# Owned
from controllers.controller import Controller
from views.menu import CYSMenu

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


def main():
    """main.
    """

    ctrlr = Controller(None, None, CYSMenu("chess yo self"), None)
    ctrlr.start()
    return 0


main()
