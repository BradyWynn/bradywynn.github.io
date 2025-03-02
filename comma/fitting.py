import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func_powerlaw(x, a, b):
    return (x / a)**b

x = [196608, 393216, 3145728, 6291456, 9437184]
y = [2.852495665550232, 2.6331967282295228, 2.385006549358368, 2.254081246852875, 2.2038679099082947]

popt, pcov = curve_fit(func_powerlaw, x, y, p0 = np.asarray([2.942*10**12,-0.0625]))

print(popt[1])
# print(popt)
# print("\n")
# print(pcov)

# interval = np.arange(x[0]-100000, x[-1], 10000)

# plt.plot(interval, (interval/popt[0])**popt[1])

# plt.scatter(x, y)
# plt.show()