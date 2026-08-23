import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import j1
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.colors import PowerNorm


def airy_disk(x, y, x0, y0, I0):
    """Calculates the intensity of an Airy disk at a given point."""
    r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    r = np.where(r == 0, 1e-10, r)
    return I0 * (2 * j1(r) / r) ** 2


def plot_rayleigh_column(
    distance,
    I1=1.0,
    I2=1.0,
    title="Rayleigh Criterion",
    fig_width=4.0,
    bottom_ratio="40%",
    crop_percent=0,
    line_alpha=0.7,
    sum_offset=0.0,
    gamma=1.0,
    log_y=False,  # <--- Added parameter to control y-axis scale
):
    """
    Plots a single column with a 2D interference pattern and a 1D intensity cross-section.

    Parameters:
    - fig_width: Width of the plots in inches.
    - bottom_ratio: Height of the bottom plot as a percentage of the top plot's height.
    - crop_percent: Percentage of the top image to crop overall (crops symmetrically from top and bottom).
    - line_alpha: Transparency level for the individual intensity lines.
    - sum_offset: Vertical offset added to the total intensity line to separate it from overlapping individual lines.
    - gamma: Power-law normalization for the 2D colormap. Values < 1.0 make faint outer rings more visible.
    - log_y: If True, uses a logarithmic scale for the 1D intensity plot to reveal faint secondary peaks.
    """
    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})

    crop_frac = crop_percent / 100.0
    keep_ratio = 1.0 - crop_frac

    # Dynamically calculate figure height to avoid clipping and preserve aspect ratio
    ratio_float = float(bottom_ratio.strip("%")) / 100
    fig_height = (fig_width * keep_ratio) * (1 + ratio_float) + 1.0

    fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))

    # --- Top Subplot (2D Image) ---
    grid_size = 400
    x = np.linspace(-8, 8, grid_size)
    y = np.linspace(-8, 8, grid_size)
    X, Y = np.meshgrid(x, y)

    intensity1_2d = airy_disk(X, Y, -distance / 2, 0, I1)
    intensity2_2d = airy_disk(X, Y, distance / 2, 0, I2)
    total_intensity_2d = intensity1_2d + intensity2_2d

    # Crop the 2D array and adjust extents
    crop_rows = int(grid_size * crop_frac / 2)
    if crop_rows > 0:
        total_intensity_2d = total_intensity_2d[crop_rows:-crop_rows, :]

    y_min = -8 + 16 * (crop_frac / 2)
    y_max = 8 - 16 * (crop_frac / 2)

    # Use Seaborn's "mako" colormap for the light intensity
    light_cmap = sns.color_palette("mako", as_cmap=True)

    ax1.imshow(
        total_intensity_2d,
        extent=[-8, 8, y_min, y_max],
        cmap=light_cmap,
        origin="lower",
        norm=PowerNorm(gamma=gamma),
    )
    ax1.set_title(title, pad=15, fontsize=14)
    ax1.axis("off")

    # --- Bottom Subplot Setup ---
    divider = make_axes_locatable(ax1)

    # Use the parameter to control the bottom plot's height
    ax2 = divider.append_axes("bottom", size=bottom_ratio, pad=0.3)

    # --- Bottom Subplot (1D Intensity Profile) ---
    x_1d = np.linspace(-8, 8, grid_size)
    intensity1_1d = airy_disk(x_1d, 0, -distance / 2, 0, I1)
    intensity2_1d = airy_disk(x_1d, 0, distance / 2, 0, I2)
    total_intensity_1d = intensity1_1d + intensity2_1d

    # Use Seaborn's "Set2" palette for the discrete lines
    set2_colors = sns.color_palette("Set2")

    ax2.plot(
        x_1d,
        intensity1_1d,
        linestyle="--",
        color=set2_colors[0],
        linewidth=2.5,
        alpha=line_alpha,
    )
    ax2.plot(
        x_1d,
        intensity2_1d,
        linestyle="--",
        color=set2_colors[1],
        linewidth=2.5,
        alpha=line_alpha,
    )
    ax2.plot(
        x_1d,
        total_intensity_1d + sum_offset,
        linestyle="-",
        color=set2_colors[2],
        linewidth=3,
    )

    ax2.set_xlabel("Radial Distance", fontsize=12)
    ax2.set_ylabel("Intensity" + (" (Log Scale)" if log_y else ""), fontsize=12)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_xlim(-8, 8)

    # <--- Apply logarithmic scale and adjust limits accordingly
    if log_y:
        ax2.set_yscale("log")
        # 1e-3 floor prevents the zeros of the Bessel function from stretching to negative infinity
        ax2.set_ylim(1e-3, max(np.max(total_intensity_1d + sum_offset) * 2.0, 2.0))
    else:
        ax2.set_ylim(0, max(np.max(total_intensity_1d + sum_offset) * 1.1, 1.2))

    sns.despine(ax=ax2)
    plt.savefig(
        f"rayleigh_{title.replace(' ', '_').lower()}.png", dpi=300, bbox_inches="tight"
    )
    plt.show()


# --- Example Usage ---

# 1. Resolved with log_y=True to reveal the secondary peaks in the 1D plot
plot_rayleigh_column(
    distance=4.5,
    I1=1.0,
    I2=0.4,
    title="Resolved",
    fig_width=5,
    bottom_ratio="60%",
    crop_percent=50,
    line_alpha=0.6,
    sum_offset=0.05,
    gamma=1,
    log_y=False,
)

# 2. Unresolved
plot_rayleigh_column(
    distance=2.5,
    I1=1.0,
    I2=0.4,
    title="Unresolved",
    fig_width=5,
    bottom_ratio="60%",
    crop_percent=50,
    line_alpha=1.0,
    sum_offset=0.05,
    gamma=1,
    log_y=False,
)
