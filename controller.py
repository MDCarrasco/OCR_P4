"""needs exceptions"""
from dateparser import parse
from model import Tournament
from model import Player
from model import TimeControl
from model import Gender
import mvc_exceptions as mvc_exc

class Controller():
    """contoller class"""

    def __init__(self, tournament_carrier, player_carrier, view):
        self.tournaments = tournament_carrier
        self.players = player_carrier
        self.view = view

    @staticmethod
    def is_date(string):
        """
        Return whether the string can be interpreted as a date.

        :param string: str, string to check for date
        :param fuzzy: bool, ignore unknown tokens in string if True
        """
        try:
            parse(string)
            return True

        except ValueError:
            return False

    def show_items(self, bullet_points=False):
        """shows all items"""
        models = [self.tournaments, self.players]
        for model in models:
            items = model.read_items()
            item_type = model.item_type
            if bullet_points:
                self.view.show_bullet_point_list(item_type, items)
            else:
                self.view.show_number_point_list(item_type, items)

    def show_item(self, its_name, its_type):
        """shows item"""
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
        """inserts tournament"""
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
        """inserts a tournament from a Tournament obj"""
        self.insert_tournament(obj.name, obj.place, obj.date, obj.rounds,
                               obj.players, obj.time_control, obj.description,
                               round_count=4)

    def insert_tournament_objs(self, objs):
        """inserts multiple tournaments from a list of Tournament objs"""
        for obj in objs:
            self.insert_tournament_obj(obj)

    def insert_player(self, first_name, last_name, birth_date, gender, ranking):
        """inserts player"""
        assert self.is_date(
            birth_date), 'birth date cannot be converted to a french date'
        assert isinstance(gender, Gender) and Gender.has_value(gender), (
            'gender must be a string of value: '
            '\'homme\', \'femme\' ou \'autre\'')
        assert ranking > 0, 'ranking must greater than 0'
        item_type = self.players.item_type
        try:
            self.players.create_item(first_name, last_name,
                                       birth_date, gender, ranking)
            self.view.display_item_stored(first_name + ' ' +
                                          last_name, item_type)
        except mvc_exc.ItemAlreadyStored as exc:
            self.view.display_item_already_stored_error(first_name + ' ' +
                                                        last_name, item_type,
                                                        exc)

    def insert_player_obj(self, obj):
        """inserts a tournament from a Tournament obj"""
        self.insert_player(obj.first_name, obj.last_name, obj.birth_date,
                           obj.gender, obj.ranking)

    def insert_player_objs(self, objs):
        """inserts multiple players from a list of player objs"""
        for obj in objs:
            self.insert_player_obj(obj)

    def update_tournament(self, name, place, date, round_count, rounds,
                          players, time_control, description):
        """updates item"""
        assert isinstance(place, str), 'place should be a string'
        assert self.is_date(date), 'date cannot be converted to a french date'
        assert round_count > 0, 'round_count must be greater than 0'
        assert rounds, 'rounds must not be empty'
        assert players, 'players must not be empty'
        assert isinstance(time_control, str) and TimeControl.has_value(
            time_control), ('time_control must be a string of value: '
                            '\'bullet\', \'blitz\' or \'rapid\'')
        assert isinstance(description, str), 'description must be a string'
        item_type = self.tournaments.item_type
        try:
            older = self.tournaments.read_item(name)
            self.tournaments.update_item(name, place, date, round_count, rounds,
                                       players, time_control, description)
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

    def update_player(self, first_name, last_name, birth_date, gender, ranking):
        """updates item"""
        assert self.is_date(
            birth_date), 'birth date cannot be converted to a french date'
        assert isinstance(gender, str) and Gender.has_value(gender), (
            'gender must be a string of value: '
            '\'homme\', \'femme\' ou \'autre\'')
        assert ranking > 0, 'ranking must greater than 0'
        item_type = self.players.item_type
        try:
            older = self.players.read_item(first_name + ' ' + last_name)
            self.players.update_item(first_name, last_name, birth_date,
                                       gender, ranking)
            self.view.display_player_updated(
                first_name + ' ' + last_name, older['first_name'],
                older['last_name'], older['birth_date'], older['gender'],
                older['ranking'], first_name, last_name, birth_date, gender,
                ranking)
        except mvc_exc.ItemNotStored as exc:
            self.view.display_item_not_yet_stored_error(first_name + ' ' +
                                                        last_name, item_type,
                                                        exc)
            # if the item is not yet stored and we performed an update,
            # we have 2 options : do nothing or call insert_item to add
            # it. self.insert_item(name, price, quantity)


    def update_tournament_type(self, new_item_type):
        """updates item type"""
        old_item_type = self.tournaments.item_type
        self.tournaments.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)

    def update_player_type(self, new_item_type):
        """updates item type"""
        old_item_type = self.players.item_type
        self.players.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)
