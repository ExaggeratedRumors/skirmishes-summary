import matplotlib.pyplot as plt
from skrplt.pvp import datamaker


def create_bar_graph(data, profession):
    data = datamaker.filter_profession(data, profession)
    plots = [0, 0, 0, 0, 0, 0]
    fig, ((plots[0], plots[1], plots[2]), (plots[3], plots[4], plots[5])) = plt.subplots(2, 3)
    i = 0
    wr = [0, 0, 0, 0, 0]
    for prof in data:
        number_of_fights = [data[prof][val][1] for val in data[prof]]
        wins = [data[prof][val][0] for val in data[prof]]
        wr[i] = sum(wins)/sum(number_of_fights)
        for lvl_range in data[prof]:
            data[prof][lvl_range] = 0 if data[prof][lvl_range][1] == 0 else data[prof][lvl_range][0] / \
                                                                            data[prof][lvl_range][1]
        plots[i].bar(
            range(len(data[prof])),
            list(data[prof].values()),
            tick_label=list(data[prof].keys())
        )
        obj_bar = plots[i].patches
        # for bar, label in zip(obj_bar, number_of_fights):
        #     plots[i].text(
        #         bar.get_x() + bar.get_width() / 2,
        #         5, label,
        #         ha="center", va="bottom"
        #     )
        plots[i].set_title(f"{profession} vs {prof}")
        plots[i].set_xticklabels(data[prof], rotation=-90)
        plots[i].set_ylim([0, 1])
        x = range(len(data[prof]))
        plots[i].plot(x, [0.5 for _ in x], 'k--')
        i += 1

    plots[5].bar(
        range(len(wr)),
        wr,
        tick_label=list(data.keys())
    )
    plots[5].set_ylim([0, 1])
    x = range(len(wr))
    plots[5].plot(x, [0.5 for _ in x], 'k--')

    fig.set_size_inches(15, 8)
    fig.tight_layout()
    plt.show()

