import csv
import sys
import itertools

import skrplt.datamaker as dm
import skrplt.plotmaker as pm

filename = sys.argv[1]
if not filename.__contains__(".csv"):
    filename += ".csv"
file = open(filename, encoding='UTF-8')
csv_reader = csv.reader(file)
raw_data = []
for row in itertools.islice(csv_reader, 10):
    raw_data.append(row)

dm.cleanup_data(raw_data)
dataset = dm.create_filtered_dataset(raw_data)
file.close()
pm.create_bar_graph(dataset, "h")

# TODO:
#   - read hiperparameters from Utils file (range, prof, server)
#   - create windows visualization for plots
#   - create pdf conversion for plots
#   - create filters for hiperparameters
