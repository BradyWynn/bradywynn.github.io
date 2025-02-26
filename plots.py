import matplotlib.pyplot as plt
import polars as pl
import math
import numpy as np

model_names = ["196608", "393216", "3145728", "6291456"]

# plot #1
# plt.ylabel("Test Loss")
# plt.xlabel("Compute (PF-days)")
# plt.xscale('log', base=10) 
# plt.grid()

# for i in model_names:
#     df = pl.read_csv(f"{i}.csv")
#     plt.plot((df.select("Step").to_numpy() * int(i) * 2**20 * 6)/(10**15 * 24 * 3600), df.select(f"{i} - loss"), label=f"{int(i)/1000000:.2f}M", alpha=0.5)
# plt.legend()
# plt.savefig("Figure_1.png")

# plot #2
# import matplotlib.ticker as mticker
# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.set_ylabel("Test Loss")
# ax.set_xlabel("Parameters")
# # plt.grid()
# ax.set_xscale('log', base=10) 
# ax.set_yscale('log', base=10) 

# x = np.arange(10**5, 10**7, 10)
# y = (x/(2.9415246413*10**12))**(-0.0625374205751)
# ax.plot(x, y, linestyle="--", color="gray", label=r'$L=\left(N/2.942\cdot10^{12}\right)^{-0.0625}$')

# for i in model_names:
#     df = pl.read_csv(f"{i}.csv")
#     ax.scatter(int(i), df.select(f"{i} - loss")[-100:].to_numpy().mean())
# ax.legend()

# # Remove 10^0 label
# ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
# ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
# ax.tick_params(axis='y', which='both', labelsize=10)  # Adjust label size if needed

# fig.savefig("Figure_1.png")

# plot 3
import matplotlib.ticker as mticker
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_ylabel("Compression Ratio")
ax.set_xlabel("Parameters")
# plt.grid()
# ax.set_xscale('log', base=10) 
# ax.set_yscale('log', base=10) 

x = np.arange(10**5, 10**8, 100)
y = (x/(2.9415246413*10**12))**(-0.0625374205751)
y1 = 10 / (y * np.log2(np.e))
ax.plot(x, y1, linestyle="--", label=r'$\frac{10}{L\left(N\right)\log_{2}e}$')
y2 = (915/(((y * np.log2(np.e))/10) * 915 + ((x * 16)/(8*1024*1024))))
ax.plot(x, y2, linestyle="--")

# for i in model_names:
    # df = pl.read_csv(f"{i}.csv")
    # ax.scatter(int(i), df.select(f"{i} - loss")[-100:].to_numpy().mean())
# ax.legend()

# Remove 10^0 label
ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
ax.tick_params(axis='y', which='both', labelsize=10)  # Adjust label size if needed

fig.savefig("Figure_1.png")