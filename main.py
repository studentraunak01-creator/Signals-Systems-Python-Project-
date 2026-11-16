import numpy as np
import matplotlib.pyplot as plt

# Create graphs folder automatically
import os
os.makedirs("graphs", exist_ok=True)


# 1. Continuous-Time Sine Signal
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 5 * t)

plt.figure(figsize=(9, 5))
plt.plot(t, x)
plt.title("Continuous-Time Sine Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("graphs/01_continuous_sine.png")
plt.show()


# 2. Discrete-Time Sine Signal
n = np.arange(0, 20)
x = np.sin(2 * np.pi * 0.1 * n)

plt.figure(figsize=(9, 5))
plt.plot(n, x, "o-")
plt.title("Discrete-Time Sine Signal")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("graphs/02_discrete_sine.png")
plt.show()


# 3. Time Shifting
t = np.linspace(-2, 2, 1000)
x = np.sin(2 * np.pi * t)
x_shifted = np.sin(2 * np.pi * (t - 0.5))

plt.figure(figsize=(9, 5))
plt.plot(t, x, label="Original Signal")
plt.plot(t, x_shifted, label="Shifted Signal")
plt.title("Time Shifting of a Sine Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig("graphs/03_time_shifting.png")
plt.show()


# 4. Time Scaling
t = np.linspace(-2, 2, 1000)
x = np.sin(2 * np.pi * t)
x_compressed = np.sin(2 * np.pi * 2 * t)
x_expanded = np.sin(2 * np.pi * 0.5 * t)

plt.figure(figsize=(9, 5))
plt.plot(t, x, label="Original x(t)")
plt.plot(t, x_compressed, label="Compressed x(2t)")
plt.plot(t, x_expanded, label="Expanded x(0.5t)")
plt.title("Time Scaling of a Sine Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig("graphs/04_time_scaling.png")
plt.show()


# 5. Signal Addition
t = np.linspace(0, 1, 1000)
x1 = np.sin(2 * np.pi * 5 * t)
x2 = 0.5 * np.sin(2 * np.pi * 10 * t)
x_sum = x1 + x2

plt.figure(figsize=(9, 5))
plt.plot(t, x1, label="Signal 1")
plt.plot(t, x2, label="Signal 2")
plt.plot(t, x_sum, label="Added Signal")
plt.title("Addition of Two Signals")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig("graphs/05_signal_addition.png")
plt.show()


# 6. Signal Multiplication
t = np.linspace(0, 1, 1000)
x1 = np.sin(2 * np.pi * 5 * t)
x2 = np.cos(2 * np.pi * 5 * t)
x_product = x1 * x2

plt.figure(figsize=(9, 5))
plt.plot(t, x1, label="Signal 1")
plt.plot(t, x2, label="Signal 2")
plt.plot(t, x_product, label="Multiplied Signal")
plt.title("Multiplication of Two Signals")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig("graphs/06_signal_multiplication.png")
plt.show()


# 7. Sampling
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 5 * t)
sample_t = np.linspace(0, 1, 25)
sample_x = np.sin(2 * np.pi * 5 * sample_t)

plt.figure(figsize=(9, 5))
plt.plot(t, x, label="Continuous Signal")
plt.plot(sample_t, sample_x, "o", label="Sampled Signal")
plt.title("Sampling of a Continuous-Time Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig("graphs/07_sampling.png")
plt.show()


# 8. Convolution
x = np.array([1, 2, 1])
h = np.array([1, 1, 1])
y = np.convolve(x, h)
n = np.arange(len(y))

plt.figure(figsize=(9, 5))
plt.stem(n, y)
plt.title("Convolution of Two Discrete Signals")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("graphs/08_convolution.png")
plt.show()


# 9. Unit Impulse Signal
n = np.arange(-10, 11)
delta = np.where(n == 0, 1, 0)

plt.figure(figsize=(9, 5))
plt.stem(n, delta)
plt.title("Unit Impulse Signal")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("graphs/09_unit_impulse.png")
plt.show()


# 10. Signal Energy
n = np.arange(0, 10)
x = np.array([1, 2, 1, 3, 2, 1, 0, 2, 1, 0])
energy = np.sum(np.abs(x) ** 2)

plt.figure(figsize=(9, 5))
plt.stem(n, x)
plt.title("Signal Energy Analysis")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("graphs/10_signal_energy.png")
plt.show()


# 11. Even and Odd Signal Decomposition
n = np.arange(-5, 6)
x = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])

x_even = (x + x[::-1]) / 2
x_odd = (x - x[::-1]) / 2

plt.figure(figsize=(9, 5))
plt.stem(n, x_even)
plt.title("Even Part of a Signal")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("graphs/11_even_signal.png")
plt.show()

plt.figure(figsize=(9, 5))
plt.stem(n, x_odd)
plt.title("Odd Part of a Signal")
plt.xlabel("Sample Number (n)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("graphs/11_odd_signal.png")
plt.show()


# 12. Signal Attenuation
t = np.linspace(0, 2, 1000)
x = np.sin(2 * np.pi * 5 * t)
attenuated = np.exp(-2 * t) * x

plt.figure(figsize=(9, 5))
plt.plot(t, x, label="Original Signal")
plt.plot(t, attenuated, label="Attenuated Signal")
plt.title("Signal Attenuation")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig("graphs/12_signal_attenuation.png")
plt.show()


# 13. Cross-Correlation
x = np.array([1, 2, 3, 2, 1])
y = np.array([1, 1, 2, 1, 1])

correlation = np.correlate(x, y, mode="full")
lags = np.arange(-(len(y) - 1), len(x))

plt.figure(figsize=(9, 5))
plt.stem(lags, correlation)
plt.title("Cross-Correlation of Two Signals")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid(True)
plt.savefig("graphs/13_cross_correlation.png")
plt.show()

print("All 13 signal analysis graphs have been generated successfully!") 