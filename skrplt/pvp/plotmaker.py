import matplotlib.pyplot as plt
from skrplt.pvp import datamaker
from skrplt import utils


def create_result_graph(data, profession):
    data = datamaker.filter_profession(data, profession)
    wr = [0, 0, 0, 0, 0]
    plots = [None] * 6
    fig, ((plots[0], plots[1], plots[2]), (plots[3], plots[4], plots[5])) = plt.subplots(2, 3)
    fig.suptitle(f'Results for profession: {profession}\n'
                 f'Numbers inside graph means amount of samples in pointed level range',
                 fontsize=14, fontweight='bold')

    i = 0
    for prof in data:
        # fill winratio array
        number_of_fights = [data[prof][val][1] for val in data[prof]]
        wins = [data[prof][val][0] for val in data[prof]]
        wr[i] = sum(wins) / sum(number_of_fights)

        # calculate winratio
        for lvl_range in data[prof]:
            data[prof][lvl_range] = 0 if data[prof][lvl_range][1] == 0 else data[prof][lvl_range][0] / \
                                                                            data[prof][lvl_range][1]

        # paint bars
        x = range(len(data[prof]))
        y = list(data[prof].values())
        labels = list(data[prof].keys())
        plots[i].bar(
            x,
            y,
            tick_label=labels,
            color=['green', 'lime']
        )

        # paint number_of_fights labels
        for j in x:
            plots[i].text(j - 0.2, 0.2, number_of_fights[j], ha='center', va='center', fontsize=9, rotation=-90)

        # paint titles and descriptions
        plots[i].set_title(f"{utils.professions[profession]} vs {utils.professions[prof]}")
        plots[i].set_xticklabels(data[prof], rotation=-90)
        plots[i].set_ylim([0, 1])
        plots[i].plot(x, [0.5 for _ in x], 'k--')
        plots[i].set_ylabel('WR')
        plots[i].set_xlabel('lvl range')
        i += 1

    # paint summary graph
    create_summary_graph(ax=plots[5], wr=wr, data=data)

    fig.set_size_inches(15, 8)
    fig.tight_layout()
    plt.show()


def create_summary_graph(ax, wr, data):
    colors = ['gold' if i > 0.5 else 'red' for i in wr]
    ax.bar(
        range(len(wr)),
        wr,
        tick_label=list(data.keys()),
        color=colors
    )
    for j in range(len(wr)):
        ax.text(j, wr[j] + 0.05, "{:.2f}".format(wr[j]), ha='center', va='center', fontsize=9)
    ax.set_ylim([0, 1])
    x = range(len(wr))
    ax.plot(x, [0.5 for _ in x], 'k--')
    ax.set_ylabel('WR')
    ax.set_xlabel('professions')
    ax.set_title("summary")
