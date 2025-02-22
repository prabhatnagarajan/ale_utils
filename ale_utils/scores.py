from ale_utils import basics
import atari_data
from pdb import set_trace
import re

def convert_to_snake_case(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

# Taken from Table H.4 of https://arxiv.org/pdf/2003.13350 (Agent57 paper)
RND_SCORES_ATARI_57 = {
	'Alien': 227.80,
	'Amidar': 5.80,
	'Assault': 222.40,
	'Asterix': 210.00,
	'Asteroids': 719.10,
	'Atlantis': 12850.00,
	'BankHeist': 14.20,
	'BattleZone': 2360.00,
	'BeamRider': 363.90,
	'Berzerk': 123.70,
	'Bowling': 23.10,
	'Boxing': 0.10,
	'Breakout': 1.70,
	'Centipede': 2090.90,
	'ChopperCommand': 811.00,
	'CrazyClimber': 10780.50,
	'Defender': 2874.50,
	'DemonAttack': 152.10,
	'DoubleDunk': -18.60,
	'Enduro': 0.00,
	'FishingDerby': -91.70,
	'Freeway': 0.0,
	'Frostbite': 65.20,
	'Gopher': 257.60,
	'Gravitar': 173.00,
	'Hero': 1027.00,
	'IceHockey': -11.20,
	'Jamesbond': 29.00,
	'Kangaroo': 52.00,
	'Krull': 1598.00,
	'KungFuMaster': 258.50,
	'MontezumaRevenge': 0.00,
	'MsPacman': 307.30,
	'NameThisGame': 2292.30,
	'Phoenix': 761.40,
	'Pitfall': -229.40,
	'Pong': -20.70,
	'PrivateEye': 24.90,
	'Qbert': 163.90,
	'Riverraid': 1338.50,
	'RoadRunner': 11.50,
	'Robotank': 2.20,
	'Seaquest': 68.40,
	'Skiing': -17098.10,
	'Solaris': 1236.30,
	'SpaceInvaders': 148.00,
	'StarGunner': 664.00,
	'Surround': -10.00,
	'Tennis': -23.80,
	'TimePilot': 3568.00,
	'Tutankham': 11.40,
	'UpNDown': 533.40,
	'Venture': 0.00,
	'VideoPinball': 0.00,
	'WizardOfWor': 563.50,
	'YarsRevenge': 3092.90,
	'Zaxxon': 32.50,
}

HUMAN_SCORES_ATARI_57 = {
	'Alien': 7127.70,
	'Amidar': 1719.50,
	'Assault': 742.00,
	'Asterix': 8503.30,
	'Asteroids': 47388.70,
	'Atlantis': 29028.10,
	'BankHeist': 753.10,
	'BattleZone': 37187.50,
	'BeamRider': 16926.50,
	'Berzerk': 2630.40,
	'Bowling': 160.70,
	'Boxing': 12.10,
	'Breakout': 30.50,
	'Centipede': 12017.00,
	'ChopperCommand': 7387.80,
	'CrazyClimber': 35829.40,
	'Defender': 18688.90,
	'DemonAttack': 1971.00,
	'DoubleDunk': -16.40,
	'Enduro': 860.50,
	'FishingDerby': -38.70,
	'Freeway': 29.60,
	'Frostbite': 4334.70,
	'Gopher': 2412.50,
	'Gravitar': 3351.40,
	'Hero': 30826.40,
	'IceHockey': 0.90,
	'Jamesbond': 302.80,
	'Kangaroo': 3035.00,
	'Krull': 2665.50,
	'KungFuMaster': 22736.30,
	'MontezumaRevenge': 4753.30,
	'MsPacman': 6951.60,
	'NameThisGame': 8049.00,
	'Phoenix': 7242.60,
	'Pitfall': 6463.70,
	'Pong': 14.60,
	'PrivateEye': 69571.30,
	'Qbert': 13455.00,
	'Riverraid': 17118.00,
	'RoadRunner': 7845.00,
	'Robotank': 11.90,
	'Seaquest': 42054.70,
	'Skiing': -4336.90,
	'Solaris': 12326.70,
	'SpaceInvaders': 1668.70,
	'StarGunner': 10250.00,
	'Surround': 6.50,
	'Tennis': -8.30,
	'TimePilot': 5229.20,
	'Tutankham': 167.60,
	'UpNDown': 11693.20,
	'Venture': 1187.50,
	'VideoPinball': 17667.90,
	'WizardOfWor': 4756.50,
	'YarsRevenge': 54576.90,
	'Zaxxon': 9173.30,
}

human_keys = HUMAN_SCORES_ATARI_57.keys()
rnd_keys = RND_SCORES_ATARI_57.keys()
assert human_keys == rnd_keys
human_keys_as_list = sorted([*human_keys])
rnd_keys_as_list = sorted([*rnd_keys])
assert human_keys_as_list == rnd_keys_as_list
assert human_keys_as_list == basics.ATARI_57

for game in HUMAN_SCORES_ATARI_57.keys():
	snake_case_game = convert_to_snake_case(game)
	rnd, human = atari_data._ATARI_DATA[snake_case_game]
	assert HUMAN_SCORES_ATARI_57[game] == human
	if game == 'VideoPinball':
		continue
	assert RND_SCORES_ATARI_57[game] == rnd, f"{RND_SCORES_ATARI_57[game]} vs {rnd}"

