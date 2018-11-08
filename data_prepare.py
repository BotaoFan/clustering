import warnings

import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster, datasets, mixture


np.random.seed(0)

# ============
# Generate datasets. We choose the size big enough to see the scalability
# of the algorithms, but not too big to avoid too long running times
# ============
n_samples = 1500
def get_data(n_samples=1500,random_state=24601):
    #Noisy_circles
    noisy_circles = datasets.make_circles(n_samples=n_samples, factor=.5,noise=.05,random_state=random_state)
    #Noisy_moons
    noisy_moons = datasets.make_moons(n_samples=n_samples, noise=.05,random_state=random_state)
    #Blobs
    blobs = datasets.make_blobs(n_samples=n_samples,random_state=random_state)
    #Anisotropicly distributed data
    X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    X_aniso = np.dot(X, transformation)
    aniso = (X_aniso, y)
    return [noisy_circles,noisy_moons,blobs,aniso]

def show_four_dataset(data_set_list):
    [noisy_circles, noisy_moons, blobs, aniso]=data_set_list
    #Show the plot of data set
    color_list=['#377eb8', '#ff7f00', '#4daf4a','#f781bf', '#a65628', '#984ea3','#999999', '#e41a1c', '#dede00']
    plt.figure(figsize=(18,4))

    plt.subplot(141)
    noisy_circles_data=noisy_circles[0]
    noisy_circles_cluster=noisy_circles[1]
    cluster_type=set(noisy_circles_cluster)
    for i,j in enumerate(cluster_type):
        plt.scatter(noisy_circles_data[noisy_circles_cluster==j,0],noisy_circles_data[noisy_circles_cluster==j,1],c=color_list[i])

    plt.subplot(142)
    noisy_moons_data=noisy_moons[0]
    noisy_moons_cluster=noisy_moons[1]
    cluster_type=set(noisy_moons_cluster)
    for i,j in enumerate(cluster_type):
        plt.scatter(noisy_moons_data[noisy_moons_cluster==j,0],noisy_moons_data[noisy_moons_cluster==j,1],c=color_list[i])

    plt.subplot(143)
    blobs_data=blobs[0]
    blobs_cluster=blobs[1]
    cluster_type=set(blobs_cluster)
    for i,j in enumerate(cluster_type):
        plt.scatter(blobs_data[blobs_cluster==j,0],blobs_data[blobs_cluster==j,1],c=color_list[i])

    plt.subplot(144)
    aniso_data=aniso[0]
    aniso_cluster=aniso[1]
    cluster_type=set(aniso_cluster)
    for i,j in enumerate(cluster_type):
        plt.scatter(aniso_data[aniso_cluster==j,0],aniso_data[aniso_cluster==j,1],c=color_list[i])