import matplotlib.pyplot as plt
import polars as pl
import math

model_names = ["196608", "393216", "3145728", "6291456"]

plt.ylabel("Test Loss")
plt.xlabel("Compute (PF-days)")
plt.xscale('log', base=10) 

for i in model_names:
    df = pl.read_csv(f"{i}.csv")
    plt.plot((df.select("Step").to_numpy() * int(i) * 2**20 * 6)/(10**15 * 24 * 3600), df.select(f"{i} - loss"), label=f"{int(i)/1000000:.2f}M", alpha=0.5)
plt.legend()
plt.show()