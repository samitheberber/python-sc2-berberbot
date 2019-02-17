#TODO: use necessary stuff and reference: https://github.com/Hannessa/python-sc2-ladderbot
import json

from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

from bot import MyBot

def run_ladder_game(bot):
    return None, None

def main():
    with open("botinfo.json") as f:
        info = json.load(f)

    race = Race[info["race"]]
    bot = Bot(race, MyBot())

    # Ladder game started by LadderManager
    print("Starting ladder game...")
    result, opponentid = run_ladder_game(bot)
    print(result," against opponent ", opponentid)

if __name__ == '__main__':
    main()
