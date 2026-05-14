import numpy as np
import matplotlib.pyplot as plt

def sample_phonon_numbers(n_bar, num_samples):
    Z = 1 / (1 - np.exp(-1 / n_bar))  # Partition function
    n_max = int(10 * n_bar)            # Truncation limit
    n_values = np.arange(0, n_max + 1) # [0, 1, ..., n_max]
    
    # PMF and CDF
    pmf = np.exp(-n_values / n_bar) / Z
    cdf = np.cumsum(pmf)
    cdf /= cdf[-1]  # Normalize to 1
    
    # Inverse transform sampling - 
    u = np.random.rand(num_samples)
    samples = np.searchsorted(cdf, u)
    return samples

def plot_ns(ns, nbar):
    # Plot histogram of different n values
    plt.figure(figsize=(10, 6))
    plt.hist(ns, bins=100, density=True, alpha=0.7, edgecolor='black')

    # Overlay theoretical distribution
    n_values = np.arange(0, np.max(ns)+1)
    pmf = np.exp(-n_values / nbar) * (1 - np.exp(-1 / nbar))
    plt.plot(n_values, pmf, 'r-', linewidth=2, label='Theoretical PMF')

    plt.xlabel('Phonon Number $n_m$', fontsize=12)
    plt.ylabel('Probability Density', fontsize=12)
    plt.title(f'Phonon Number Distribution ($\\bar{{n}}_m = {nbar}$)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()

# Time-averaged Rabi frequency formula
def rabi_correction(n_ms, mode_freqs, bs, omega_0):
    hbar = 6.63e-34
    mass = 2.84e-25
    waist = 2e-6
    sum = 0
    for i, wm in enumerate(mode_freqs):
        sum += bs[i]**2 * n_ms[i] / wm
    return (-1 * (1/ waist**2) * (hbar / mass)) * sum

# Single ion in single mode
omega_0 = .1667e6
bim = [1/np.sqrt(7)]
mode_freqs = [290.83e3 * 2*np.pi]

nbar = 500
ns = sample_phonon_numbers(nbar, 2000)
print(f"Sampled mean: {np.mean(ns):.1f} (Theory: {nbar})")
print(f"Sampled variance: {np.var(ns):.1f} (Theory: {nbar**2 + nbar:.1f})")
plot_ns(ns, nbar)
omegas = list(map(lambda n : rabi_correction([n], mode_freqs, bim, omega_0), ns))
# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(omegas, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Rabi Frequency Correction', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.title(f'Rabi Frequency Corrections ($\\bar{{n}} = {nbar}$)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# plot_ns(ns, nbar)