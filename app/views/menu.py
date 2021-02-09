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
import pydoc

# Other Libs
# pylint: disable=import-error
from simple_term_menu import TerminalMenu
from PyInquirer import style_from_dict, Token, prompt

# Owned
# from models.bcolors import Bcolors
from views.cli_view import CliView
from views.validators import DateValidator, FutureDateValidator
from views.validators import StringValidator, NumberValidator
from views.sub_m_titles import SubMTitles


__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"

# pylint: disable=too-many-instance-attributes
class CYSMenu(CliView):
    """Menu.
    """

    def __init__(self, app_title):
        super().__init__(app_title)

        self.db_name_form = [
            {
                'type': 'input',
                'name': 'db_name',
                'message': 'Nom de la nouvelle BDD:',
                'validate': StringValidator,
                'filter': lambda val: "".join(x for x in val if x.isalnum())
            },
        ]

        # Variable forms
        self.player_form = [
            {
                'type': 'input',
                'name': 'first_name',
                'message': 'Prenom:',
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'last_name',
                'message': 'Nom de famille:',
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'birth_date',
                'message': 'Date de naissance:',
                'validate': DateValidator
            },
            {
                'type': 'list',
                'name': 'gender',
                'message': 'Genre:',
                'choices': ['Homme', 'Femme', 'Autre'],
            },
            {
                'type': 'input',
                'name': 'rank',
                'message': 'Classement:',
                'validate': None,
                'filter': lambda val: int(val) if int(val) > 0 else None
            },
            {
                'type': 'confirm',
                'name': 'done',
                'message': 'Tous les champs sont-ils corrects?',
                'default': False
            }
        ]
        self.tournament_form = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Nom du tournoi:',
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'place',
                'message': 'Lieu du tournoi:',
                'validate': StringValidator
            },
            {
                'type': 'input',
                'name': 'date',
                'message': 'Date du tournoi:',
                'validate': FutureDateValidator
            },
            {
                'type': 'checkbox',
                'message': 'Selectionnez les joueurs',
                'name': 'players',
                'choices': [],
                'validate': lambda choices: 'Au moins 8 joueurs'
                if len(choices['players']) < 8 else True
            },
            {
                'type': 'list',
                'name': 'time_control',
                'message': 'Controle du temps:',
                'choices': ['Bullet', 'Blitz', 'Rapid'],
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
                'type': 'input',
                'name': 'description',
                'message': 'Remarques generales:',
                'validate': None
            },
            {
                'type': 'confirm',
                'name': 'done',
                'message': 'Tous les champs sont-ils corrects?',
                'default': False
            }
        ]
        self.tournament_pick = [
            {
                'type': 'list',
                'name': 'tournament',
                'message': 'Selectionnez le tournoi',
                'choices': [],
            },
        ]
        self.player_pick = [
            {
                'type': 'list',
                'name': 'name',
                'message': 'Selectionnez le joueur',
                'choices': [],
            },
            {
                'type': 'input',
                'name': 'new_rank',
                'message': 'Nouveau classement:',
                'validate': NumberValidator,
                'filter': lambda val: int(val) if int(val) > 0 else None
            },

        ]
        self.who_won = [
            {
                'type': 'list',
                'name': 'fullname',
                'message': 'Selectionnez le vainqueur',
                'choices': [],
            },
        ]

        # Bools and check variables
        self.load_db_sel = -1
        self.main_menu_exit = False
        self.display_menu_back = False
        self.display_sorted_menu_back = False
        self.load_db_menu_back = False

        # Title
        self.main_menu_title = self.title_string(
            "Assistant pour tournois d'echecs")

        # Menu Items
        self.main_nemu_items = [
            "[1] Organiser un tournoi", "[2] Ajouter un joueur",
            "[3] Modifier le classement", "[4] Lancer un tournoi",
            "[5] Afficher", "[n] Nouvelle BDD", "[c] Charger",
            "[q] Quitter"
        ]
        self.display_menu_items = [
            "[1] Tous les joueurs", "[2] Tous les tournois",
            "[3] Tous les joueurs d'un tournoi",
            "[4] Tous les tours d'un tournoi",
            "[5] Tous les matchs d'un tournoi", "[r] Retour"
        ]
        self.display_sorted_menu_items = [
            "[1] Par ordre alphabetique",
            "[2] Par classement", "[r] Retour"
        ]

        # Menus
        self.main_menu = TerminalMenu(
            menu_entries=self.main_nemu_items,
            title=self.main_menu_title,
            shortcut_key_highlight_style=self.skhs,
            cycle_cursor=True,
            clear_screen=True
        )
        self.display_menu = TerminalMenu(
            menu_entries=self.display_menu_items,
            title=self.title_string(SubMTitles.DISPLAY),
            shortcut_key_highlight_style=self.skhs,
            cycle_cursor=True,
            clear_screen=True
        )
        self.display_sorted_menu = TerminalMenu(
            menu_entries=self.display_sorted_menu_items,
            title=self.title_string(SubMTitles.DISPLAY_SORTED),
            shortcut_key_highlight_style=self.skhs,
            cycle_cursor=True,
            clear_screen=True
        )
        self.load_db_menu = TerminalMenu(
            menu_entries=[],
            title=self.title_string(SubMTitles.LOAD_DB),
            shortcut_key_highlight_style=self.skhs,
            cycle_cursor=True,
            clear_screen=True
        )

        # Style
        self.style = style_from_dict({
            Token.QuestionMark: '#E91E63 bold',
            Token.Selected: '#673AB7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#2196f3 bold',
            Token.Question: '',
        })

    def print_title_string(self, that):
        """Summary of print_title_string.

        Args:
            that
        """
        print(self.title_string(that))

    def prompt_form(self, form) -> dict:
        """Summary of prompt_form.

        Args:
            form

        Returns:
            dict: answers
        """
        return prompt(form, style=self.style)

    @staticmethod
    def print_pydoc(those):
        """Summary of print_pydoc.

        Args:
            those: a list of things
        """
        pydoc.pager("\n".join(map(str, those)))
