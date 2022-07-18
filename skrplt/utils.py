import configparser
from dataclasses import dataclass

private_servers = ['astraja', 'asylum', 'ataensic', 'badzior', 'dionizos',
                   'dream', 'elizjum', 'ertill', 'febris', 'hades',
                   'helios', 'hypnos', 'inferno', 'latimar', 'legion',
                   'lupus', 'majorka', 'mordor', 'narwhals', 'nerthus',
                   'nexos', 'nubes', 'nyras', 'odysea', 'orchidea',
                   'pandora', 'regros', 'riventia', 'stark', 'stoners',
                   'syberia', 'thantos', 'unia', 'virtus', 'zefira'
                   ]
public_servers = ['aether', 'aldous', 'berufs', 'brutal', 'classic',
                  'fobos', 'gefion', 'hutena', 'jaruna', 'katahha',
                  'lelwani', 'majuna', 'nomada', 'perkun', 'tarhuna',
                  'telawel', 'tempest', 'zemyna', 'zorza']

config = configparser.ConfigParser()
config.read('config.ini')
server = config['general']['server']
analysis_type = config['general']['analysis_type']
sample_size = int(config['general']['sample_size'])

min_lvl = int(config['pve']['min_lvl'])
max_lvl = int(config['pve']['max_lvl'])
min_group = int(config['pve']['min_group'])

target_profession = config['pvp']['target_profession']
min_advantage = int(config['pvp']['min_advantage'])
max_advantage = int(config['pvp']['max_advantage'])
advantage_factor = float(config['pvp']['advantage_factor'])
min_level = int(config['pvp']['min_level'])
max_level = int(config['pvp']['max_level'])
