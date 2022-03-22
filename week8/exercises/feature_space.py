from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

def generate_babies(amount):
    baby_list = []
    while amount > 0:
        baby_list.append(
            (np.random.randint(42, 56), 
            round(np.random.uniform(2.4, 3.8), 1),
            np.random.randint(2, 12))
            )
        amount -= 1
    print(baby_list)
    return baby_list
    
def plot_babies(babies):
    plot_points = np.asarray(babies)
    x, y, z = plot_points[:,0], plot_points[:,1], plot_points[:,2]
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.scatter3D(x, y, z, color='green')
    plt.show()



