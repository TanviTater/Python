import numpy as np
mean  = [0,0]
cov = [[1,2],
       [2,5]]  # covariance matrix
n = 100  # number of points
X = np.random.multivariate_normal(mean, cov, n)  # Generate random points
print("Shape of X:", X.shape)  # Print the shape of the generated points
import matplotlib.pyplot as plt
import seaborn ; seaborn.set()
plt.scatter(X[:, 0], X[:, 1])
plt.show()
indices = np.random.choice(X.shape[0], 20, replace=False)
print("Selected indices:", indices)  # Print the selected indices
selected_points = X[indices]  # Select random points
print("Selected points shape:\n", selected_points.shape)  # Print the selected 
plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selected_points[:, 0], selected_points[:, 1],
            facecolor='none', s=200);
plt.title("Scatter plot with selected points")
plt.show()  