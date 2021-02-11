# tournament.py
# Created at: Wed Jan 20 2021 17:09:34 GMT+0100 (GMT+01:00)
# Copyright 2021 MDCarrasco <michaeldanielcarrasco@gmail.com>
#

"""
tournament.py

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

# Owned
# pylint: disable=import-error
from models.round import Round
from models.match import Match

__author__ = "Michael Carrasco"
__copyright__ = "2021 MDCarrasco <michaeldanielcarrasco@gmail.com>"
__credits__ = ["Michael Carrasco"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Michael Carrasco"
__email__ = "<michaeldanielcarrasco@gmail.com>"
__status__ = "Dev"


class Tournament:
    """Tournament.
    """

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    # pylint: disable=dangerous-default-value
    def __init__(self, name, place, date, players, time_control,
                 description, rounds=[], round_count=4):
        """Summary of __init__.

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
        self.name = name
        self.place = place
        self.date = date
        self.round_count = round_count
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description

    def __str__(self) -> str:
        """Summary of __str__.

        Returns:
            str: Description of return value
        """
        return ('\nTournoi: {}\nLieu: {}\nDate: {}\nNombre de tours: {}\n'
                'Vitesse: {}\nDescription: {}\n'.format(self.name, self.place,
                                                        self.date,
                                                        self.round_count,
                                                        self.time_control,
                                                        self.description))

    def start(self, date_time):
        """Summary of start.

        Args:
            date_time

        Returns:
            list: Description of return value
        """
        rank_p = sorted(self.players, key=lambda x: x.rank)
        length = len(rank_p)
        middle_index = length//2
        first_half = rank_p[:middle_index]
        second_half = rank_p[middle_index:]
        matches = []
        for i in range(middle_index):
            matches.append(Match(first_half[i].first_name +
                                 ' ' +
                                 first_half[i].last_name,
                                 0,
                                 second_half[i].first_name +
                                 ' ' +
                                 second_half[i].last_name,
                                 0))
            first_half_play = next((x for x in self.players if x.first_name +
                                    ' ' +
                                    x.last_name == first_half[i].first_name +
                                    ' ' +
                                    first_half[i].last_name), None)

            second_half_play = next((x for x in self.players if x.first_name +
                                     ' ' +
                                     x.last_name == second_half[i].first_name +
                                     ' ' +
                                     second_half[i].last_name), None)
            first_half_play.opponents.append(second_half_play.first_name +
                                              ' ' +
                                              second_half_play.last_name)
            second_half_play.opponents.append(first_half_play.first_name +
                                               ' ' +
                                               first_half_play.last_name)
        if length > middle_index*2:
            matches.append(Match("Pas d'adversaire", 0,
                                 second_half[middle_index].first_name +
                                 ' ' +
                                 second_half[middle_index].last_name, 0))
            second_half_play = next((x for x in self.players if x.first_name +
                                     ' ' +
                                     x.last_name == second_half[middle_index].first_name +
                                     ' ' +
                                     second_half[middle_index].last_name), None)
            second_half_play.opponents.append("Pas d'adversaire")
        for i in range(self.round_count):
            if i == 0:
                self.rounds.append(Round("Round {}".format(i + 1),
                                         date_time, "", matches))
            else:
                matches = []
                self.rounds.append(Round("Round {}".format(i + 1),
                                         "", "", matches))

    def proceed(self, winners, tied, idx):
        """Summary of proceed.

        Args:
            winners
            tied
            matches
            idx
        """
        matches = []
        for p in self.players:
            p.match_score = 0
        points_or_rank_p = sorted(self.players,
                                  key=lambda x: (-x.current_score, x.rank))
        for winner in winners:
            play = next((x for x in points_or_rank_p if x.first_name +
                        ' ' + x.last_name == winner), None)
            if play:
                play.match_score = 1
                for m in self.rounds[idx].matches:
                    if m.tuple[0][0] == play.first_name + ' ' + play.last_name:
                        m.tuple[0][1] = play.match_score
                    elif m.tuple[1][0] == play.first_name + ' ' + play.last_name:
                        m.tuple[1][1] = play.match_score
                play.current_score += play.match_score
        if tied:
            for tie in tied:
                play = next((x for x in points_or_rank_p if x.first_name +
                            ' ' +
                            x.last_name == tie), None)
                if play:
                    play.match_score = 0.5
                    for m in self.rounds[idx].matches:
                        if m.tuple[0][0] == play.first_name + ' ' + play.last_name:
                            m.tuple[0][1] = play.match_score
                        elif m.tuple[1][0] == play.first_name + ' ' + play.last_name:
                            m.tuple[1][1] = play.match_score
                    play.current_score += play.match_score
        if idx != self.round_count - 1:
            i = 0
            while i < len(points_or_rank_p):
                offset = 2
                if len(points_or_rank_p[i].opponents) == len(points_or_rank_p):
                    points_or_rank_p[i].opponents = []
                try:
                    while offset < (len(points_or_rank_p)):
                        n = points_or_rank_p[i + 1].first_name+ ' ' +points_or_rank_p[i + 1].last_name
                        if n in points_or_rank_p[i].opponents:
                            points_or_rank_p[i + 1], points_or_rank_p[i + offset] = points_or_rank_p[i + offset], points_or_rank_p[i + 1]
                        offset += 1
                    matches.append(Match(points_or_rank_p[i].first_name + ' ' +
                                    points_or_rank_p[i].last_name, 0,
                                    points_or_rank_p[i + 1].first_name + ' ' +
                                    points_or_rank_p[i + 1].last_name, 0))
                    first_in_pair_play = next(
                        (x for x in self.players if x.first_name +
                         ' ' +
                         x.last_name == points_or_rank_p[i].first_name +
                         ' ' +
                         points_or_rank_p[i].last_name),
                        None
                    )

                    second_in_pair_play = next(
                        (x for x in self.players if x.first_name +
                         ' ' +
                         x.last_name == points_or_rank_p[i + 1].first_name +
                         ' ' +
                         points_or_rank_p[i + 1].last_name),
                        None
                    )
                    first_in_pair_play.opponents.append(
                        second_in_pair_play.first_name +
                        ' ' +
                        second_in_pair_play.last_name)
                    second_in_pair_play.opponents.append(
                        first_in_pair_play.first_name +
                        ' ' +
                        first_in_pair_play.last_name)
                    i += 2
                # pylint: disable=bare-except
                except IndexError:
                    matches.append(Match("Pas d'adversaire", 0,
                                         points_or_rank_p[i].first_name + ' ' +
                                         points_or_rank_p[i].last_name, 0))
                    second_in_pair_play = next((x for x in self.players if x.first_name +
                                                ' ' +
                                                x.last_name == points_or_rank_p[i].first_name +
                                                ' ' +
                                                points_or_rank_p[i].last_name), None)
                    second_in_pair_play.opponents.append("Pas d'adversaire")
                    i += 2
            self.rounds[idx + 1].matches = matches
