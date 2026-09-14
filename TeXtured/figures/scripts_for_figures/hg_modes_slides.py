import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import CenteredNorm
import seaborn as sns

# ==========================================
# 1. Define Parameters
# ==========================================
w0 = 1.0
delta_x = 0.0
delta_y = 0.0
grid_size = 2.5
resolution = 400

# Colors
navy_bg = "#111D2E"
panel_bg = "#1C2B40"
paper_text = "#F5F3EE"

# ==========================================
# 2. Create the Spatial Grid
# ==========================================
x = np.linspace(-grid_size, grid_size, resolution)
y = np.linspace(-grid_size, grid_size, resolution)
X, Y = np.meshgrid(x, y)

Xs = (X - delta_x) / w0
Ys = (Y - delta_y) / w0

# ==========================================
# 3. Define the Spatial Modes
# ==========================================
psi_0 = np.exp(-(Xs**2 + Ys**2))

u = np.sqrt(2) * Xs
v = np.sqrt(2) * Ys

HG_00 = psi_0
HG_01 = (2 * v) * psi_0
HG_10 = (2 * u) * psi_0
HG_20 = (4 * u**2 - 2) * psi_0
HG_11 = (2 * u) * (2 * v) * psi_0
HG_02 = (4 * v**2 - 2) * psi_0

# Reordered modes to match the requested label sequence
modes = [HG_00, HG_01, HG_10, HG_20, HG_11, HG_02]
labels = [r"$|HG_{00}\rangle$", r"$|HG_{01}\rangle$", r"$|HG_{10}\rangle$", "", "", ""]

# ==========================================
# 4. Visualization
# ==========================================
cmap = sns.blend_palette(["#56D6BE", panel_bg, "#FF967D"], as_cmap=True)

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
fig.patch.set_facecolor(navy_bg)

for ax, mode, label in zip(axes.flatten(), modes, labels):
    ax.set_facecolor(panel_bg)

    ax.imshow(
        mode,
        extent=[-grid_size, grid_size, -grid_size, grid_size],
        cmap=cmap,
        norm=CenteredNorm(),
        origin="lower",
    )

    # Place name in the bottom right corner if a label exists for this panel
    if label:
        ax.text(
            0.95,
            0.05,
            label,
            color=paper_text,
            fontsize=20,
            ha="right",
            va="bottom",
            transform=ax.transAxes,
        )

    ax.axis("off")

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig(
    "hg_modes_labeled.png", dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight"
)
plt.show()
