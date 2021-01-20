# app/views/menu.py
# Created at: Tue Jan 19 2021 18:24:14 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/views/menu.py
Menu of the chess app

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
import time

# Other Libs
from simple_term_menu import TerminalMenu

# Owned

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"

MAIN_MENU_TITLE = "  Assistant pour tournois d'echecs\n"
MAIN_MENU_ITEMS = ["[1] Lancer un tournoi", "[2] Creer un tournoi",
                   "[3] Consulter un tournoi", "[4] Creer un joueur",
                   "[5] Consulter un joueur", "[6] Modifications",
                   "[q] Quitter"]
EDIT_MENU_TITLE = "  Modifications\n"
EDIT_MENU_ITEMS = ["[1] Editer un tournoi", "[2] Editer un joueur",
                   "[r] Retour au menu principal"]
SKHS = ("fg_yellow",)


class Menu:
    def __init__(self):
        self.main_menu = TerminalMenu(menu_entries=MAIN_MENU_ITEMS,
                                      title=MAIN_MENU_TITLE,
                                      shortcut_key_highlight_style=SKHS,
                                      cycle_cursor=True,
                                      clear_screen=True)

        self.edit_menu = TerminalMenu(EDIT_MENU_ITEMS,
                                      EDIT_MENU_TITLE,
                                      shortcut_key_highlight_style=SKHS,
                                      cycle_cursor=True,
                                      clear_screen=True)


if __name__ == '__main__':

    main_menu_exit = False
    edit_menu_back = False
    menu = Menu()

    while not main_menu_exit:
        main_sel = menu.main_menu.show()

        if main_sel == 0:
            print("Lancement de tournoi")
            time.sleep(5)
        elif main_sel == 1:
            print("Creation de tournoi")
            time.sleep(5)
        elif main_sel == 2:
            print("Consultation de tournoi")
            time.sleep(5)
        elif main_sel == 3:
            print("Creation de joueur")
            time.sleep(5)
        elif main_sel == 4:
            print("Consultation de joueur")
            time.sleep(5)
        elif main_sel == 5:
            while not edit_menu_back:
                edit_sel = menu.edit_menu.show()
                if edit_sel == 0:
                    print("Modification de tournoi")
                    time.sleep(5)
                elif edit_sel == 1:
                    print("Modification de joueur")
                    time.sleep(5)
                elif edit_sel == 2:
                    edit_menu_back = True
                    print("Retour")
            edit_menu_back = False
        elif main_sel == 6:
            main_menu_exit = True
