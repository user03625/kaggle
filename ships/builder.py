
from kaggle_environments.envs.kore_fleets.helpers import *

def agent(obs, config):
    board = Board(obs,config)
    me = board.current_player
    turn = board.step
    spawn_cost = board.configuration.spawn_cost
    kore_left = me.kore
    for shipyard in me.shipyards:
        if kore_left >= spawn_cost:
            shipyard.next_action = ShipyardAction.spawn_ships(1)
        elif shipyard.ship_count > 0:
            shipyard.next_action = ShipyardAction.launch_fleet_with_flight_plan(2,Direction.NORTH.to_char())
    return me.next_actions

