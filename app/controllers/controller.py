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

# Futures

# Generic/Built-in

# Other Libs
from dateparser import parse

# Owned
from app.models.tournament import Tournament
from app.models.player import Player
from app.models.enums import TimeControl
from app.models.enums import Gender
import app.exceptions.mvc_exceptions as mvc_exc

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class Controller():
    """Controller.
    """

    def __init__(self, tournament_carrier, player_carrier, view):
        self.tournaments = tournament_carrier
        self.players = player_carrier
        self.view = view

    @staticmethod
    def is_date(string) -> bool:
        """Summary of is_date.
        Returns whether the string can be interpreted as a date.

        Args:
            string

        Returns:
            bool: is_date
        """
        try:
            parse(string)
            return True

        except ValueError:
            return False

    def show_all_items(self, models=None, bullet_points=False):
        """Summary of show_all_items.

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
                self.view.show_bullet_point_list(item_type, items)
            else:
                self.view.show_number_point_list(item_type, items)

    def show_all_tournaments(self, bullet_points=False):
        """Summary of show_all_tournaments.

        Args:
            bullet_points Default to False
        """
        models = [self.tournaments]
        self.show_all_items(models, bullet_points)

    def show_all_players(self, bullet_points=False):
        """Summary of show_all_players.

        Args:
            bullet_points Default to False
        """
        models = [self.players]
        self.show_all_items(models, bullet_points)

    def show_item(self, its_name, its_type):
        """Summary of show_item.

        Args:
            its_name
            its_type
        """
        try:
            if its_type == self.players.item_type:
                item = self.players.read_item(its_name)
            else:
                item = self.tournaments.read_item(its_name)
            self.view.show_item(its_type, its_name, item)
        except mvc_exc.ItemNotStored as exc:
            self.view.display_missing_item_error(its_name, exc)

    # pylint: disable=too-many-arguments
    def insert_tournament(self, name, place, date, rounds, players,
                          time_control, description, round_count=4):
        """Summary of insert_tournament.

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
        assert self.is_date(date), 'date cannot be converted to a french date'
        assert round_count > 0, 'round_count must be greater than 0'
        assert rounds, 'rounds must not be empty'
        assert players, 'players must not be empty'
        assert isinstance(time_control, TimeControl), ('time_control must have'
                                                       ' value: '
                                                       '\'bullet\','
                                                       '\'blitz\' or \'rapid\'')
        assert isinstance(description, str), 'description must be a string'
        item_type = self.tournaments.item_type
        tournament = Tournament(name, place, date, rounds, players,
                                time_control, description, round_count)
        try:
            self.tournaments.create_item(tournament)
            self.view.display_item_stored(name, item_type)
        except mvc_exc.ItemAlreadyStored as exc:
            self.view.display_item_already_stored_error(name, item_type, exc)

    def insert_tournament_obj(self, obj):
        """Summary of insert_tournament_obj.

        Args:
            obj
        """
        self.insert_tournament(obj.name, obj.place, obj.date, obj.rounds,
                               obj.players, obj.time_control, obj.description,
                               obj.round_count)

    def insert_tournament_objs(self, objs):
        """Summary of insert_tournament_objs.

        Args:
            objs
        """
        for obj in objs:
            self.insert_tournament_obj(obj)

    def insert_player(self, last_name, first_name, birth_date, gender, ranking):
        """Summary of insert_player.

        Args:
            last_name
            first_name
            birth_date
            gender
            ranking
        """
        assert self.is_date(
            birth_date), 'birth date cannot be converted to a french date'
        assert isinstance(gender, Gender), ('gender must be a string of value: '
                                            '\'homme\', \'femme\' ou \'autre\'')
        assert ranking > 0, 'ranking must greater than 0'
        item_type = self.players.item_type
        player = Player(last_name, first_name, birth_date, gender, ranking)
        try:
            self.players.create_item(player)
            self.view.display_item_stored(first_name + ' ' +
                                          last_name, item_type)
        except mvc_exc.ItemAlreadyStored as exc:
            self.view.display_item_already_stored_error(first_name + ' ' +
                                                        last_name, item_type,
                                                        exc)

    def insert_player_obj(self, obj):
        """Summary of insert_player_obj.

        Args:
            obj
        """
        self.insert_player(obj.last_name, obj.first_name, obj.birth_date,
                           obj.gender, obj.ranking)

    def insert_player_objs(self, objs):
        """Summary of insert_player_objs.

        Args:
            objs
        """
        for obj in objs:
            self.insert_player_obj(obj)

    def update_tournament(self, name, place, date, rounds, players,
                          time_control, description, round_count=4):
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
        assert self.is_date(date), 'date cannot be converted to a french date'
        assert round_count > 0, 'round_count must be greater than 0'
        assert rounds, 'rounds must not be empty'
        assert players, 'players must not be empty'
        assert isinstance(time_control, TimeControl), ('time_control must have'
                                                       ' value: '
                                                       '\'bullet\','
                                                       '\'blitz\' or \'rapid\'')
        assert isinstance(description, str), 'description must be a string'
        item_type = self.tournaments.item_type
        tournament = Tournament(name, place, date, rounds, players,
                                time_control, description, round_count)
        try:
            older = self.tournaments.read_item(name)
            self.tournaments.update_item(tournament)
            self.view.display_tournament_updated(
                name, older['place'], older['date'], older['round_count'],
                older['rounds'], older['players'], older['time_control'],
                older['description'], place, date, round_count, rounds,
                players, time_control, description)
        except mvc_exc.ItemNotStored as exc:
            self.view.display_item_not_yet_stored_error(name, item_type, exc)
            # if the item is not yet stored and we performed an update,
            # we have 2 options : do nothing or call insert_item to add
            # it. self.insert_item(name, price, quantity)

    def update_tournament_obj(self, obj):
        """Summary of update_tournament_obj.

        Args:
            obj
        """
        self.update_tournament(obj.name, obj.place, obj.date, obj.rounds,
                               obj.players, obj.time_control, obj.description,
                               obj.round_count)

    def update_player(self, last_name, first_name, birth_date, gender, ranking):
        """Summary of update_player.

        Args:
            last_name
            first_name
            birth_date
            gender
            ranking
        """
        assert self.is_date(
            birth_date), 'birth date cannot be converted to a french date'
        assert isinstance(gender, Gender), ('gender must be a string of value: '
                                            '\'homme\', \'femme\' ou \'autre\'')
        assert ranking > 0, 'ranking must greater than 0'
        item_type = self.players.item_type
        player = Player(last_name, first_name, birth_date, gender, ranking)
        try:
            older = self.players.read_item(first_name + ' ' + last_name)
            self.players.update_item(player)
            self.view.display_player_updated(
                first_name + ' ' + last_name, older['birth_date'],
                older['gender'], older['ranking'], birth_date, gender, ranking)
        except mvc_exc.ItemNotStored as exc:
            self.view.display_item_not_yet_stored_error(first_name + ' ' +
                                                        last_name, item_type,
                                                        exc)
            # if the item is not yet stored and we performed an update,
            # we have 2 options : do nothing or call insert_item to add
            # it. self.insert_item(name, price, quantity)

    def update_player_obj(self, obj):
        """Summary of update_player_obj.

        Args:
            obj
        """
        self.update_player(obj.last_name, obj.first_name, obj.birth_date,
                           obj.gender, obj.ranking)

    def update_tournament_type(self, new_item_type):
        """Summary of update_tournament_type.

        Args:
            new_item_type
        """
        old_item_type = self.tournaments.item_type
        self.tournaments.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)

    def update_player_type(self, new_item_type):
        """Summary of update_player_type.

        Args:
            new_item_type
        """
        old_item_type = self.players.item_type
        self.players.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)
