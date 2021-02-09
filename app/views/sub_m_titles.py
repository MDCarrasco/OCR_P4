# sub_m_titles.py
# Created at: Wed Jan 20 2021 17:06:36 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
sub_m_titles.py

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


class SubMTitles(StrEnum):
    """SMTitles.
    """

    CREATE_TOURNAMENT = 'Organisation de tournoi (Ctrl + C pour annuler)'
    ADD_PLAYER = 'Ajout de joueur (CTRL + C pour annuler)'
    UPDATE_RANK = ('Choix du joueur et modification de son classement '
                   '(CTRL + C pour annuler)')
    PICK_TOURNAMENT = 'Choix du tournoi (CTRL + C pour annuler)'
    LAUNCH_TOURNAMENT = 'Lancement de tournoi'
    TOURNAMENT_FOLLOW_UP = 'Suite du tournoi {}'
    NEW_DB = 'Creation d\'une nouvelle BDD (CTRL + C pour annuler)'
    LOAD_DB = 'Chargement d\'une BDD'
    DISPLAY = 'Affichage'
    DISPLAY_SORTED = 'Tri de la selection'

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
