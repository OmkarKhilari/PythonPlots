import matplotlib.pyplot as plt
import numpy as np

def plotFunction(xStress, yStress, shear):
    center = (xStress + yStress) * 0.5
    radius = np.sqrt(((xStress - yStress)*0.5)**2 + shear**2)

    pStress1 = center - radius
    pStress2 = center + radius

    # xAxis = np.array([0, 1000])
    # yAxis = np.array([0, 1000])
    angles = np.linspace(0,2*np.pi , 1000)
    # print(angles)
    x_axis = center + radius * np.cos(angles)
    y_axis = np.sin(angles) * radius
    
    t_pos = np.array([xStress,xStress,yStress,yStress])
    t_neg = np.array([0,shear,-shear,0])

    horLinex = np.array([pStress1,pStress2])
    horLiney = np.array([0,0])
    # x_axis_point1 = np.array([])

    # print(center)
    # plt.plot([center,0], [xStress,shear], [yStress, -shear], [pStress1,0], [pStress2,0])
    plt.plot([center,xStress,yStress,pStress1,pStress2], [0,shear,-shear,0,0] , 'ro')
    plt.grid(True)
    plt.plot(t_pos,t_neg)
    plt.plot(horLinex,horLiney, 'black')
    plt.plot(x_axis,y_axis)
    plt.legend()
    plt.show()

plotFunction(10,20,5)




