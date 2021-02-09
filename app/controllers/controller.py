# app/controllers/controller.py
# Created at: Tue Jan 19 2021 19:00:30 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
app/controllers/controller.py

Example:
        INSERT example

Todo:
        * INSERT TODO lines
        *

.. _Google Python Style Guide (reference):
http://google.github.io/styleguide/pyguide.html
"""

# pylint: disable=import-error
# pylint: disable=no-name-in-module
# Futures

# Generic/Built-in
import json
import os
import itertools
from typing import Union
from datetime import datetime
from time import sleep

# Other Libs
from simple_term_menu import TerminalMenu

# Owned
from models.tournament import Tournament
from models.match import Match
from models.round import Round
from models.player import Player
from models.enums import TimeControl
from models.enums import Gender
from models.carriers import TournamentCarrier, PlayerCarrier
from views.sub_m_titles import SubMTitles
from views.logger import Logger
from views.validators import is_date
import exceptions.mvc_exceptions as mvc_exc

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"

def list_db_files(directory="./databases/") -> list:
    """Summary of list_db_files.

    Args:
        directory Default to "./databases/"

    Returns:
        list: Description of return value
    """
    return list((file for file in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, file))))

def database_is_not_empty(filename) -> bool:
    """Summary of database_is_not_empty.

    Args:
        filename

    Returns:
        bool: Description of return value
    """
    return os.path.getsize("./database/{}".format(filename)) > 0


# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes
class Controller():
    """Controller.
    """

    def __init__(self, tournament_carrier, player_carrier, menu_view, logger):
        self.tournaments = tournament_carrier
        self.players = player_carrier
        self.menu_view = menu_view
        self.logger = logger
        self.db_files = list_db_files()

    def get_item(self, its_name, its_type):
        """Summary of log_item.

        Args:
            its_name
            its_type
        """
        try:
            if its_type == self.players.item_type:
                return self.players.read_item(its_name)
            return self.tournaments.read_item(its_name)
        except mvc_exc.ItemNotStored as exc:
            self.logger.log_missing_item_error(its_name, exc)

    # pylint: disable=unsubscriptable-object
    def get_obj(self, its_name, its_type) -> Union[Player, Tournament]:
        """Summary of get_obj.

        Args:
            its_name
            its_type

        Returns:
            Union[Player, Tournament]: Description of return value
        """
        item = self.get_item(its_name, its_type)
        if its_type == self.players.item_type:
            return Player(item['last_name'],
                          item['first_name'],
                          item['birth_date'],
                          Gender(item['gender']),
                          int(item['rank']))
        tournament_rounds_objs = []
        for rnd in item['rounds']:
            if isinstance(rnd, str):
                rnd = json.loads(rnd)
            tournament_round_matches_objs = []
            for mat in rnd['matches']:
                tournament_round_matches_objs.append(
                    Match(mat['pone_name'],
                          mat['pone_score'],
                          mat['ptwo_name'],
                          mat['ptwo_score']))
            tournament_rounds_objs.append(Round(rnd['name'],
                                                rnd['start_date_time'],
                                                rnd['end_date_time'],
                                                tournament_round_matches_objs))
        tournament_player_objs = []
        for play in item['players']:
            if isinstance(play, str):
                play = json.loads(play)
            tournament_player_objs.append(Player(play['last_name'],
                                                 play['first_name'],
                                                 play['birth_date'],
                                                 play['gender'],
                                                 play['rank']))
        return Tournament(item['name'], item['place'], item['date'],
                          tournament_player_objs, item['time_control'],
                          item['description'], tournament_rounds_objs,
                          item['round_count'])

    def log_item(self, its_name, its_type):
        """Summary of log_item.

        Args:
            its_name
            its_type
        """
        try:
            if its_type == self.players.item_type:
                item = self.players.read_item(its_name)
            else:
                item = self.tournaments.read_item(its_name)
            self.logger.log_item(its_type, its_name, item)
        except mvc_exc.ItemNotStored as exc:
            self.logger.log_missing_item_error(its_name, exc)

    def log_all_items(self, models=None, bullet_points=False):
        """Summary of log_all_items.

        Args:
            models Default to None
            bullet_points Default to False
        """
        if not models:
            models = [self.tournaments, self.players]
        for model in models:
            items = model.read_items()
            item_type = model.item_type
            if bullet_points:
                self.logger.log_bullet_point_list(item_type, items)
            else:
                self.logger.log_number_point_list(item_type, items)

    def get_all_tournaments(self) -> list:
        """Summary of get_all_tournaments.

        Returns:
            list: Description of return value
        """
        return self.tournaments.read_items()

    def get_all_tournaments_objs(self) -> list:
        """Summary of get_all_tournaments_objs.

        Returns:
            list: Description of return value
        """
        items = self.get_all_tournaments()
        objs = []
        for item in items:
            objs.append(
                Tournament(item['name'], item['place'], item['date'],
                           item['players'], item['time_control'],
                           item['description'], item['rounds'],
                           item['round_count'])
            )
        return objs


    def log_all_tournaments(self, bullet_points=False):
        """Summary of log_all_tournaments.

        Args:
            bullet_points Default to False
        """
        models = [self.tournaments]
        self.log_all_items(models, bullet_points)

    def get_player_by_rank(self, rank) -> str:
        """Summary of get_player_by_rank.

        Args:
            rank

        Returns:
            str: Description of return value
        """
        try:
            return self.players.read_item_by_rank(rank)
        except mvc_exc.ItemNotStored as exc:
            self.logger.log_missing_item_error(rank, exc)

    def get_all_players(self) -> list:
        """Summary of get_all_players.

        Returns:
            list: Description of return value
        """
        return self.players.read_items()

    def get_all_players_objs(self) -> list:
        """Summary of get_all_players_objs.

        Returns:
            list: Description of return value
        """
        items = self.get_all_players()
        objs = []
        for item in items:
            objs.append(Player(item['last_name'],
                          item['first_name'],
                          item['birth_date'],
                          item['gender'],
                          item['rank']))
        return objs

    def log_all_players(self, bullet_points=False):
        """Summary of log_all_players.

        Args:
            bullet_points Default to False
        """
        models = [self.players]
        self.log_all_items(models, bullet_points)

    # pylint: disable=too-many-arguments
    def insert_tournament(self, name, place, date, players, time_control,
                          description, rounds=None, round_count=4):
        """Summary of insert_tournament.

        Args:
            name
            place
            date
            players
            time_control
            description
            round_count Default to 4
        """
        assert isinstance(place, str), 'place should be a string'
        assert is_date(date), 'date cannot be converted to a french date'
        assert round_count > 0, 'round_count must be greater than 0'
        assert any(players), 'players must not be empty'
        assert TimeControl.has_value(time_control), ('time_control must have'
                                                     ' value: '
                                                     '\'Bullet\','
                                                     '\'Blitz\' or \'Rapid\'')
        assert isinstance(description, str), 'description must be a string'
        item_type = self.tournaments.item_type
        int_round_count = int(round_count)
        if not rounds:
            rounds = []
        time_control_obj = TimeControl(time_control)
        tournament = Tournament(name, place, date, players, time_control_obj,
                                description, rounds, int_round_count)
        try:
            self.tournaments.create_item(tournament)
            self.logger.log_item_stored(name, item_type)
        except mvc_exc.ItemAlreadyStored as exc:
            self.logger.log_item_already_stored_error(name, item_type, exc)

    def insert_tournament_obj(self, obj):
        """Summary of insert_tournament_obj.

        Args:
            obj
        """
        self.insert_tournament(obj.name, obj.place, obj.date, obj.players,
                               obj.time_control, obj.description, obj.rounds,
                               obj.round_count)

    def insert_tournament_objs(self, objs):
        """Summary of insert_tournament_objs.

        Args:
            objs
        """
        for obj in objs:
            self.insert_tournament_obj(obj)

    def insert_player(self, last_name, first_name, birth_date, gender, rank):
        """Summary of insert_player.

        Args:
            last_name
            first_name
            birth_date
            gender
            rank
        """
        assert is_date(
            birth_date), 'birth date cannot be converted to a french date'
        assert Gender.has_value(gender), ('gender must be a string of value: '
                                          '\'Homme\', \'Femme\' ou \'Autre\'')
        assert rank > 0, 'rank must greater than 0'
        item_type = self.players.item_type
        player = Player(last_name, first_name, birth_date, Gender(gender), rank)
        try:
            self.players.create_item(player)
            self.logger.log_item_stored(first_name + ' ' +
                                          last_name, item_type)
        except mvc_exc.ItemAlreadyStored as exc:
            self.logger.log_item_already_stored_error(first_name + ' ' +
                                                        last_name, item_type,
                                                        exc)

    def insert_player_obj(self, obj):
        """Summary of insert_player_obj.

        Args:
            obj
        """
        self.insert_player(obj.last_name, obj.first_name, obj.birth_date,
                           obj.gender, obj.rank)

    def insert_player_objs(self, objs):
        """Summary of insert_player_objs.

        Args:
            objs
        """
        for obj in objs:
            self.insert_player_obj(obj)

    def update_tournament(self, name, place, date, players, time_control,
                          description, rounds, round_count=4):
        """Summary of update_tournament.

        Args:
            name
            place
            date
            rounds
            players
            time_control
            description
            round_count Default to 4
        """
        assert isinstance(place, str), 'place should be a string'
        assert is_date(date), 'date cannot be converted to a french date'
        assert round_count > 0, 'round_count must be greater than 0'
        assert rounds, 'rounds must not be empty'
        assert players, 'players must not be empty'
        assert TimeControl.has_value(time_control), ('time_control must have'
                                                       ' value: '
                                                       '\'Bullet\','
                                                       '\'Blitz\' or \'Rapid\'')
        assert isinstance(description, str), 'description must be a string'
        item_type = self.tournaments.item_type
        tournament = Tournament(name, place, date, players, time_control,
                                description, rounds, round_count)
        try:
            older = self.tournaments.read_item(name)
            self.tournaments.update_item(tournament)
            self.logger.log_tournament_updated(
                name, older['place'], older['date'], older['round_count'],
                older['rounds'], older['players'], older['time_control'],
                older['description'], place, date, round_count, rounds,
                players, time_control, description)
        except mvc_exc.ItemNotStored as exc:
            self.logger.log_item_not_yet_stored_error(name, item_type, exc)
            # if the item is not yet stored and we performed an update,
            # we have 2 options : do nothing or call insert_item to add
            # it.

    def update_tournament_obj(self, obj):
        """Summary of update_tournament_obj.

        Args:
            obj
        """
        self.update_tournament(obj.name, obj.place, obj.date, obj.players,
                               obj.time_control, obj.description,
                               obj.rounds, obj.round_count)

    def update_player(self, last_name, first_name, birth_date, gender, rank):
        """Summary of update_player.

        Args:
            last_name
            first_name
            birth_date
            gender
            rank
        """
        assert is_date(
            birth_date), 'birth date cannot be converted to a french date'
        assert isinstance(gender, Gender), ('gender must be a string of value: '
                                            '\'homme\', \'femme\' ou \'autre\'')
        assert rank > 0, 'rank must greater than 0'
        item_type = self.players.item_type
        player = Player(last_name, first_name, birth_date, gender, rank)
        try:
            older = self.players.read_item(first_name + ' ' + last_name)
            self.players.update_item(player)
            self.logger.log_player_updated(
                first_name + ' ' + last_name, older['birth_date'],
                older['gender'], older['rank'], birth_date, gender, rank)
        except mvc_exc.ItemNotStored as exc:
            self.logger.log_item_not_yet_stored_error(first_name + ' ' +
                                                           last_name, item_type,
                                                           exc)

    def update_player_obj(self, obj):
        """Summary of update_player_obj.

        Args:
            obj
        """
        self.update_player(obj.last_name, obj.first_name, obj.birth_date,
                           obj.gender, obj.rank)

    def update_player_rank_rec(self, dic, new_rank, up_or_down):
        """Summary of update_player_rank_rec.

        Args:
            dic
            new_rank
            up_or_down
        """
        dup_rank = self.get_player_by_rank(new_rank)
        if dup_rank:
            self.update_player_rank_rec(dup_rank, dup_rank['rank'] - up_or_down,
                                        up_or_down)
        self.update_player(dic['last_name'], dic['first_name'],
                           dic['birth_date'], Gender(dic['gender']), new_rank)

    def update_player_rank(self, dic, new_rank):
        """Summary of update_player_rank.

        Args:
            dic
            new_rank
        """
        up_or_down = 1 if dic['rank'] - new_rank < 0 else -1
        self.update_player_rank_rec(dic, new_rank, up_or_down)

    def update_tournament_type(self, new_item_type):
        """Summary of update_tournament_type.

        Args:
            new_item_type
        """
        old_item_type = self.tournaments.item_type
        self.tournaments.item_type = new_item_type
        self.logger.log_change_item_type(old_item_type, new_item_type)

    def update_player_type(self, new_item_type):
        """Summary of update_player_type.

        Args:
            new_item_type
        """
        old_item_type = self.players.item_type
        self.players.item_type = new_item_type
        self.logger.log_change_item_type(old_item_type, new_item_type)

    def render_view(self):
        """provide_view.
        """

    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    def start(self):
        """start.
        """
        # pylint: disable=invalid-name
        c = lambda: None
        view = self.menu_view
        db_files = self.db_files
        db_players = []
        db_tournaments = []

        # pylint: disable=too-many-nested-blocks
        while not view.main_menu_exit:
            if view.load_db_sel == -1 and db_files:
                main_sel = 6
            else:
                main_sel = view.main_menu.show()
            if main_sel == 0 and len(db_players) > 3:
                view.print_title_string(SubMTitles.CREATE_TOURNAMENT)
                view.tournament_form[0]['validate'] = (
                    lambda name: "Ce nom de "
                    "tournoi existe deja dans la bdd, choisissez en un autre."
                    if next(
                        (d for d in db_tournaments if d["name"] == name),
                        None) else ("Entrez un nom." if not name else True)
                )
                for v in db_players:
                    view.tournament_form[3]['choices'].append(
                        {'name': "{} {}".format(
                            v['first_name'], v['last_name'])
                         }
                    )
                answers = view.prompt_form(view.tournament_form)
                players = []
                if 'players' in answers and answers['players']:
                    for p in answers['players']:
                        player = c.get_obj(p, 'player')
                        players.append(player)
                    if answers['done']:
                        c.insert_tournament(answers['name'],
                                            answers['place'],
                                            answers['date'],
                                            players,
                                            answers['time_control'],
                                            answers['description'])
                        db_tournaments = c.get_all_tournaments()
                        view.printd("\nSauvegarde du nouveau tournoi")
                    else:
                        db_players = []
                elif 'players' in answers and not answers['players']:
                    db_players = []
                    view.printd("\n Vous n'avez pas ajoute de joueur au "
                                "tournoi, annulation")
                else:
                    db_players = []
            elif main_sel == 1 and isinstance(c, Controller):
                db_players = c.get_all_players()
                view.print_title_string(SubMTitles.ADD_PLAYER)
                view.player_form[4]['validate'] = (
                    lambda rank: "Entrez un nombre positif."
                    if not rank.isdigit() or int(rank) <= 0
                    else ("Il existe deja un joueur avec ce classement "
                    "dans la bdd."
                    if next((d for d in db_players if d["rank"] == int(rank)),
                            None) else True)
                )
                answers = view.prompt_form(view.player_form)
                if answers and answers['done']:
                    c.insert_player(answers['last_name'],
                                    answers['first_name'],
                                    answers['birth_date'],
                                    answers['gender'],
                                    answers['rank'])
                    db_players = []
                    view.printd("\nSauvegarde du nouveau joueur")
            elif main_sel == 2 and db_players:
                view.print_title_string(SubMTitles.UPDATE_RANK)
                for v in db_players:
                    view.player_pick[0]['choices'].append(
                        {'name': "{} {}".format(
                            v['first_name'], v['last_name'])
                         }
                    )
                player = view.prompt_form(view.player_pick)
                if player:
                    c.update_player_rank(c.get_item(player['name'], 'player'),
                                         player['new_rank'])
                    view.printd("\nModification du classement")
                view.player_pick[0]['choices'] = []
            elif main_sel == 3 and db_tournaments:
                view.print_title_string(SubMTitles.PICK_TOURNAMENT)
                view.tournament_pick[0]['choices'] = []
                db_tournaments = c.get_all_tournaments()
                for v in db_tournaments:
                    view.tournament_pick[0]['choices'].append(
                        {'name': "{}".format(v['name'])}
                    )
                choice = view.prompt_form(view.tournament_pick)
                # generation des paires
                if 'tournament' in choice and choice['tournament']:
                    view.clear()
                    view.print_title_string(SubMTitles.LAUNCH_TOURNAMENT)
                    c.start_tournament(choice['tournament'])
                    view.printd("Generation des paires pour le tournoi {}"
                                .format(choice['tournament']))
                    view.clear()
                    winners = []
                    tied = []
                    tournament = c.get_item(choice['tournament'], 'tournament')
                    # print(tournament['rounds'])
                    for i in range(1, tournament['round_count'] + 1):
                        tournament = c.get_item(choice['tournament'], 'tournament')
                        r = tournament['rounds'][i - 1]
                        for m in r['matches']:
                            if (m['pone_name'] != "Pas d'adversaire" and
                                    m['ptwo_name'] != "Pas d'adversaire"):
                                view.who_won[0]['choices'] =[m['pone_name'],
                                                             m['ptwo_name'],
                                                             'Aucun']
                                winner = view.prompt_form(view.who_won)
                                if 'fullname' in winner and winner['fullname'] == 'Aucun':
                                    tied.append(m['pone_name'])
                                    tied.append(m['ptwo_name'])
                                elif 'fullname' in winner and winner['fullname'] != 'Aucun':
                                    winners.append(winner['fullname'])
                            elif m['pone_name'] == "Pas d'adversaire":
                                winners.append(m['ptwo_name'])
                            else:
                                winners.append(m['pone_name'])
                        c.next_round(choice['tournament'], winners=winners,
                                     tied=tied, i=i)
                        winners = []
                        tied = []
                        view.who_won[0]['choices'] = []
                    c.end_tournament(choice['tournament'])
                    view.print_title_string(SubMTitles
                                            .TOURNAMENT_FOLLOW_UP
                                            .format(choice['tournament']))
                    # affichage des joueurs/paires du round actuet
                    # et update en permanence en dessous du titre de l'app
                    # formulaire de resultats liste des paires restantes
                    # results = prompt(round_results_form, style=style)
            elif main_sel == 4 and isinstance(c, Controller):
                while not view.display_menu_back:
                    display_sel = view.display_menu.show()
                    view.tournament_pick[0]['choices'] = []
                    db_players = c.get_all_players()
                    db_tournaments = c.get_all_tournaments()
                    if display_sel == 0 and db_players:
                        while not view.display_sorted_menu_back:
                            display_sorted_sel = (
                                view.display_sorted_menu.show()
                            )
                            db_players_objs = c.get_all_players_objs()
                            if display_sorted_sel == 0:
                                alpha_p = sorted(
                                    db_players_objs,
                                    key=lambda x: x.last_name.upper()
                                )
                                view.print_pydoc(alpha_p)
                            elif display_sorted_sel == 1:
                                rank_p = sorted(
                                    db_players_objs, key=lambda x: x.rank
                                )
                                view.print_pydoc(rank_p)
                            elif display_sorted_sel == 2:
                                view.display_sorted_menu_back = True
                        view.display_sorted_menu_back = False
                    elif display_sel == 1 and db_tournaments:
                        db_tournaments_objs = c.get_all_tournaments_objs()
                        view.print_pydoc(db_tournaments_objs)
                    elif display_sel == 2 and db_tournaments:
                        view.print_title_string(SubMTitles
                                                .PICK_TOURNAMENT)
                        for v in db_tournaments:
                            view.tournament_pick[0]['choices'].append(
                                {'name': "{}".format(v['name'])}
                            )
                        answer = view.prompt_form(view.tournament_pick)
                        if 'tournament' in answer and answer['tournament']:
                            tournament = c.get_obj(answer['tournament'],
                                                    'tournament')
                            while not view.display_sorted_menu_back:
                                display_sorted_sel = (
                                    view.display_sorted_menu.show()
                                )
                                if display_sorted_sel == 0:
                                    alpha_p = sorted(
                                        tournament.players,
                                        key=lambda x: x.last_name.upper()
                                    )
                                    view.print_pydoc(alpha_p)
                                elif display_sorted_sel == 1:
                                    rank_p = sorted(
                                        tournament.players,
                                        key=lambda x: x.rank
                                    )
                                    view.print_pydoc(rank_p)
                                elif display_sorted_sel == 2:
                                    view.display_sorted_menu_back = True
                            view.display_sorted_menu_back = False
                    elif display_sel == 3 and db_tournaments:
                        view.print_title_string(SubMTitles
                                                .PICK_TOURNAMENT)
                        for v in db_tournaments:
                            view.tournament_pick[0]['choices'].append(
                                {'name': "{}".format(v['name'])}
                            )
                        answer = view.prompt_form(view.tournament_pick)
                        if 'tournament' in answer and answer['tournament']:
                            tournament = c.get_obj(answer['tournament'],
                                                    'tournament')
                            view.print_pydoc(tournament.rounds)
                    elif display_sel == 4 and db_tournaments:
                        view.print_title_string(SubMTitles
                                                .PICK_TOURNAMENT)
                        for v in db_tournaments:
                            view.tournament_pick[0]['choices'].append(
                                {'name': "{}".format(v['name'])}
                            )
                        answer = view.prompt_form(view.tournament_pick)
                        if 'tournament' in answer and answer['tournament']:
                            tournament = c.get_obj(answer['tournament'],
                                                    'tournament')
                        view.clear()
                        tournament_matches =[]
                        for i, rnd in zip(range(1, len(tournament.rounds) + 1),
                                          tournament.rounds):
                            tournament_matches.append('-----Round {}-----'.format(i))
                            for match in rnd.matches:
                                tournament_matches.append(match)
                        view.print_pydoc(tournament_matches)
                    elif display_sel == 5:
                        view.display_menu_back = True
                view.display_menu_back = False
            elif main_sel == 5:
                view.print_title_string(SubMTitles.NEW_DB)
                choice = view.prompt_form(view.db_name_form)
                if 'db_name' in choice and choice['db_name']:
                    view.main_menu_title = view.title_string(
                        "Assistant pour tournois d'echecs ({})"
                        .format(choice['db_name'] + ".json"))
                    view.main_menu = TerminalMenu(
                        menu_entries=view.main_nemu_items,
                        title=view.main_menu_title,
                        shortcut_key_highlight_style=view.skhs,
                        cycle_cursor=True,
                        clear_screen=True
                    )
                    if isinstance(c, Controller):
                        c.disconnect()
                    db_players = []
                    db_tournaments = []
                    c = self.switch_db(choice['db_name'])
                    db_players = c.get_all_players()
                    db_tournaments = c.get_all_tournaments()
                    db_files = list_db_files()
                    view.printd("Sauvegarde")
            elif main_sel == 6:
                db_files = list_db_files()
                view.load_db_menu = TerminalMenu(
                    menu_entries=db_files,
                    title=view.title_string(SubMTitles.LOAD_DB),
                    shortcut_key_highlight_style=view.skhs,
                    cycle_cursor=True,
                    clear_screen=True
                )
                while not view.load_db_menu_back:
                    view.load_db_sel = view.load_db_menu.show()
                    if view.load_db_sel != -1 and view.load_db_sel is not None:
                        choice = db_files[view.load_db_sel]
                        # if database_is_not_empty(choice):
                            # coloredchoice = Bcolors.apply_green(choice)
                        # else:
                            # coloredchoice = Bcolors.apply_warning(choice)
                        view.main_menu_title = view.title_string(
                            "Assistant pour tournois d'echecs ({})"
                            .format(choice))
                        view.main_menu = TerminalMenu(
                            menu_entries=view.main_nemu_items,
                            title=view.main_menu_title,
                            shortcut_key_highlight_style=view.skhs,
                            cycle_cursor=True,
                            clear_screen=True
                        )
                        if isinstance(c, Controller):
                            c.disconnect()
                        db_players = []
                        db_tournaments = []
                        c = self.switch_db(choice.split('.')[0])
                        db_players = c.get_all_players()
                        db_tournaments = c.get_all_tournaments()
                        view.load_db_menu_back = True
                view.load_db_menu_back = False
            elif main_sel == 7:
                view.main_menu_exit = True

    def start_tournament(self, tournament_name):
        """Summary of start_tournament.

        Args:
            tournament_name
        """
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tournament = self.get_obj(tournament_name, 'tournament')
        tournament.start(now)
        self.update_tournament_obj(tournament)
        self.next_round(tournament_name)

    # pylint:disable=too-many-branches
    def next_round(self, tournament_name, winners=None, tied=None, i=0):
        """Summary of next_round.

        Args:
            tournament_name
            winners Default to None
            tied Default to None
            matches Default to None
            i Default to 0
        """
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tournament = self.get_obj(tournament_name, 'tournament')
        if i != 0:
            tournament.rounds[i - 1].end_date_time = now
        if i < tournament.round_count:
            tournament.rounds[i].start_date_time = now
        for p in tournament.players:
            print("name {}".format(p.first_name + " " + p.last_name))
            print("current_score: {}".format(p.current_score))
        if winners is not None and tied is not None:
            tournament.proceed(winners, tied, i - 1)
        self.update_tournament_obj(tournament)

    def end_tournament(self, tournament_name):
        """end_tournament.
        """
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        tournament = self.get_obj(tournament_name, 'tournament')
        tournament.rounds[tournament.round_count - 1].end_date_time = now
        self.update_tournament_obj(tournament)


    def disconnect(self):
        """disconnect.
        """
        if isinstance(self.tournaments, TournamentCarrier):
            self.tournaments.disconnect()
        if isinstance(self.players, PlayerCarrier):
            self.players.disconnect()

    def switch_db(self, db_name):
        """Summary of switch_db.

        Args:
            tournament_carrier
            player_carrier
            view
        """
        self.disconnect()
        return Controller(TournamentCarrier(db_name), PlayerCarrier(db_name),
                          self.menu_view, Logger(db_name))
