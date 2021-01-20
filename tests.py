"""needs MVC imports"""
from app.controllers.controller import Controller
from app.models.enums import Gender
from app.models.enums import TimeControl
from app.models.tournament import Tournament
from app.models.player import Player
from app.models.round import Round
from app.models.carriers import TournamentCarrier
from app.models.carriers import PlayerCarrier
from app.views.view import View

if __name__ == '__main__':

    my_matches = [
        {}
    ]

    my_rounds = [
        Round("round1", "21/21/21", "21/21/21", my_matches),
        Round("round2", "21/21/21", "21/21/21", my_matches),
        Round("round3", "21/21/21", "21/21/21", my_matches),
        Round("round4", "21/21/21", "21/21/21", my_matches)
    ]

    my_player = Player("hey", "heythere", "23/12/1992", Gender.FEMALE, 129)

    my_updated_player = Player("hey", "heythere", "23/11/1800",
                               Gender.OTHER, 100)

    my_players = [
        Player("Carrasco", "Michael", "23/12/1992", Gender.MALE, 299),
        Player("Myers", "Michael", "25/05/1963", Gender.MALE, 23),
        Player("Weaver", "Susan", "08/08/1949", Gender.FEMALE, 53),
        Player("Tobia", "Jacob", "07/06/1991", Gender.OTHER, 156),
        Player("Kasparof", "Garry", "13/04/1963", Gender.MALE, 2),
        Player("Carlsen", "Magnus", "30/11/1990", Gender.MALE, 1),
        Player("Polgar", "Judit", "23/07/1976", Gender.FEMALE, 5),
        Player("Brunson", "Doyle", "10/08/1933", Gender.MALE, 198),
        Player("Vachier-Lagrave", "Maxime", "21/10/1990", Gender.MALE, 10),
        Player("Scharzenegger", "Arnold", "30/07/1947", Gender.MALE, 78)
    ]

    my_tournament = Tournament(
        "Le grand jeu",
        "5 avenue Victor Hugo",
        "23/12/2021",
        my_rounds,
        my_players,
        TimeControl.BLITZ,
        "C'est le plus gros tournoi d'echecs du monde !")

    my_updated_tournament = Tournament(
        "Le petit jeu",
        "mise a jour de l'adresse aaaaa",
        "mise a jour de la dateaaaaa ffdf",
        my_rounds,
        my_players,
        TimeControl.RAPID,
        "mise a jour de la descriptionsadfasd  fdf sf")

    my_tournaments = [
        Tournament(
            "Tournoi 1",
            "5 avenue Victor Hugo",
            "23/12/2021",
            my_rounds,
            my_players,
            TimeControl.BLITZ,
            "C'est le plus gros tournoi d'echecs du monde !"),
        Tournament(
            "Tournoi 2",
            "5 avenue Victor Hugo",
            "23/12/2021",
            my_rounds,
            my_players,
            TimeControl.BLITZ,
            "C'est le plus gros tournoi d'echecs du monde !"),
        Tournament(
            "Tournoi 3",
            "5 avenue Victor Hugo",
            "23/12/2021",
            my_rounds,
            my_players,
            TimeControl.BLITZ,
            "C'est le plus gros tournoi d'echecs du monde !")
    ]

    # CREATE
    c = Controller(TournamentCarrier(), PlayerCarrier(), View())

    # insert one tournament details version
    c.insert_tournament("Le petit jeu",
            "9 rue de la 1ere D.F.L",
            "24/12/2021",
            my_rounds,
            my_players,
            TimeControl.RAPID,
            "C'est le plus petit tournoi d'echecs du monde !")
    # insert one tournament Obj version
    c.insert_tournament_obj(my_tournament)
    # insert multiple tournaments
    c.insert_tournament_objs(my_tournaments)

    # insert one player details version
    c.insert_player("test", "bob", "23/12/1992", Gender.MALE, 500)
    # insert one player Obj version
    c.insert_player_obj(my_player)
    # insert multiple players
    c.insert_player_objs(my_players)

    # READ
    c.show_all_items()
    #c.show_all_players(bullet_points=True)
    #c.show_all_tournaments(bullet_points=True)
    #c.show_all_items(bullet_points=True)
    #c.show_item('Le grand jeu', 'tournament')
    #c.show_item('Michael Carrasco', 'player')

    # UPDATE
    # update tournament details version
    #c.update_tournament("Le petit jeu",
    #        "mise a jour de l'adresse",
    #        "mise a jour de la date",
    #        my_rounds,
    #        my_players,
    #        TimeControl.RAPID,
    #        "mise a jour de la description")
    # update tournament obj version
    #c.update_tournament_obj(my_updated_tournament)
    # update player details version
    #c.update_player("test", "bob", "23/11/1900", Gender.FEMALE, 39)
    # update player obj version
    #c.update_player_obj(my_updated_player)
    #c.show_item('Le petit jeu', 'tournament')

    #c.show_items()

    # we close the current sqlite database connection explicitly
    #if isinstance(c.models[0], TournamentCarrier):
        #tinydb_backend.disconnect_from_db(c.models[0].connection)
        # the sqlite backend understands that it needs to open a new connection
        #c.show_items()
        #tinydb_backend.disconnect_from_db(c.models[0].connection)
    # we close the current sqlite database connection explicitly
    #if isinstance(c.models[1], PlayerCarrier):
        #tinydb_backend.disconnect_from_db(c.models[1].connection)
        # the sqlite backend understands that it needs to open a new connection
        #c.show_items()
        #tinydb_backend.disconnect_from_db(c.models[1].connection)
