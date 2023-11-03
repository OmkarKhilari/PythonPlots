import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots()

circle = Circle((0.5, 0.5), 0.2, fill=False, color='blue', linewidth=2)
ax.add_patch(circle)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Circle Example')

plt.show()
