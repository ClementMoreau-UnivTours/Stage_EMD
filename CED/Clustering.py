import numpy as np
import statistics as sc
import sklearn.metrics

def clusters_identity(assignement, sequences_name):
    """
    :param assignement: List<Int> -- List of the class of each elements
    :param sequences_name : List<String> -- Name of each element
    :return: List<List<int>> -- List of the id element of each cluster
    """
    clusters = []
    nb_clust = max(assignement)
    for i in range(1,nb_clust+1) :
        c_i = []
        for j in range(len(assignement)) :
            if(assignement[j] == i) :
                c_i += [j]
        clusters += [c_i]

    # Matching to the name
    clusters_id = []
    for c in clusters:
        clust = []
        for e in c:
            clust += [sequences_name[e]]
        clusters_id += [clust]
    print("Clusters idententity :\n", clusters_id, "\n")
    print("Clusters :\n", clusters, "\n")
    return clusters

def medoid(clusters, distMatrix, sequences_name) :
    """
    :param clusters: List<List<int>> -- List of the id element of each cluster (clusters_identity)
    :param distMatrix: Numpy 2D array Float -- Distance Matrix (CED_matrix)
    :param sequences_name: List<String> -- Name of each element
    :return: List<int> -- Id of medoid for each cluster
    """
    medoids = []
    k = 1
    for tab in clusters :
        subMatrix = np.zeros((len(tab), len(tab)))
        for i in range(len(tab)):
            for j in range(i, len(tab)):
                subMatrix[i, j] = distMatrix[tab[i],tab[j]]
                subMatrix[j, i] = distMatrix[tab[i],tab[j]]
        print ("Diameter of cluster", k, " : ", np.max(subMatrix))
        medoid = np.argmin(subMatrix.sum(axis=0))
        medoids += [tab[medoid]]
        k += 1
    # Matching to the name
    medoid_id = []
    for m in medoids:
       medoid_id += [sequences_name[m]]
    print("\nMedoid identity :\n", medoid_id, "\n")
    print("\nMedoid :\n", medoids, "\n")
    return medoids

def silhouette_cluster(clusters, distMatrix, assignement):
    """
    :param clusters: List<List<int>> -- List of the id element of each cluster
    :param distMatrix: Numpy 2D array Float -- Distance Matrix (CED_matrix)
    :param assignement: List<Int> -- List of the class of each elements
    :return: List<Float> -- Silhouette score for each cluster
    """
    silhouette_samples = sklearn.metrics.silhouette_samples(distMatrix, assignement, metric="precomputed")
    silhouette_cluster = []
    for c in clusters :
        score_sil = []
        for e in c :
            score_sil += [silhouette_samples[e]]
        silhouette_cluster += [sc.mean(score_sil)]
    return silhouette_cluster