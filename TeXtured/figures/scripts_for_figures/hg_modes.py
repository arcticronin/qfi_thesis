import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import CenteredNorm

# ==========================================
# 1. Define Parameters
# ==========================================
w0 = 1.0  # Beam waist radius
delta_x = 0.0  # Residual spatial misalignment in x
delta_y = 0.3  # Residual spatial misalignment in y (exaggerated for visualization)
grid_size = 2.0  # Half-width of the spatial grid
resolution = 400  # Number of pixels along one axis

fontsize = 18 # title has +3

# ==========================================
# 2. Create the Spatial Grid
# ==========================================
x = np.linspace(-grid_size, grid_size, resolution)
y = np.linspace(-grid_size, grid_size, resolution)
X, Y = np.meshgrid(x, y)

# ==========================================
# 3. Define the Spatial Modes
# ==========================================
# Fundamental Gaussian mode (psi_0)
# Note: Using the standard Gaussian amplitude profile
psi_0 = np.exp(-(X**2 + Y**2) / w0**2)

# HG_00 Mode
HG_00 = psi_0

# HG_01 Mode (x-axis misalignment)
HG_01 = ((X - delta_x) / w0) * psi_0

# HG_10 Mode (y-axis misalignment)
HG_10 = ((Y - delta_y) / w0) * psi_0

# Store modes for easy iteration during plotting
modes = [
    (HG_00, r"$|HG_{00}\rangle$"),
    (HG_01, r"$|HG_{01}\rangle$"),
    (HG_10, r"$|HG_{10}\rangle$"),
]

# ==========================================
# 4. Visualization
# ==========================================
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle(
    f"Hermite-Gaussian Spatial Modes: ($w_0={w0}$, $\delta_x={delta_x}$, $\delta_y={delta_y}$)",
    fontsize=fontsize + 3,
)

for i, (mode, title) in enumerate(modes):
    # Plot Field Amplitude (Top Row)
    # Using a diverging colormap (RdBu) to clearly show positive (blue) and negative (red) lobes
    ax_amp = axes[0, i]
    im_amp = ax_amp.imshow(
        mode,
        extent=[-grid_size, grid_size, -grid_size, grid_size],
        cmap="RdBu_r",
        norm=CenteredNorm(),
        origin="lower",
    )
    ax_amp.set_title(f"{title} Amplitude", fontsize=fontsize)
    ax_amp.set_xlabel("x")
    ax_amp.set_ylabel("y")
    fig.colorbar(im_amp, ax=ax_amp, fraction=0.046, pad=0.04)

    # Plot Field Intensity (Bottom Row)
    # Intensity is the absolute square of the amplitude
    intensity = np.abs(mode) ** 2
    ax_int = axes[1, i]
    im_int = ax_int.imshow(
        intensity,
        extent=[-grid_size, grid_size, -grid_size, grid_size],
        cmap="inferno",
        origin="lower",
    )
    ax_int.set_title(f"{title} Intensity ($|E|^2$)", fontsize=fontsize)
    ax_int.set_xlabel("x")
    ax_int.set_ylabel("y")
    fig.colorbar(im_int, ax=ax_int, fraction=0.046, pad=0.04)

plt.tight_layout()
plt.savefig("hg_modes_visualization.png", dpi=300)
plt.show()
