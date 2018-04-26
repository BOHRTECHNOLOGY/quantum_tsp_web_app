import matplotlib.pyplot as plt


def plot_solution(name, nodes_array, solution):
    plt.scatter(nodes_array[:, 0], nodes_array[:, 1], s=200)
    for i in range(len(nodes_array)):
        plt.annotate(i, (nodes_array[i, 0] + 0.15, nodes_array[i, 1] + 0.15), size=16, color='r')

    plt.xlim([min(nodes_array[:, 0]) - 1, max(nodes_array[:, 0]) + 1])
    plt.ylim([min(nodes_array[:, 1]) - 1, max(nodes_array[:, 1]) + 1])
    for i in range(len(solution) - 1):
        A = solution[i]
        B = solution[i + 1]
        plt.plot([nodes_array[A, 0], nodes_array[B, 0]], [nodes_array[A, 1], nodes_array[B, 1]], c='r')

    cost = calculate_cost(get_tsp_matrix(nodes_array), solution)
    title_string = "Cost:" + str(cost)
    title_string += "\n" + str(solution)
    plt.title(title_string)
    plt.savefig(name + '.png')
    plt.clf()
