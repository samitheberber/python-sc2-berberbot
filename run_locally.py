# Based on https://gitlab.com/overmind-challenge/overmind-challenge-template/blob/master/run_locally.py
import json

from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

from bot import MyBot

import random

def main():
    with open("botinfo.json") as f:
        info = json.load(f)

    race = Race[info["race"]]

    opponents = [
        Computer(Race.Random, Difficulty.Hard)
    ]

    map_pool = [
        "(2)dreamcatcherle",
        "(2)RedshiftLE",
        "(2)LostandFoundLE"
    ]

    run_game(maps.get(random.choice(map_pool)), [
        Bot(race, MyBot()),
        random.choice(opponents)
    ], realtime=False, step_time_limit=2.0, game_time_limit=(60*20), save_replay_as="test.SC2Replay")

if __name__ == '__main__':
    main()
