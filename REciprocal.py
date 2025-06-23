import numpy as np
np.random.seed(0)
def  compute_reciprocal(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1/values[i]
    return output
values  = np.random.randint(1, 10, size=6)  # Avoid zero to prevent division by zero
print("Original values:", values)
reciprocal_values = compute_reciprocal(values)
print("Reciprocal values:", reciprocal_values)