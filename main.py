"""needs MVC imports"""
from controller import Controller
from model import TournamentCarrier
from model import PlayerCarrier
from view import View
import tinydb_backend

if __name__ == '__main__':

    # TODO 08/01/21
    # Create instances of tournament and player
    # test all functions with this main
    # check for bugs (there will be for sure)

    my_tournament = [
        {


        }
    ]

    my_players = [
        some players here
    ]

    c = Controller(TournamentCarrier(my_tournament),
                   PlayerCarrier(my_players) View())
    c.show_items()
    c.show_items(bullet_points=True)
    c.show_item('chocolate')
    c.show_item('bread')

    c.insert_item('bread', price=1.0, quantity=5)
    c.insert_item('chocolate', price=2.0, quantity=10)
    c.show_item('chocolate')

    c.update_item('milk', price=1.2, quantity=20)
    c.update_item('ice cream', price=3.5, quantity=20)

    c.show_items()

    # we close the current sqlite database connection explicitly
    if isinstance(c.models[0], TournamentCarrier):
        tinydb_backend.disconnect_from_db(c.model[0].connection)
        # the sqlite backend understands that it needs to open a new connection
        c.show_items()
        tinydb_backend.disconnect_from_db(c.model[0].connection)
    # we close the current sqlite database connection explicitly
    if isinstance(c.models[1], PlayerCarrier):
        tinydb_backend.disconnect_from_db(c.model[1].connection)
        # the sqlite backend understands that it needs to open a new connection
        c.show_items()
        tinydb_backend.disconnect_from_db(c.model[1].connection)
