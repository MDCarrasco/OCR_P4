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
import os
import json
import pydoc

# Other Libs
# pylint: disable=import-error
from simple_term_menu import TerminalMenu
from PyInquirer import style_from_dict, Token, prompt

# Owned
from controllers.controller import Controller, NumberValidator, DateValidator
from controllers.controller import FutureDateValidator
from models.carriers import TournamentCarrier, PlayerCarrier
from models.tournament import Tournament
from models.player  import Player
from models.round import Round
from models.enums import TimeControl, Gender
from views.cli_view import CliView, printd
from views.logger import Logger


__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"

class CYSMenu(CliView):
    """Menu.
    """
    PLAYER_FORM = [
        {
            'type': 'input',
            'name': 'first_name',
            'message': 'Prenom:'
        },
        {
            'type': 'input',
            'name': 'last_name',
            'message': 'Nom de famille:'
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
            'choices': [Gender.MALE,
                        Gender.FEMALE,
                        Gender.OTHER],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'input',
            'name': 'rank',
            'message': 'Classement:',
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

    TOURNAMENT_PICK = [
        {
            'type': 'list',
            'name': 'tournament',
            'message': 'Selectionnez le tournoi',
            'choices': ['tournoi1', 'tournoi2', 'tournoi3'],
        },
    ]

    def __init__(self, app_title):
        super().__init__(app_title)
        self.tournament_form = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Nom du tournoi:',
                'validate': None
            },
            {
                'type': 'input',
                'name': 'place',
                'message': 'Lieu du tournoi:'
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
                'validate': lambda choices: 'Vous devez choisir au moins 8 joueurs'
                if len(choices['players']) < 8 else True
            },
            {
                'type': 'list',
                'name': 'time_control',
                'message': 'Controle du temps:',
                'choices': [TimeControl.BULLET,
                            TimeControl.BLITZ,
                            TimeControl.RAPID],
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
        self.main_menu_exit = False
        self.display_menu_back = False
        self.display_sorted_menu_back = False
        self.main_menu_title = self.title_string(
            "Assistant pour tournois d'echecs")
        self.main_nemu_items = [
            "[1] Organiser un tournoi", "[2] Ajouter un joueur",
            "[3] Modifier le classement", "[4] Lancer un tournoi",
            "[5] Afficher", "[s] Sauvegarder", "[c] Charger",
            "[q] Quitter"
        ]
        self.display_menu_title = self.title_string("Affichage")
        self.display_menu_items = [
            "[1] Tous les joueurs", "[2] Tous les tournois",
            "[3] Tous les joueurs d'un tournoi",
            "[4] Tous les tours d'un tournoi",
            "[5] Tous les matchs d'un tournoi", "[r] Retour"
        ]
        self.display_sorted_menu_title = self.title_string(
            "Tri de la selection")
        self.display_sorted_menu_items = ["[1] Par ordre alphabetique",
                                          "[2] Par classement", "[r] Retour"]
        self.main_menu = TerminalMenu(
            menu_entries=self.main_nemu_items,
            title=self.main_menu_title,
            shortcut_key_highlight_style=self.skhs,
            cycle_cursor=True,
            clear_screen=True
        )
        self.display_menu = TerminalMenu(
            menu_entries=self.display_menu_items,
            title=self.display_menu_title,
            shortcut_key_highlight_style=self.skhs,
            cycle_cursor=True,
            clear_screen=True
        )
        self.display_sorted_menu = TerminalMenu(
            menu_entries=self.display_sorted_menu_items,
            title=self.display_sorted_menu_title,
            shortcut_key_highlight_style=self.skhs,
            cycle_cursor=True,
            clear_screen=True
        )
        self.style = style_from_dict({
            Token.QuestionMark: '#E91E63 bold',
            Token.Selected: '#673AB7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#2196f3 bold',
            Token.Question: '',
        })
        self.logger = Logger()

    def start(self):
        # pylint: disable=invalid-name
        c = Controller(TournamentCarrier(), PlayerCarrier(), self)
        # TODO maybe put these somewhere else
        db_players = c.get_all_players()
        db_tournaments = c.get_all_tournaments()


        # pylint: disable=too-many-nested-blocks
        while not self.main_menu_exit:
            main_sel = self.main_menu.show()
            if main_sel == 0:
                print(self.title_string(
                    "Organisation de tournoi (Ctrl + C pour annuler)"))
                self.tournament_form[0]['validate'] = (
                    lambda name: "Ce nom de "
                    "tournoi existe deja dans la bdd, choisissez en un autre."
                    if next(
                        (d for d in db_tournaments if d["name"] == name),
                        None) else True
                )
                for v in db_players:
                    self.tournament_form[3]['choices'].append(
                        {'name': "{} {}".format(
                            v['first_name'], v['last_name'])
                         }
                    )
                answers = prompt(self.tournament_form, style=self.style)
                players = []
                rounds = []
                if 'players' in answers and answers['players']:
                    for p in answers['players']:
                        player = c.get_item(p, 'player')
                        players.append(Player(player['last_name'],
                                              player['first_name'],
                                              player['birth_date'],
                                              player['gender'],
                                              player['ranking']))
                    for i in range(int(answers['round_count'])):
                        rounds.append(Round("Round{}".format(i),
                                            answers['date'],
                                            "TBD",
                                            [{}]))
                    if answers['done']:
                        c.insert_tournament(answers['name'],
                                            answers['place'],
                                            answers['date'],
                                            rounds,
                                            players,
                                            TimeControl(answers['time_control'].capitalize()),
                                            answers['description'])
                        printd("\nSauvegarde du nouveau tournoi")
                    else:
                        db_players = []
                elif 'players' in answers and not answers['players']:
                    db_players = []
                    printd("\n Vous n'avez pas ajoute de joueur au tournoi, annulation")
                else:
                    db_players = []
            elif main_sel == 1:
                print(self.title_string(
                    "Ajout de joueur (Ctrl + C pour annuler)"))
                answers = prompt(CYSMenu.PLAYER_FORM, style=self.style)
                if answers and answers['done']:
                    c.insert_player(answers['last_name'],
                                    answers['first_name'],
                                    answers['gender'],
                                    answers['rank'])
                    printd("\nSauvegarde du nouveau joueur")
            elif main_sel == 2:
                print(self.title_string(
                    "Choix du joueur et modification de son "
                    "classement (Ctrl + C pour annuler)"))
                for v in db_players:
                    self.player_pick[0]['choices'].append(
                        {'name': "{} {}".format(
                            v['first_name'], v['last_name'])
                         }
                    )
                player = prompt(self.player_pick, style=self.style)
                if player:
                    c.update_player_rank(c.get_item(player['name'], 'player'),
                                         player['new_rank'])
                    printd("\nModification du classement")
            elif main_sel == 3:
                print(self.title_string(
                    "Choix du tournoi (Ctrl + C pour annuler)"))
                tournament = prompt(CYSMenu.TOURNAMENT_PICK, style=self.style)
                # generation des paires
                printd("Generation des paires")
                # affichage des joueurs/paires du round actuet
                # et update en permanence en dessous du titre de l'app
                # formulaire de resultats liste des paires restantes
                # results = prompt(round_results_form, style=style)
                print(self.title_string("Lancement de tournoi"))
                sleep(5)
            elif main_sel == 4:
                while not self.display_menu_back:
                    display_sel = self.display_menu.show()
                    if display_sel == 0:
                        while not self.display_sorted_menu_back:
                            display_sorted_sel = self.display_sorted_menu.show()
                            db_players_objs = []
                            for plyr in db_players:
                                db_players_objs.append(
                                    Player(plyr['last_name'],
                                           plyr['first_name'],
                                           plyr['birth_date'],
                                           plyr['gender'],
                                           plyr['rank'])
                                )
                            if display_sorted_sel == 0:
                                alpha_p = sorted(
                                    db_players_objs,
                                    key=lambda x: x.last_name.upper()
                                )
                                pydoc.pager("\n".join(map(str, alpha_p)))
                            elif display_sorted_sel == 1:
                                rank_p = sorted(
                                    db_players_objs, key=lambda x: x.rank
                                )
                                pydoc.pager("\n".join(map(str, rank_p)))
                            elif display_sorted_sel == 2:
                                self.display_sorted_menu_back = True
                        self.display_sorted_menu_back = False
                    elif display_sel == 1:
                        db_tournaments_objs = []
                        for trnmt in db_tournaments:
                            db_tournaments_objs.append(
                                Tournament(trnmt['name'], trnmt['place'],
                                           trnmt['date'], trnmt['rounds'],
                                           trnmt['players'],
                                           trnmt['time_control'],
                                           trnmt['description'],
                                           trnmt['round_count'])
                            )
                        pydoc.pager("\n".join(map(str, db_tournaments_objs)))
                    elif display_sel == 2:
                        print(self.title_string(
                            "Choix du tournoi (Ctrl + C pour annuler)"))
                        tournament = prompt(CYSMenu.TOURNAMENT_PICK,
                                            style=self.style)
                        while not self.display_sorted_menu_back:
                            display_sorted_sel = self.display_sorted_menu.show()
                            if display_sorted_sel == 0:
                                by_alpha = True
                                print(self.title_string(
                                    "Liste des joueurs du tournoi"
                                    " {} par ordre alphabetique"
                                    .format(tournament['tournament'])))
                                sleep(5)
                            elif display_sorted_sel == 1:
                                by_rank = True
                                print(self.title_string(
                                    "Liste des joueurs du tournoi"
                                    " {} par classement"
                                    .format(tournament['tournament'])))
                                sleep(5)
                            elif display_sorted_sel == 2:
                                self.display_sorted_menu_back = True
                        self.display_sorted_menu_back = False
                    elif display_sel == 3:
                        print(self.title_string(
                            "Choix du tournoi (Ctrl + C pour annuler)"))
                        tournament = prompt(CYSMenu.TOURNAMENT_PICK,
                                            style=self.style)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(self.title_string("Liste des tours du tournoi"
                                      " {}"
                                      .format(tournament['tournament'])))
                        sleep(5)
                    elif display_sel == 4:
                        print(self.title_string(
                            "Choix du tournoi (Ctrl + C pour annuler)"))
                        tournament = prompt(CYSMenu.TOURNAMENT_PICK,
                                            style=self.style)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(self.title_string("Liste des matchs du tournoi"
                                      " {}".format(tournament['tournament'])))
                        sleep(5)
                    elif display_sel == 5:
                        self.display_menu_back = True
                self.display_menu_back = False
            elif main_sel == 5:
                printd("Sauvegarde")
            elif main_sel == 6:
                printd("Chargement")
            elif main_sel == 7:
                self.main_menu_exit = True
