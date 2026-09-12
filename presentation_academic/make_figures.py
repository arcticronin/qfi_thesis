"""Generate presentation figures; does not invoke TeX or modify thesis assets.

The TFIM curve is independently reproduced from the Hamiltonian and settings
in NoiseAnalysis.tex, Project 9. Checks below compare it to the reported values.
"""
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / 'assets'
OUT.mkdir(exist_ok=True)
NAVY, WHITE, MUTED, TEAL, CORAL = '#111D2E', '#F5F3EE', '#ACB8C9', '#56D6BE', '#FF967D'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
    'text.usetex': False, 'figure.facecolor': NAVY, 'axes.facecolor': NAVY,
    'axes.edgecolor': MUTED, 'axes.labelcolor': WHITE, 'text.color': WHITE,
    'xtick.color': MUTED, 'ytick.color': MUTED, 'pdf.fonttype': 42,
    'axes.spines.top': False, 'axes.spines.right': False})

def save(fig, name):
    fig.savefig(OUT / (name+'.pdf'), bbox_inches='tight', facecolor=NAVY)
    fig.savefig(OUT / (name+'.png'), bbox_inches='tight', facecolor=NAVY, dpi=170)
    plt.close(fig)

N, n = 6, 4
X, Z, I = np.array([[0., 1.], [1., 0.]]), np.diag([1., -1.]), np.eye(2)
def op(a, site):
    result = np.ones((1, 1))
    for j in range(N):
        result = np.kron(result, a if j == site else I)
    return result
xs, zs = [op(X, j) for j in range(N)], [op(Z, j) for j in range(N)]
V = -sum(xs)
H0 = -sum(zs[j] @ zs[(j+1) % N] for j in range(N))

def reduce(a):
    return np.trace(a.reshape(2**n, 2**(N-n), 2**n, 2**(N-n)), axis1=1, axis2=3)

def qfi(rho, drho):
    p, u = eigh(rho)
    den = p[:, None] + p[None, :]
    d = u.T @ drho @ u
    use = den > 1e-10
    return 2*np.sum(np.abs(d[use])**2 / den[use])

fields = np.linspace(.1, 2.5, 60)
ground, thermal, depol = [], [], []
for h in fields:
    e, u = eigh(H0 + h*V)
    v = u.T @ V @ u
    psi = u[:, 0]
    dpsi = u[:, 1:] @ (v[1:, 0] / (e[0]-e[1:]))
    rg = reduce(np.outer(psi, psi))
    dg = reduce(np.outer(dpsi, psi) + np.outer(psi, dpsi))
    ground.append(qfi(rg, dg))
    depol.append(qfi(.9*rg + .1*np.eye(2**n)/2**n, .9*dg))
    beta = 2.
    p = np.exp(-beta*(e-e[0])); p /= p.sum()
    gaps = e[:, None] - e[None, :]
    coef = np.empty_like(gaps)
    regular = np.abs(gaps) > 1e-9
    np.divide(p[:, None]-p[None, :], gaps, out=coef, where=regular)
    coef[~regular] = (-beta*(p[:, None]+p[None, :])/2)[~regular]
    dt = coef*v
    np.fill_diagonal(dt, -beta*p*(np.diag(v)-p@np.diag(v)))
    thermal.append(qfi(reduce((u*p)@u.T), reduce(u@dt@u.T)))
ground, thermal, depol = map(np.asarray, (ground, thermal, depol))
assert abs(ground.max()-3.926) < .002
assert abs(thermal.max()-2.607) < .002
assert abs(depol.max()-3.419) < .002
assert thermal.max() < ground.max()
assert np.all(thermal[(fields >= 1.2) & (fields <= 2)] > ground[(fields >= 1.2) & (fields <= 2)])
np.savetxt(OUT/'tfim_curves.csv', np.column_stack((fields, ground, thermal, depol)),
    delimiter=',', header='h_over_J,ground_local_qfi,thermal_beta2_local_qfi,depolarized_P01_local_qfi', comments='')
fig, ax = plt.subplots(figsize=(8.3, 4.3))
ax.plot(fields, ground, color=WHITE, lw=2.5, label='Ground state')
ax.plot(fields, thermal, color=TEAL, lw=3, label=r'Gibbs state ($\beta J=2$)')
ax.fill_between(fields, ground, thermal, where=thermal>ground, color=TEAL, alpha=.13, interpolate=True)
ax.set(xlabel=r'Magnetic field $h_x/J$', ylabel=r'Local QFI (with $J=1$)', xlim=(.1, 2.0), ylim=(0, 4.4))
ax.grid(axis='y', color=MUTED, alpha=.13)
ax.legend(frameon=False, fontsize=11, loc='upper right')
ax.annotate('Higher off-peak QFI', xy=(1.5, np.interp(1.5, fields, thermal)), xytext=(1.22, 3.2),
    color=TEAL, fontsize=11, arrowprops={'arrowstyle':'-', 'color':TEAL})
fig.tight_layout()
save(fig, 'thermal_advantage')

fig, axes = plt.subplots(1, 2, figsize=(9, 2.7))
x = np.linspace(-4, 4, 400)
for ax, shift, title in zip(axes, [.3, 1.5], ['Small statistical change', 'Large statistical change']):
    for mean, col in [(0., WHITE), (shift, TEAL)]:
        y = np.exp(-(x-mean)**2/2)
        ax.plot(x, y, color=col, lw=2.8)
        ax.fill_between(x, 0, y, color=col, alpha=.08)
    ax.set_title(title, fontsize=13, pad=12)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel('Measurement outcome', fontsize=11)
    ax.spines['left'].set_visible(False)
fig.tight_layout(w_pad=3)
save(fig, 'distinguishability')
print('TFIM verification: ground peak %.6f; thermal peak %.6f; advantage at %d/60 fields.' %
      (ground.max(), thermal.max(), np.count_nonzero(thermal>ground)))

print('Displayed off-peak point h/J=1.5: ground %.4f, thermal %.4f' % (np.interp(1.5, fields, ground), np.interp(1.5, fields, thermal)))
