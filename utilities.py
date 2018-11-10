# Functions for showing result
import matplotlib.pyplot as plt
color_list=['#377eb8', '#ff7f00', '#4daf4a','#f781bf', '#a65628', '#984ea3','#999999', '#e41a1c', '#dede00']
def show_result(cluster,data,show_data,color_list=color_list):
    x_clusters=cluster.x_clusters
    cluster_type = set(x_clusters)
    for i, j in enumerate(cluster_type):
        plt.scatter(data[x_clusters == j, 0], data[x_clusters == j, 1])
    plt.scatter(show_data[:, 0], show_data[:, 1], c='#e41a1c')
def displot_imgs(cluster, data_set, test_count=3):
    for data in data_set:
        cluster.fit(data)
        plt.figure(figsize=(18, 5))
        for i in range(1, test_count + 1):
            plt.subplot(1, test_count, i)
            show_result(cluster, data,cluster.centroids)