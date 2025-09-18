
import matplotlib.pyplot as plt
from math import sin, cos, pi, tan, sqrt
import numpy as np
import random

def cartesian_to_polar(coordinates):
    x = coordinates[0]
    y = coordinates[1]

    theta = tan(y/x)
    r = sqrt(x**2 + y**2)
    return r, theta

def cartesian_to_polar_all(coordinate_list):
    rs = []
    thetas = []
    for coordinate in coordinate_list:
        r, theta = cartesian_to_polar(coordinate)
        rs.append(r)
        thetas.append(theta)
    return rs, thetas

def create_shape(A, alpha, ts):
    phis = {}
    for t in ts:
        partial_sum = 0
        for k in range(len(A)):
            partial_sum += A[k]*cos(k*t - alpha[k]) #these first few partial sum terms are the global features?
        phis[t] = partial_sum

    return phis

def plot_polar_shape(radii, thetas,name):
    fig, axs = plt.subplots(1, 1, subplot_kw={'projection': 'polar'},figsize=(6, 6))
    axs.fill(thetas, radii, color="black")
    axs.plot(thetas, radii, color="black")
    axs.set_axis_off()
    #plt.savefig(name)
    plt.show()

def create_shapes(n, cat):
    for a in range (n):
        cartesian_descriptors = []  # x-y values
        for i in range(1, 11):
            coor = [i, i]
            cartesian_descriptors.append(coor)

        polar_A, polar_alpha = cartesian_to_polar_all(cartesian_descriptors)
        ts = np.arange(0, 2 * pi, pi / 20)
        print(f"############### {a} ##################")
        phis = create_shape(A=polar_A, alpha=polar_alpha, ts=ts)
        plot_polar_shape(radii=phis.values(), thetas=phis.keys(), name=f"cat_1/{a}.png")

if __name__ == '__main__':
    create_shapes(1, 1)
