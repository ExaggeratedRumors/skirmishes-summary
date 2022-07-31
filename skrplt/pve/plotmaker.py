import matplotlib.pyplot as plt
from skrplt.pve import datamaker
import skrplt.utils as utils
import pandas as pd
import numpy as np


def create_score_graph(data, npc_names):
    dataset = datamaker.create_npcs_score_label(data, npc_names)
    # data standardization
    for _, value in dataset.items():
        fights_sum = sum(value)
        if fights_sum == 0:
            continue
        value[0] /= fights_sum
        value[1] /= fights_sum
        value[2] /= fights_sum

    df = pd.DataFrame({'Wygrane': np.array(list(dataset.values()))[:, 0],
                       'Przegrane': np.array(list(dataset.values()))[:, 1],
                       'Remisy': np.array(list(dataset.values()))[:, 2]},
                      index=dataset.keys())
    ax = df.plot(kind='barh', stacked=True,
                 figsize=(18, 7))
    for p in ax.patches:
        left, bottom, width, height = p.get_bbox().bounds
        fontsize = 8
        if width == 0:
            fontsize = 0
        ax.annotate("{:.2f}".format(width), xy=(left, bottom + height / 2),
                    ha='left', va='center', fontsize=fontsize)
    plt.legend(loc='upper center')
    plt.title("Wynik grupowych walk przeciw NPC")
    plt.xlabel("Odsetek zwycięstw")
    plt.show()


def create_group_amount_graph(data, npc_names):
    dataset = datamaker.create_group_amount_label(data, npc_names)
    # data standardization
    for _, value in dataset.items():
        group_sum = sum(value)
        if group_sum == 0:
            continue
        for i in range(len(value)):
            value[i] /= group_sum

    labeled_data = {}
    i = 0
    for _ in list(dataset.values())[0]:
        labeled_data[f"Grupa {utils.min_group + i}"] = np.array(list(dataset.values()))[:, i]
        i += 1

    df = pd.DataFrame(labeled_data, index=dataset.keys())
    ax = df.plot(kind='barh', stacked=True,
                 figsize=(18, 7))
    for p in ax.patches:
        left, bottom, width, height = p.get_bbox().bounds
        fontsize = 8
        if width < 0.02:
            fontsize = 0
        ax.annotate("{:.2f}".format(width), xy=(left + width / 2, bottom + height / 2),
                    ha='center', va='center', fontsize=fontsize)
    plt.legend(loc='upper center')
    plt.title("Wielkość grupy w walkach przeciw NPC")
    plt.xlabel("Odsetek liczności danej grupy")
    plt.show()