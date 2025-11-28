import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 5000)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title("sin(x)")
axs[0,0].grid()

axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title("cos(x)")
axs[0,1].grid()

y_tan = np.tan(x)
y_tan[np.abs(y_tan) > 10] = np.nan
axs[1,0].plot(x, y_tan)
axs[1,0].set_title("tan(x)")
axs[1,0].set_ylim(-10,10)
axs[1,0].grid()

y_sinh = np.sinh(x)
y_sinh[np.abs(y_sinh) > 50] = np.nan
axs[1,1].plot(x, y_sinh)
axs[1,1].set_title("sinh(x)")
axs[1,1].grid()

plt.tight_layout()
plt.show()
