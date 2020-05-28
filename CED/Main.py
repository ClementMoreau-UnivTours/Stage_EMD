from CED import *
from Sim_stock import *
import pandas as pd
from Context_function import *
import numpy as np
import multiprocessing as mp

def compute_sequences(df):
    """
    :param df:          Dataframe -- Dafaframe of explorations sequences and queries

    :return: List<NumpyArray<String>> -- List of all sequences
    """
    sequences = []  # All sequences
    seq_i = [] # Sequence in process
    buff_name = df['id'][0]
    for index, row in df.iterrows():
        if row['id'] != buff_name :
            sequences.append(np.array(seq_i) )
            seq_i = []
            buff_name = row['id']
        seq_i.append(str(row['activity']))
    sequences.append(seq_i)
    return sequences

def stop_move(s):
    """
    :param s: Mobility Sequence
    :return: Two Sequences STOP and MOVE
    """
    stop = []
    move = []
    move_set = []
    for x in s:
        if x < 100 : # If id of activity is >= 100, it's a move activity
            stop.append(x)
            if move_set:
                move.append(set(move_set))
            move_set.clear()
        else :
            move_set.append(x)
    return [stop,move]


"""
# Creation de la matrice des similarités (non utile ici)

all_act = list(map(str, list(emd['activity'].unique())))
M_sim = np.zeros((len(all_act), len(all_act)))
G = nx.read_adjlist("ontologie.txt", create_using=nx.DiGraph)
for i in range(len(all_act)):
    for j in range(i, len(all_act)):
        M_sim[i][j] = wu_palmer(all_act[i], all_act[j], G)
        M_sim[j][i] = M_sim[i][j]

def get_sim(x, y):
    return M_sim[all_act.index(x)][all_act.index(y)]
"""

"""""""""""""""""
!!! MAIN HERE !!!
"""""""""""""""""

# Load data
emd = pd.read_csv("sequences_original_modif.csv", sep=';')


### /!\ CED parameters /!\ ###

f_k = gaussian
sim = Sim_stock('sim_ontology.csv', 'names.csv').get_sim
alpha = 0

### Compute sequences from a file  ###
sequences = compute_sequences(emd)

print(CED(sequences[0], sequences[1], sim, f_k, alpha))


## Multi-thread computing (takes long time...)
"""
nb_sequences = 100 #len(sequences)

pool = mp.Pool(mp.cpu_count())
result = pool.starmap(CED, [(sequences[i], sequences[j], sim, f_k, alpha) for i in range(nb_sequences) for j in range(i+1)])
pool.close()


CED_matrix = np.zeros((nb_sequences, nb_sequences)) # Matrice des distance CED

for k in range(len(result)) :
    i = int(-1/2 + sqrt(1/4 + 2*k))
    j = int(k - i*(i+1)/2)
    CED_matrix[i, j] = result[k]
    CED_matrix[j, i] = CED_matrix[i, j]

## TO export CED matrix
#CED_csv = pd.DataFrame(data=CED_matrix, columns=sequences_name)
"""

