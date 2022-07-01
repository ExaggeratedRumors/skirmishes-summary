import matplotlib.pyplot as plt
import numpy as np


def create_bar_graph(data, profession):
    dataset = data[data.first_player_prof == profession]
    print(dataset.values)

# TODO: Create bar graph by:
#   - 5 plots for every profession for skirmishes vs single enemy profession
#   - percentage values of winrate for every level range
