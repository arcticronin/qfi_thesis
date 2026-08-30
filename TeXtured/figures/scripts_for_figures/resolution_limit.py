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

def gaussian_psf(x, y, x0, y0, I0, w0):
    """Gaussian intensity PSF with common width w0."""
    r_squared = (x - x0) ** 2 + (y - y0) ** 2
    return I0 * np.exp(-r_squared / (2 * w0**2))


def compute_w0(radial_profile, max_radius=10.0, samples=20000):
    """Return the characteristic width of a centrally peaked radial PSF.

    The width w0 is defined as the first radius at which the intensity equals
    exp(-1/2) times its on-axis value. With this definition, the result is the
    standard deviation for a Gaussian intensity PSF and an equivalent Gaussian
    width for the central lobe of an Airy PSF.

    Parameters
    ----------
    radial_profile : callable
        Function that accepts an array of non-negative radii and returns the
        corresponding PSF intensities.
    max_radius : float
        Largest radius searched for the first threshold crossing.
    samples : int
        Number of radial samples used to locate and interpolate the crossing.
    """
    radii = np.linspace(0.0, max_radius, samples)
    intensities = np.asarray(radial_profile(radii), dtype=float)

    if intensities.shape != radii.shape:
        raise ValueError("radial_profile must return one intensity per radius.")
    if not np.all(np.isfinite(intensities)) or intensities[0] <= 0:
        raise ValueError("radial_profile must be finite and positive at r = 0.")

    target = intensities[0] * np.exp(-0.5)
    crossings = np.flatnonzero(intensities <= target)
    if crossings.size == 0:
        raise ValueError(
            "The PSF does not reach exp(-1/2) of its peak within max_radius."
        )

    upper_index = crossings[0]
    if upper_index == 0:
        return 0.0

    lower_index = upper_index - 1
    r1, r2 = radii[lower_index], radii[upper_index]
    i1, i2 = intensities[lower_index], intensities[upper_index]

    # Linear interpolation is sufficient because the radial sampling is dense.
    return r1 + (target - i1) * (r2 - r1) / (i2 - i1)


def add_dimension_markers(ax, distance, I1, I2, w0):
    """Mark the source separation d, the common Gaussian width w0 and the intensities"""
    """The first two quantities are marked in the resolved plot, the intensities in the unresolved"""
    marker_color = "#888888"
    marker_alpha = 0.8
    max_intensity = max(I1, I2)
    centers = (-distance / 2, distance / 2)

    if distance > 3:

        # ------ Distance d marker -------

        # Put the separation marker above the profiles. The dotted guides associate
        # its endpoints with the centres of the two individual PSFs.
        d_height = 1.12 * max_intensity
        for center, peak in zip(centers, (I1, I2)):
            ax.plot(
                [center, center],
                [peak, d_height],
                color=marker_color,
                linewidth=0.9,
                linestyle=":",
                alpha=0.6,
                zorder=4,
            )
        ax.annotate(
            "",
            xy=(centers[1], d_height),
            xytext=(centers[0], d_height),
            arrowprops=dict(
                arrowstyle="<->",
                color=marker_color,
                linewidth=1.1,
                shrinkA=0,
                shrinkB=0,
                alpha=marker_alpha,
            ),
            zorder=5,
        )
        ax.text(
            0,
            d_height + 0.035 * max_intensity,
            r"$d$",
            ha="center",
            va="bottom",
            color=marker_color,
            fontsize=11,
        )

        # ----- Width w0 marker -------

        # For exp[-(x-x0)^2/(2 w0^2)], w0 is the horizontal distance from the
        # centre to the point where the intensity has fallen to exp(-1/2) of its peak.
        for center, peak in zip(centers, (I1, I2)):
            width_height = peak * np.exp(-0.5)
            ax.annotate(
                "",
                xy=(center + w0, width_height),
                xytext=(center, width_height),
                arrowprops=dict(
                    arrowstyle="|-|",
                    color=marker_color,
                    linewidth=1.0,
                    mutation_scale=6,
                    shrinkA=0,
                    shrinkB=0,
                    alpha=marker_alpha,
                ),
                zorder=5,
            )
            ax.text(
                center + w0 / 2,
                width_height - 0.055 * max_intensity,
                r"$w_0$",
                ha="center",
                va="top",
                color=marker_color,
                fontsize=9.5,
            )
    else:
        # For unresolved sources, mark the intensities of the two sources
        for center, peak in zip(centers, (I1, I2)):
            ax.plot(
                [center, center],
                [0, peak],
                color=marker_color,
                linewidth=0.9,
                linestyle=":",
                alpha=0.6,
                zorder=4,
            )
            lable = r"$I_1$" if center==centers[0] else r"$I_2$"
            pos_testo = center + 0.4 * (-1 if center==centers[0] else 1)  # Adjust text position based on center
            ax.text(
                pos_testo,
                peak/3,
                lable,
                ha="center",
                va="bottom",
                color=marker_color,
                fontsize=11,
            )


def plot_rayleigh_column(
    distance,
    I1=1.0,
    I2=1.0,
    w0=1.0,
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

    # Plotting Gaussian PSF for the 2D image
    # intensity1_2d = gaussian_psf(X, Y, -distance / 2, 0, I1, w0)
    # intensity2_2d = gaussian_psf(X, Y,  distance / 2, 0, I2, w0)

    # Plotting the Airy disk instead of Gaussian PSF for the 2D image
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

    # Plotting Gaussian PSF for the 1D profile
    intensity1_1d = gaussian_psf(x_1d, 0, -distance / 2, 0, I1, w0)
    intensity2_1d = gaussian_psf(x_1d, 0,  distance / 2, 0, I2, w0)

    # Plotting the Airy disk instead of Gaussian PSF for the 1D profile
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

    add_dimension_markers(ax2, distance, I1, I2, w0)

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
        ax2.set_ylim(
            0,
            max(
                np.max(total_intensity_1d + sum_offset) * 1.1,
                1.30 * max(I1, I2),
            ),
        )

    sns.despine(ax=ax2)
    plt.savefig(
        f"rayleigh_{title.replace(' ', '_').lower()}.png", dpi=300, bbox_inches="tight"
    )
    plt.show()


# --- Example Usage ---

# Equivalent Gaussian width of the Airy central lobe in the dimensionless
# coordinates used by airy_disk. Passing a Gaussian profile instead would return
# that Gaussian's standard deviation according to the same definition.
airy_equivalent_w0 = compute_w0(
    lambda radius: airy_disk(radius, 0, 0, 0, 1.0),
    max_radius=4.0,
)

# 1. Resolved with log_y=True to reveal the secondary peaks in the 1D plot
plot_rayleigh_column(
    distance=4.5,
    I1=1.0,
    I2=0.4,
    w0=airy_equivalent_w0,
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
    w0=airy_equivalent_w0,
    title="Unresolved",
    fig_width=5,
    bottom_ratio="60%",
    crop_percent=50,
    line_alpha=1.0,
    sum_offset=0.05,
    gamma=1,
    log_y=False,
)
