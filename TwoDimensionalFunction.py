import numpy as np
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
import matplotlib.pyplot as plt
plt.imshow(z, origin='lower', extent=(0, 5, 0, 5), cmap='viridis')
plt.colorbar()  
plt.title('2D Function Visualization')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
