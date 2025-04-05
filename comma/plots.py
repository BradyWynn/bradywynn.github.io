import matplotlib.pyplot as plt
import polars as pl
import math
import numpy as np

model_names = ["old", "new"]

plt.ylabel("Train Loss")
plt.xlabel("Steps")

for i in model_names:
    df = pl.read_csv(f"comma/runs/{i}.csv")
    plt.plot(df.select("Step").to_numpy(), df.select(f"{i} - loss"), label=i, alpha=0.5)

plt.ylim(2, 7)
plt.xlim(0, 8000)
plt.grid()
plt.legend()
plt.savefig("Figure_1.png")

# model_names = ["196608", "393216", "3145728", "6291456", "9437184"]

# plot #1
# import matplotlib.ticker as mticker
# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.set_ylabel("Train Loss")
# ax.set_xlabel("Compute (PF-days)")
# ax.set_xscale('log', base=10) 
# ax.set_yscale('log', base=10) 
# # ax.grid()

# for i in model_names:
#     df = pl.read_csv(f"comma/runs/{i}.csv")
#     ax.plot((df.select("Step").to_numpy() * int(i) * 2**20 * 6)/(10**15 * 24 * 3600), df.select(f"{i} - loss"), label=f"{int(i)/1000000:.2f}M", alpha=0.5)

# ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
# ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
# ax.tick_params(axis='y', which='both', labelsize=10)  # Adjust label size if needed

# ax.legend()
# fig.savefig("train_loss_vs_compute.png")

# plot #2
# import matplotlib.ticker as mticker
# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.set_ylabel("Train Loss")
# ax.set_xlabel("Parameters")
# # plt.grid()
# ax.set_xscale('log', base=10) 
# ax.set_yscale('log', base=10) 

# x = np.arange(10**5, 2*10**7, 100)
# y = (x/(2.65293642*10**12))**(-0.0629678928294751)
# ax.plot(x, y, linestyle="--", color="gray", label=r'$L=\left(N/2.653\cdot10^{12}\right)^{-0.0630}$')

# for i in model_names:
#     df = pl.read_csv(f"comma/runs/{i}.csv")
#     ax.scatter(int(i), df.select(f"{i} - loss")[-100:].to_numpy().mean())
#     print(i, df.select(f"{i} - loss")[-100:].to_numpy().mean())
# ax.legend()

# # Remove 10^0 label
# ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
# ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
# ax.tick_params(axis='y', which='both', labelsize=10)  # Adjust label size if needed

# fig.savefig("Figure_1.png")

# plot 3
# import matplotlib.ticker as mticker
# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.set_ylabel("Compression Ratio")
# ax.set_xlabel("Parameters")
# # plt.grid()
# # ax.set_xscale('log', base=10) 
# # ax.set_yscale('log', base=10) 

# x = np.arange(10**5, 10**8, 100, dtype=np.int64)
# y = (x/(2.65293642*10**12))**(-0.0629678928294751)
# y1 = 10 / (y * np.log2(np.e))
# ax.plot(x, y1, linestyle="-", label="no model size")
# y2 = (915/(((y * np.log2(np.e))/10) * 915 + ((x * 4)/(8*1024*1024))))
# ax.plot(x, y2, linestyle="-", label="4 bit")
# y2 = (915/(((y * np.log2(np.e))/10) * 915 + ((x * 8)/(8*1024*1024))))
# ax.plot(x, y2, linestyle="-", label="8 bit")
# y2 = (915/(((y * np.log2(np.e))/10) * 915 + ((x * 16)/(8*1024*1024))))
# ax.plot(x, y2, linestyle="-", label="16 bit")
# y2 = (915/(((y * np.log2(np.e))/10) * 915 + ((x * 32)/(8*1024*1024))))
# ax.plot(x, y2, linestyle="-", label="32 bit")

# # for i in model_names:
#     # df = pl.read_csv(f"{i}.csv")
#     # ax.scatter(int(i), df.select(f"{i} - loss")[-100:].to_numpy().mean())
# ax.legend()

# # Remove 10^0 label
# ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
# ax.yaxis.set_minor_formatter(mticker.ScalarFormatter())
# ax.tick_params(axis='y', which='both', labelsize=10)  # Adjust label size if needed

# fig.savefig("Figure_1.png")