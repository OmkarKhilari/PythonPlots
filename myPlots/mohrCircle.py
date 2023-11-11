import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import numpy as np

# Initialize global variables
xStress = 0.0
yStress = 0.0
shear = 0.0

def update_plot(event):
    global xStress, yStress, shear
    xStress = float(x_text_box.text)
    yStress = float(y_text_box.text)
    shear = float(shear_text_box.text)

    ax.cla()  # Clear the previous plot
    plotFunction(xStress, yStress, shear)

def plotFunction(xStress, yStress, shear):
    center = (xStress + yStress) * 0.5
    radius = np.sqrt(((xStress - yStress) * 0.5)**2 + shear**2)

    pStress1 = center - radius
    pStress2 = center + radius

    angles = np.linspace(0, 2 * np.pi, 1000)
    x_axis = center + radius * np.cos(angles)
    y_axis = np.sin(angles) * radius
    
    t_pos = np.array([xStress, xStress, yStress, yStress])
    t_neg = np.array([0, shear, -shear, 0])

    horLinex = np.array([pStress1, pStress2])
    horLiney = np.array([0, 0])

    ax.plot([center, xStress, yStress, pStress1, pStress2], [0, shear, -shear, 0, 0], 'ro')
    ax.grid(True)
    ax.plot(t_pos, t_neg)
    ax.plot(horLinex, horLiney, 'black')
    ax.plot(x_axis, y_axis)
    ax.legend()

# Create the interactive plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

ax.set_title('Mohr Circle')

# Text input boxes
x_text_box = TextBox(plt.axes([0.1, 0.01, 0.1, 0.075]), 'xStress:')
y_text_box = TextBox(plt.axes([0.35, 0.01, 0.1, 0.075]), 'yStress:')
shear_text_box = TextBox(plt.axes([0.6, 0.01, 0.1, 0.075]), 'Shear:')

update_button = Button(plt.axes([0.85, 0.01, 0.1, 0.075]), 'Update')

# Attach update_plot function to the button's action
update_button.on_clicked(update_plot)

plt.show()
