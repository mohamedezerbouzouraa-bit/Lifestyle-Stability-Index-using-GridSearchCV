import numpy as np

def load_data():
    X = np.load("data/dataset.npy")
    y = np.load("data/targets.npy")
    return X, y
