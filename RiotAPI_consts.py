
LEGAL = "\
{application_name} isn't endorsed by Riot Games and doesn't reflect the views or opinions of \
Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games \
are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc."

API_VERSION = {
    'champion': '1.2',
    'championmastery': '',
    'current-game': '1.0',
    'featured-games': '1.0',
    'game': '1.3',
    'league': '2.5',
    'lol-static-data': '1.2',
    'lol-status': '1.0',
    'match': '2.2',
    'matchlist': '2.2',
    'stats': '1.3',
    'summoner': '1.4',
    'team': '2.4'
}

API_URL = {
    'base': 'https://{proxy}.api.pvp.net/',

    'champion': 'api/lol/{region}/v{version}/champion',
    'championmastery': 'championmastery',
    'current-game': 'observer-mode/rest/consumer/getSpectatorGameInfo',
    'featured-games': 'observer-mode/rest/featured',
    'game': 'api/lol/{region}/v{version}/game',
    'league': 'api/lol/{region}/v{version}/league',
    'lol-status': 'shards',
    'match': 'api/lol/{region}/v{version}/match',
    'matchlist': 'api/lol/{region}/v{version}/matchlist',
    'stats': 'api/lol/{region}/v{version}/stats',
    'summoner': 'api/lol/{region}/v{version}/summoner',
    'team': 'api/lol/{region}/v{version}/team',

    'lol-static-data': 'api/lol/static-data/{region}/v{version}',
    'data-dragon': 'http://ddragon.leagueoflegends.com/cdn'
}

REQUEST_LIMITS = {
    'normal_10s': 10,
    'normal_10m': 500,
    'production_10s': 3000,
    'production_10m': 180000
}

PLATFORMS = {
    'br': 'BR1',
    'eune': 'EUN1',
    'euw': 'EUW1',
    'jp': 'JP1',
    'kr': 'KR',
    'lan': 'LA1',
    'las': 'LA2',
    'na': 'NA1',
    'oce': 'OC1',
    'tr': 'TR1',
    'ru': 'RU',
    'pbe': 'PBE1'
}

ERRORS = {
    400: 'Bad request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not found',
    415: 'Unsupported media type',
    429: 'API key rate limit exceeded',
    500: 'Internal server error',
    503: 'Service unavailable',
    504: 'Gateway timeout'
}

CLASSES = [
    'None',

    'Utility',
    'Healer',
    'Vanguard',
    'Warden',
    'Juggernaut',
    'Diver',
    'Burst Mage',
    'Battle Mage',
    'Artillery Mage',
    'Control Mage',
    'Assassin',
    'Skirmisher',
    'Marksman'
]

