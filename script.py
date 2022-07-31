# TODO:
#   - create date filter
#   - create Windows visualization for plots (some libs can works as powerbi)
#   - create pdf conversion for plots

import csv
import sys
import itertools

import skrplt.utils as utils
import skrplt.pvp.execution as pvp
import skrplt.pve.execution as pve

# Read data from first argue
filename = sys.argv[1]
if not filename.__contains__(".csv"):
    filename += ".csv"
file = open(filename, encoding='UTF-8')
csv_reader = csv.reader(file)

raw_data = []
for row in itertools.islice(csv_reader, utils.sample_size):
    raw_data.append(row)
if raw_data[0][7].count('PID') == 0:
    pve.execute(raw_data)
else:
    pvp.execute(raw_data)
file.close()


