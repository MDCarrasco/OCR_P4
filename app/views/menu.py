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
from time import sleep
from time import time

# Other Libs
# pylint: disable=import-error
from simple_term_menu import TerminalMenu
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
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

FIGLET_FONT = "slant"
APP_TITLE = "chess yo self"
APP_TITLE_F = Figlet(font=FIGLET_FONT)


def title_string(string) -> str:
    """Summary of title_string.

    Args:
        string

    Returns:
        str: Description of return value
    """
    return "{}\n  {}\n".format(APP_TITLE_F.renderText(APP_TITLE), string)


MAIN_MENU_TITLE = title_string("Assistant pour tournois d'echecs")
MAIN_MENU_ITEMS = ["[1] Organiser un tournoi", "[2] Ajouter des joueurs",
                   "[3] Modifier le classement", "[4] Lancer un tournoi",
                   "[5] Afficher", "[s] Sauvegarder", "[c] Charger",
                   "[q] Quitter"]
DISPLAY_MENU_TITLE = title_string("Affichage")
DISPLAY_MENU_ITEMS = ["[1] Tous les joueurs", "[2] Les joueurs d'un tournoi",
                      "[3] Tous les tournois", "[4] Tous les tours d'un tournoi",
                      "[5] Tous les matchs d'un tournoi", "[r] Retour"]
DISPLAY_SORTED_MENU_TITLE = title_string("Tri de la selection")
DISPLAY_SORTED_MENU_ITEMS = ["[1] Par ordre alphabetique", "[2] Par classement",
                             "[r] Retour"]
SKHS = ("fg_yellow",)

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


# pylint: disable=too-few-public-methods
class NumberValidator(Validator):
    """NumberValidator.
    """

    # pylint: disable=raise-missing-from
    # pylint: disable=no-self-use
    def validate(self, document):
        """Summary of validate.

        Args:
            document

        Raises:
            ValidationError
        """
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Entrez un nombre',
                cursor_position=len(document.text))  # Move cursor to end
        try:
            assert int(document.text) > 0
        except AssertionError:
            raise ValidationError(
                message='Entrez un nombre plus grand que 0',
                cursor_position=len(document.text))  # Move cursor to end


tournament_form = [
    {
        'type': 'input',
        'name': 'name',
        'message': 'Nom du tournoi:'
    },
    {
        'type': 'input',
        'name': 'place',
        'message': 'Lieu du tournoi:'
    },
    {
        'type': 'checkbox',
        'message': 'Selectionnez les joueurs',
        'name': 'players',
        'choices': [
            {
                'name': 'player1'
            },
            {
                'name': 'player2'
            },
            {
                'name': 'player3'
            },
            {
                'name': 'player4'
            },
            {
                'name': 'player5'
            },
            {
                'name': 'player6'
            },
            {
                'name': 'player7'
            },
            {
                'name': 'player8'
            },
            {
                'name': 'player9'
            },
            {
                'name': 'player10'
            },
            {
                'name': 'player11'
            },
            {
                'name': 'player12'
            }
        ],
        'validate': lambda answer: 'Vous devez choisir au moins 8 joueurs.'
        if len(answer) < 8 else True
    },
    {
        'type': 'list',
        'name': 'time_control',
        'message': 'Controle du temps:',
        'choices': ['Bullet', 'Blitz', 'Rapid'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'description',
        'message': 'Remarques generales:'
    },
    {
        'type': 'input',
        'name': 'round_count',
        'message': 'Nombre de tours (superieur a 0 SINON --> 4):',
        'default': '4',
        'validate': NumberValidator,
        'filter': lambda val: int(val) if int(val) > 0 else None
    },
    {
        'type': 'confirm',
        'name': 'done',
        'message': 'Tous les champs sont-ils corrects?',
        'default': False
    }
]

main_menu = TerminalMenu(menu_entries=MAIN_MENU_ITEMS,
                         title=MAIN_MENU_TITLE,
                         shortcut_key_highlight_style=SKHS,
                         cycle_cursor=True,
                         clear_screen=True)

display_menu = TerminalMenu(menu_entries=DISPLAY_MENU_ITEMS,
                            title=DISPLAY_MENU_TITLE,
                            shortcut_key_highlight_style=SKHS,
                            cycle_cursor=True,
                            clear_screen=True)

display_sorted_menu = TerminalMenu(menu_entries=DISPLAY_SORTED_MENU_ITEMS,
                                   title=DISPLAY_SORTED_MENU_TITLE,
                                   shortcut_key_highlight_style=SKHS,
                                   cycle_cursor=True,
                                   clear_screen=True)


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


if __name__ == '__main__':

    # pylint: disable=invalid-name
    main_menu_exit = False
    display_menu_back = False
    display_sorted_menu_back = False

    while not main_menu_exit:
        main_sel = main_menu.show()
        if main_sel == 0:
            print(title_string(
                "Organisation de tournoi (Ctrl + C pour annuler)"))
            answers = prompt(tournament_form, style=style)
            printd("\nSauvegarde du nouveau tournoi")
        elif main_sel == 1:
            while not display_menu_back:
                display_sel = display_menu.show()
                if display_sel == 0:
                    print("Edit Config Selected")
                    sleep(5)
                elif display_sel == 1:
                    print("Save Selected")
                    sleep(5)
                elif display_sel == 2:
                    display_menu_back = True
                    print("Back Selected")
            display_menu_back = False
            # print("Ajout de joueurs")
            # sleep(5)
        elif main_sel == 2:
            print("Modification du classement")
            sleep(5)
        elif main_sel == 3:
            print("Lancement de tournoi")
            sleep(5)
        elif main_sel == 4:
            while not display_menu_back:
                display_sel = display_menu.show()
                if display_sel == 0:
                    while not display_sorted_menu_back:
                        display_sorted_sel = display_sorted_menu.show()
                        if display_sorted_sel == 0:
                            print("Liste des joueurs par ordre alphabetique")
                            sleep(5)
                        elif display_sorted_sel == 1:
                            print("Liste des joueurs par classement")
                            sleep(5)
                        elif display_sorted_sel == 2:
                            display_sorted_menu_back = True
                    display_sorted_menu_back = False
                elif display_sel == 1:
                    while not display_sorted_menu_back:
                        display_sorted_sel = display_sorted_menu.show()
                        if display_sorted_sel == 0:
                            print("Liste des joueurs d'un tournoi"
                                  " par ordre alphabetique")
                            sleep(5)
                        elif display_sorted_sel == 1:
                            print("Liste des joueurs d'un tournoi"
                                  " par classement")
                            sleep(5)
                        elif display_sorted_sel == 2:
                            display_sorted_menu_back = True
                    display_sorted_menu_back = False
                elif display_sel == 2:
                    print("Liste des tournois")
                    sleep(5)
                elif display_sel == 3:
                    print("Liste des tours d'un tournoi")
                    sleep(5)
                elif display_sel == 4:
                    print("Liste des matchs d'un tournoi")
                    sleep(5)
                elif display_sel == 5:
                    display_menu_back = True
            display_menu_back = False
        elif main_sel == 5:
            print("Sauvegarde")
            sleep(5)
        elif main_sel == 6:
            print("Chargement")
        elif main_sel == 7:
            main_menu_exit = True
