import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

s1 = np.sin(2*np.pi*5*t)
s2 = np.sin(2*np.pi*10*t)

s_total = s1 + s2

plt.figure(figsize=(10,6))

plt.plot(t, s1, label="5 Hz Signal")
plt.plot(t, s2, label="10 Hz Signal")
plt.plot(t, s_total, label="Combined Signal", linestyle='--')

plt.title("Signal Visualization and Superposition")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()
