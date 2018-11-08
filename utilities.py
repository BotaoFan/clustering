# Functions for showing result
def show_result(cluster, data,color_list):
    x_cluster = cluster.fit(data)
    cluster_type = set(x_cluster)
    initial_x = cluster.initial_x
    for i, j in enumerate(cluster_type):
        plt.scatter(data[x_cluster == j, 0], data[x_cluster == j, 1], c=color_list[i])
    plt.scatter(initial_x[:, 0], initial_x[:, 1], c='#e41a1c')
def displot_imgs(cluster, data_set, test_count=3):
    for data in data_set:
        plt.figure(figsize=(18, 5))
        for i in range(1, test_count + 1):
            plt.subplot(1, test_count, i)
            show_result(cluster, data)