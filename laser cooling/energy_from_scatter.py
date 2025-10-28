import numpy as np 

n_cycles = 200 
avg_photons_per_cycle = 3 
n_photons = n_cycles * avg_photons_per_cycle 
hbar = 1.054571817e-34     # J⋅s 
wavelength = 369.5e-09 
axial_freq = 125e03 * 2 * np.pi 
amu = 171
m= amu * 1.66053906660e-27 # Mass in kg 
k = (2 * np.pi) / wavelength 

# Calculate heating during SBC due to scattering:
expected_energy = (hbar**2 * k**2) / (6 * m) # J , isotropic scattering
expected_nbar = expected_energy / (hbar * axial_freq) 

print(f"expected energy and motional quanta due to {n_cycles} pumping cycles at axial frequency {axial_freq / (2 * np.pi)} Hz") 
print(expected_energy * n_photons) 
print(expected_nbar * n_photons) 

# Calculate heating during SBC not due to scattering
pumping_duration=9e-03 # in ms 
pi_time = 3e-03 # in ms 
print(f"Expected time spent doing pumping with pi time {pi_time} and pumping duration {pumping_duration} in ms") 
exp_duration = (pi_time + pumping_duration) * n_cycles 
print(exp_duration) 
heating_rate = 22.5 # q / ms 
print(f"Expected heat due to heating rate of {heating_rate} q / ms for {n_cycles} pumping cycles, each taking {pumping_duration} ms") 
print(exp_duration * heating_rate) 