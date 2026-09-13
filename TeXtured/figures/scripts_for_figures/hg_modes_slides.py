import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import eval_hermite
import math

# Define the spatial grid
x = np.linspace(-5, 5, 500)

# Generate a custom 6-color palette blending the two hex codes
custom_palette = sns.blend_palette(["#56D6BE", "#FF967D"], n_colors=6)

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot the first 6 Hermite-Gaussian modes
for n in range(6):
    # Normalization constant for the n-th mode
    N_n = 1.0 / np.sqrt((2**n) * math.factorial(n) * np.sqrt(np.pi))
    
    # Calculate the Hermite-Gaussian function
    # H_n(x) * exp(-x^2 / 2)
    psi_n = N_n * eval_hermite(n, x) * np.exp(-x**2 / 2.0)
    
    # Plot using the corresponding color from the custom palette
    plt.plot(x, psi_n, color=custom_palette[n], label=f'Mode $n={n}$', linewidth=2)

# Formatting and aesthetics
plt.title('First 6 1D Hermite-Gaussian Modes')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.legend(title='Mode Order')
plt.grid(True, alpha=0.3)
sns.despine()

# Display the plot
plt.show()