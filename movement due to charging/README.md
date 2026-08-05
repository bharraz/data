
## estimate_position.ipynb
Given an echoe'd pulse sequence that decays to 1/e amplitude after a total of N pi-times ($N_{\pi}$), I want to estimate the amount of shot-to-shot change in position needed to explain the decoherence.

Given:

- $w_0$ - beam waist
- $x$ - deviation from maximum beam intensity
- $\Omega_0$ - Max rabi frequency
- $N_{\pi}$ - Number of pi times until decoherence

I'll start with
$\Omega(x) = \Omega_0 \exp(-\frac{x^2}{w_0^2})$
For a small displacement:
$\Omega(x) \approx \Omega_0 (1 - \frac{x^2}{w_0^2})$
For a single pi-pulse of duration $t_\pi$
$\theta(x) = t_\pi \Omega(x) \approx \pi (1 - \frac{x^2}{w_0^2})$
$\delta \theta \approx \pi \frac{x^2}{w_0^2}$
The fractional error would be
$\frac{\delta \theta}{\pi} \approx  \frac{x^2}{w_0^2}$

So, for the total number of pi-pulses, the total fractional error would be:
$N_\pi\frac{x^2}{w_0^2}$
When the fractional error is 1, we can say that it's completely decohered, so
$\frac{x^2}{w_0^2} = \frac{1}{N_\pi}$
Is the condition we care about to estimate the position drift of the ion.
The calculations are in the python notebook