CHAMPIONS = {
    "Aatrox": {'classes': ['Diver'], 'id': 266},
    "Ahri": {'classes': ['Burst Mage', 'Assassin'], 'id': 103},
    "Akali": {'classes': ['Assassin'], 'id': 84},
    "Alistar": {'classes': ['Warden'], 'id': 12},
    "Amumu": {'classes': ['Vanguard', 'Battle Mage'], 'id': 32},
    "Anivia": {'classes': ['Control Mage'], 'id': 34},
    "Annie": {'classes': ['Burst Mage'], 'id': 1},
    "Ashe": {'classes': ['Marksman'], 'id': 22},
    "Aurelion Sol": {'classes': ['Battle Mage'], 'id': 136},
    "Azir": {'classes': ['Control Mage'], 'id': 268},
    "Bard": {'classes': ['Utility', 'Healer'], 'id': 432},
    "Blitzcrank": {'classes': ['Vanguard'], 'id': 53},
    "Brand": {'classes': ['Burst Mage'], 'id': 63},
    "Braum": {'classes': ['Warden'], 'id': 201},
    "Caitlyn": {'classes': ['Marksman'], 'id': 51},
    "Cassiopeia": {'classes': ['Battle Mage'], 'id': 69},
    "Cho'Gath": {'classes': ['Vanguard', 'Burst Mage'], 'id': 31},
    "Corki": {'classes': ['Marksman', 'Artillery Mage'], 'id': 42},
    "Darius": {'classes': ['Juggernaut'], 'id': 122},
    "Diana": {'classes': ['Assassin', 'Burst Mage'], 'id': 131},
    "Dr. Mundo": {'classes': ['Juggernaut'], 'id': 36},
    "Draven": {'classes': ['Marksman'], 'id': 119},
    "Ekko": {'classes': ['Diver'], 'id': 245},
    "Elise": {'classes': ['Diver'], 'id': 60},
    "Evelynn": {'classes': ['Diver'], 'id': 28},
    "Ezreal": {'classes': ['Marksman', 'Artillery Mage'], 'id': 81},
    "Fiddlesticks": {'classes': ['Burst Mage'], 'id': 9},
    "Fiora": {'classes': ['Skirmisher'], 'id': 114},
    "Fizz": {'classes': ['Assassin'], 'id': 105},
    "Galio": {'classes': ['Battle Mage'], 'id': 3},
    "Gangplank": {'classes': ['Skirmisher'], 'id': 41},
    "Garen": {'classes': ['Juggernaut'], 'id': 86},
    "Gnar": {'classes': ['Vanguard'], 'id': 150},
    "Gragas": {'classes': ['Vanguard'], 'id': 79},
    "Graves": {'classes': ['Marksman'], 'id': 104},
    "Hecarim": {'classes': ['Diver'], 'id': 120},
    "Heimerdinger": {'classes': ['Control Mage'], 'id': 74},
    "Illaoi": {'classes': ['Juggernaut'], 'id': 420},
    "Irelia": {'classes': ['Diver'], 'id': 39},
    "Janna": {'classes': ['Utility'], 'id': 40},
    "Jarvan IV": {'classes': ['Diver'], 'id': 59},
    "Jax": {'classes': ['Diver'], 'id': 24},
    "Jayce": {'classes': ['Skirmisher'], 'id': 126},
    "Jhin": {'classes': ['Marksman'], 'id': 202},
    "Jinx": {'classes': ['Marksman'], 'id': 222},
    "Kalista": {'classes': ['Marksman'], 'id': 429},
    "Karma": {'classes': ['Utility'], 'id': 43},
    "Karthus": {'classes': ['Battle Mage'], 'id': 30},
    "Kassadin": {'classes': ['Diver'], 'id': 38},
    "Katarina": {'classes': ['Assassin'], 'id': 55},
    "Kayle": {'classes': ['Battle Mage', 'Skirmisher'], 'id': 10},
    "Kennen": {'classes': ['Battle Mage'], 'id': 85},
    "Kha'Zix": {'classes': ['Assassin'], 'id': 121},
    "Kindred": {'classes': ['Marksman', 'Skirmisher'], 'id': 203},
    "Kog'Maw": {'classes': ['Marksman'], 'id': 96},
    "LeBlanc": {'classes': ['Assassin'], 'id': 7},
    "Lee Sin": {'classes': ['Diver'], 'id': 64},
    "Leona": {'classes': ['Vanguard'], 'id': 89},
    "Lissandra": {'classes': ['Battle Mage'], 'id': 127},
    "Lucian": {'classes': ['Marksman'], 'id': 236},
    "Lulu": {'classes': ['Utility', 'Battle Mage'], 'id': 117},
    "Lux": {'classes': ['Burst Mage', 'Artillery Mage'], 'id': 99},
    "Malphite": {'classes': ['Vanguard'], 'id': 54},
    "Malzahar": {'classes': ['Battle Mage'], 'id': 90},
    "Maokai": {'classes': ['Vanguard'], 'id': 57},
    "Master Yi": {'classes': ['Skirmisher'], 'id': 11},
    "Miss Fortune": {'classes': ['Marksman'], 'id': 21},
    "Mordekaiser": {'classes': ['Juggernaut'], 'id': 82},
    "Morgana": {'classes': ['Utility', 'Control Mage'], 'id': 25},
    "Nami": {'classes': ['Utility', 'Healer'], 'id': 267},
    "Nasus": {'classes': ['Juggernaut'], 'id': 75},
    "Nautilus": {'classes': ['Vanguard'], 'id': 111},
    "Nidalee": {'classes': ['Assassin', 'Artillery Mage'], 'id': 76},
    "Nocturne": {'classes': ['Diver', 'Skirmisher'], 'id': 56},
    "Nunu": {'classes': ['Utility', 'Warden'], 'id': 20},
    "Olaf": {'classes': ['Diver'], 'id': 2},
    "Orianna": {'classes': ['Control Mage'], 'id': 61},
    "Pantheon": {'classes': ['Diver'], 'id': 80},
    "Poppy": {'classes': ['Vanguard', 'Diver'], 'id': 78},
    "Quinn": {'classes': ['Marksman', 'Assassin'], 'id': 133},
    "Rammus": {'classes': ['Vanguard', 'Warden'], 'id': 33},
    "Rek'Sai": {'classes': ['Diver'], 'id': 421},
    "Renekton": {'classes': ['Diver'], 'id': 58},
    "Rengar": {'classes': ['Assassin'], 'id': 107},
    "Riven": {'classes': ['Diver'], 'id': 92},
    "Rumble": {'classes': ['Control Mage', 'Battle Mage'], 'id': 68},
    "Ryze": {'classes': ['Battle Mage'], 'id': 13},
    "Sejuani": {'classes': ['Vanguard'], 'id': 113},
    "Shaco": {'classes': ['Assassin'], 'id': 35},
    "Shen": {'classes': ['Warden', 'Vanguard'], 'id': 98},
    "Shyvana": {'classes': ['Diver', 'Skirmisher'], 'id': 102},
    "Singed": {'classes': ['Vanguard', 'Juggernaut'], 'id': 27},
    "Sion": {'classes': ['Vanguard'], 'id': 14},
    "Sivir": {'classes': ['Marksman'], 'id': 15},
    "Skarner": {'classes': ['Vanguard'], 'id': 72},
    "Sona": {'classes': ['Healer', 'Utility'], 'id': 37},
    "Soraka": {'classes': ['Healer'], 'id': 16},
    "Swain": {'classes': ['Battle Mage'], 'id': 50},
    "Syndra": {'classes': ['Battle Mage', 'Burst Mage'], 'id': 134},
    "Tahm Kench": {'classes': ['Warden', 'Vanguard'], 'id': 223},
    "Talon": {'classes': ['Assassin'], 'id': 91},
    "Taric": {'classes': ['Warden'], 'id': 44},
    "Teemo": {'classes': ['Control Mage', 'Marksman'], 'id': 17},
    "Thresh": {'classes': ['Warden', 'Vanguard'], 'id': 412},
    "Tristana": {'classes': ['Marksman'], 'id': 18},
    "Trundle": {'classes': ['Juggernaut'], 'id': 48},
    "Tryndamere": {'classes': ['Skirmisher'], 'id': 23},
    "Twisted Fate": {'classes': ['Assassin', 'Burst Mage'], 'id': 4},
    "Twitch": {'classes': ['Marksman', 'Assassin'], 'id': 29},
    "Udyr": {'classes': ['Diver'], 'id': 77},
    "Urgot": {'classes': ['Marksman'], 'id': 6},
    "Varus": {'classes': ['Marksman'], 'id': 110},
    "Vayne": {'classes': ['Marksman'], 'id': 67},
    "Veigar": {'classes': ['Burst Mage', 'Control Mage'], 'id': 45},
    "Vel'Koz": {'classes': ['Artillery Mage'], 'id': 161},
    "Vi": {'classes': ['Diver'], 'id': 254},
    "Viktor": {'classes': ['Control Mage'], 'id': 112},
    "Vladimir": {'classes': ['Battle Mage'], 'id': 8},
    "Volibear": {'classes': ['Vanguard'], 'id': 106},
    "Warwick": {'classes': ['Diver'], 'id': 19},
    "Wukong": {'classes': ['Diver'], 'id': 62},
    "Xerath": {'classes': ['Artillery Mage'], 'id': 101},
    "Xin Zhao": {'classes': ['Diver'], 'id': 5},
    "Yasuo": {'classes': ['Skirmisher'], 'id': 157},
    "Yorick": {'classes': ['Juggernaut'], 'id': 83},
    "Zac": {'classes': ['Vanguard', 'Juggernaut'], 'id': 154},
    "Zed": {'classes': ['Assassin'], 'id': 238},
    "Ziggs": {'classes': ['Artillery Mage'], 'id': 115},
    "Zilean": {'classes': ['Utility'], 'id': 26},
    "Zyra": {'classes': ['Control Mage'], 'id': 143}
}