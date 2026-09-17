import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import CenteredNorm
import seaborn as sns
from pathlib import Path

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

# Arrange the indices as a compact coordinate grid:
#
#   HG_00  HG_01  HG_02
#   HG_10  HG_11  HG_20
#
# This keeps HG_01 to the right of HG_00, HG_10 below it, and HG_11 on
# the diagonal while preserving the wide 2 x 3 footprint used by the slide.
mode_panels = [
    (HG_00, r"$|HG_{00}\rangle$"),
    (HG_01, r"$|HG_{01}\rangle$"),
    (HG_02, r"$|HG_{02}\rangle$"),
    (HG_10, r"$|HG_{10}\rangle$"),
    (HG_11, r"$|HG_{11}\rangle$"),
    (HG_20, r"$|HG_{20}\rangle$"),
]

# ==========================================
# 4. Visualization
# ==========================================
cmap = sns.blend_palette(["#56D6BE", panel_bg, "#FF967D"], as_cmap=True)

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
fig.patch.set_facecolor(navy_bg)

for ax, (mode, label) in zip(axes.flatten(), mode_panels):
    ax.set_facecolor(panel_bg)

    ax.imshow(
        mode,
        extent=[-grid_size, grid_size, -grid_size, grid_size],
        cmap=cmap,
        norm=CenteredNorm(),
        origin="lower",
    )

    ax.text(
        0.95,
        0.05,
        label,
        color=paper_text,
        fontsize=24,
        ha="right",
        va="bottom",
        transform=ax.transAxes,
    )

    ax.axis("off")

plt.subplots_adjust(wspace=0.05, hspace=0.05)

script_dir = Path(__file__).resolve().parent
outputs = [
    script_dir / "hg_modes_labeled.png",
    script_dir.parents[2] / "presentation_4" / "assets" / "hg_modes_strong_visuals.png",
]
for output in outputs:
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")

plt.close(fig)
