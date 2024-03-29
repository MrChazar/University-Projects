import random
import math
import matplotlib.pyplot as plt
import numpy as np


def determine_score(distance):
    if distance < 0.1:
        return 6
    elif distance < 0.2:
        return 5
    elif distance < 0.3:
        return 4
    elif distance < 0.4:
        return 3
    elif distance < 0.5:
        return 2
    elif distance < 0.6:
        return 1
    else:
        return 0


def generate_shield(coordinates, x=[], y=[], x_1=[], y_1=[],  rays=None, type="single_a"):
    if rays is None:
        rays = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    fig, ax = plt.subplots()
    for radius in rays:
        circle = plt.Circle(coordinates, radius, edgecolor='b', facecolor='none')
        ax.add_patch(circle)

    ax.set_aspect('equal', adjustable='box')
   # ax.set_xlim(-1, 1)
   # ax.set_ylim(-1, 1)
    if type == "single_a":
        plt.scatter(x, y, color='red', label='Points', s=10)
        plt.title("Shoot A:")
    if type == "single_b":
        plt.scatter(x, y, color='blue', label='Points', s=10)
        plt.title("Shoot B:")
    if type == "multiple":
        plt.scatter(x, y, color='red', label='Points A', s=10)
        plt.scatter(x_1, y_1, color='blue', label='Points B', s=10)

    plt.xlabel("axis X")
    plt.ylabel("axis Y")
    plt.grid(True)
    plt.show()


def shoot_a():
    d_x = np.random.normal(0, 1)
    x = random.uniform(-0.75, 0.75)
    y = random.uniform(-0.75, 0.75)
    r = math.sqrt(pow(x + d_x,2) + pow(y,2) )
    return [x+d_x, y, r]


def shoot_b():
    d_x = np.random.normal(0, 1)
    r = random.uniform(0, 0.75)
    phi = random.uniform(-3.14, 3.14)
    x = r*math.cos(phi)
    y = r*math.sin(phi)
    return [x+d_x, y, r]


def simulation(type_of_shoot):
    temp = []
    x_points = []
    y_points = []
    for _ in range(10):
        if type_of_shoot == "A":
            x, y, r = shoot_a()
            temp.append(determine_score(r))
            x_points.append(x)
            y_points.append(y)
        elif type_of_shoot == "B":
            x, y, r = shoot_b()
            temp.append(determine_score(r))
            x_points.append(x)
            y_points.append(y)
    return [temp, x_points, y_points]


def generate_histogram(avg_a, avg_b):
    fig, axs = plt.subplots(1, 2)

    axs[0].hist(avg_a, bins=15, color='red', alpha=0.7, )
    axs[0].set_title("Shooting Range A")

    axs[1].hist(avg_b, bins=15, color='blue', alpha=0.7)
    axs[1].set_title("Shooting Range B")

    plt.tight_layout()
    plt.show()