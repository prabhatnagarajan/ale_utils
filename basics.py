import gymnasium


GAMES = ['Adventure',
	'AirRaid',
	'Alien',
	'Amidar',
	'Assault',
	'Asterix',
	'Asteroids',
	'Atlantis',
	'Atlantis2',
	'Backgammon',
	'BankHeist',
	'BasicMath',
	'BattleZone',
	'BeamRider',
	'Berzerk',
	'Blackjack',
	'Bowling',
	'Boxing',
	'Breakout',
	'Carnival',
	'Casino',
	'Centipede',
	'ChopperCommand',
	'CrazyClimber',
	'Crossbow',
	'Darkchambers',
	'Defender',
	'DemonAttack',
	'DonkeyKong',
	'DoubleDunk',
	'Earthworld',
	'ElevatorAction',
	'Enduro',
	'Entombed',
	'FishingDerby',
	'FlagCapture',
	'Freeway',
	'Frogger',
	'Frostbite',
	'Galaxian',
	'Gopher',
	'Gravitar',
	'Hangman',
	'HauntedHouse',
	'Hero',
	'HumanCannonball',
	'IceHockey',
	'Jamesbond',
	'JourneyEscape',
	'Kaboom',
	'Kangaroo',
	'KeystoneKapers',
	'KingKong',
	'Klax',
	'Koolaid',
	'Krull',
	'KungFuMaster',
	'LaserGates',
	'LostLuggage',
	'MarioBros',
	'MiniatureGolf',
	'MontezumaRevenge',
	'MrDo',
	'MsPacman',
	'NameThisGame',
	'Othello',
	'Pacman',
	'Phoenix',
	'Pitfall',
	'Pitfall2',
	'Pong',
	'Pooyan',
	'PrivateEye',
	'Qbert',
	'Riverraid',
	'RoadRunner',
	'Robotank',
	'Seaquest',
	'SirLancelot',
	'Skiing',
	'Solaris',
	'SpaceInvaders',
	'SpaceWar',
	'StarGunner',
	'Superman',
	'Surround',
	'Tennis',
	'Tetris',
	'TicTacToe3D',
	'TimePilot',
	'Trondead',
	'Turmoil',
	'Tutankham',
	'UpNDown',
	'Venture',
	'VideoCheckers',
	'VideoChess',
	'VideoCube',
	'VideoPinball',
	'WizardOfWor',
	'WordZapper',
	'YarsRevenge',
	'Zaxxon',
	]

# Atari-57 taken from
ATARI_57 = [
	'Alien',
	'Amidar',
	'Assault',
	'Asterix',
	'Asteroids',
	'Atlantis',
	'BankHeist',
	'BattleZone',
	'BeamRider'
	'Berzerk',
	'Bowling',
	'Boxing',
	'Breakout',
	'Centipede',
	'ChopperCommand',
	'CrazyClimber',
	'Defender',
	'DemonAttack',
	'DoubleDunk',
	'Enduro',
	'FishingDerby',
	'Freeway',
	'Frostbite',
	'Gopher',
	'Gravitar',
	'Hero',
	'IceHockey',
	'Jamesbond',
	'Kangaroo',
	'Krull',
	'KungFuMaster',
	'MontezumaRevenge',
	'MsPacman',
	'NameThisGame',
	'Phoenix',
	'Pitfall',
	'Pong',
	'PrivateEye',
	'Qbert',
	'Riverraid',
	'RoadRunner',
	'Robotank',
	'Seaquest',
	'Skiing',
	'Solaris',
	'SpaceInvaders',
	'StarGunner',
	'Surround',
	'Tennis',
	'TimePilot',
	'Tutankham',
	'UpNDown',
	'Venture',
	'VideoPinball',
	'WizardOfWor',
	'YarsRevenge',
	'Zaxxon',
]


ATARI_5 = ['BattleZone', 'DoubleDunk', 'NameThisGame', 'Phoenix', 'Qbert']

ATARI_10 = ATARI_5 + ['Amidar', 'Bowling', 'Frostbite', 'KungFuMaster', 'Riverraid']


if __name__ == '__main__':
	env = gymnasium.make('ALE/Breakout-v5',
                         repeat_action_probability=0.0,
                         full_action_space=False, frameskip=1,
                         max_num_frames_per_episode=30 * 60 * 60)
	for game in GAMES:
		gym_string = 'ALE/' + game + '-v5'
		env = gymnasium.make(gym_string,
                         repeat_action_probability=0.0,
                         full_action_space=False, frameskip=1,
                         max_num_frames_per_episode=30 * 60 * 60)
		print(f"{gym_string}:{env.action_space.n}")
	print()
	print("ATARI-10")
	for game in ATARI_10:
		gym_string = 'ALE/' + game + '-v5'
		env = gymnasium.make(gym_string,
                         repeat_action_probability=0.0,
                         full_action_space=False, frameskip=1,
                         max_num_frames_per_episode=30 * 60 * 60)
		print(f"{gym_string}:{env.action_space.n}")

