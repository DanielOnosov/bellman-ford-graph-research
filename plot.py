

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

dfl = pd.read_csv("matrixes_2001.csv")

xl = dfl["density"]
yl = dfl["vertexes"]
zl = dfl["time"]
el = dfl["edges"]
clear = dfl[dfl["density"] > 0.65]
average = dfl["time"].mean()
print(average)

# Тут допомагав ЩІ
colors = ["blue","green", "yellow", "orange", "orangered","red"]
cmap = LinearSegmentedColormap.from_list("violet_red", colors)

norm = plt.Normalize(vmin=min(zl), vmax=max(zl))
colors_mapped = cmap(norm(zl))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(yl, xl, zl, c=zl, cmap=cmap, vmin=0, vmax=300)

ax.set_xlabel('кількість вершин')
ax.set_ylabel('щільність')
ax.set_zlabel('час, мілі сек.', rotation=90)
ax.view_init(elev=30, azim=-135)
ax.set_title('Представлення через матрицю суміжності')
ax.set_zlim(0, 300)

cbar = fig.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('час, мілі сек.')

plt.show()


plt.scatter(el**3, zl, color = 'blue')
plt.xlabel('грані^3')
plt.ylabel('час')
plt.title('час від формулм, матриця суміжності')
plt.grid(True)
plt.ylim(0, 300)
plt.show()