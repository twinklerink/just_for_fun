import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.stats import binom

# Matplotlib Configration
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
bb = "#69c2ec" # bilibili blue
bp = "#ed91ab" # bilibili pink

# Basic constants
num_of_coin = 60
trial_number = 1000
heads_prob = 0.5

# Derived constants
order = np.arange(1, trial_number + 1)
sample = binom.rvs(num_of_coin, heads_prob, size=trial_number)
expec = num_of_coin * heads_prob
var = num_of_coin * heads_prob * (1 - heads_prob)
mean = np.cumsum(sample) / (np.arange(1, trial_number + 1))
sample_var = [np.var(sample[0:i + 2], ddof=1) for i in range(len(sample) - 1)]

# Figure Initialization
fig, ax = plt.subplots(2, 2, figsize=(9, 9))
fig.patch.set_facecolor(bp)
fig.suptitle(r'二项分布模拟 X ~ B(60, 0.5)', fontsize=16)

# Plot Sample Dot Distribution
dot_dist = ax.flat[0].scatter([], [], marker=".",  c=bb, s=1)
ax.flat[0].set_title("样本点分布")
ax.flat[0].grid(True, linewidth=0.5, alpha=0.5)
ax.flat[0].set_yticks(np.arange(0, num_of_coin, 6))
ax.flat[0].set_xlabel(r'试验次数N/次')
ax.flat[0].set_ylabel(r'成功事件数Y/件')

# Sample Distribution (Histogram)
ax.flat[1].hist([], bins=num_of_coin, range=(0, num_of_coin), color=bb, edgecolor=bp)
ax.flat[1].set_title("样本分布直方图")
ax.flat[1].set_xlim(0, num_of_coin)
ax.flat[1].set_ylim(0, trial_number // 5)
ax.flat[1].set_xlabel(r'成功事件数Y/件')
ax.flat[1].set_ylabel(r'出现次数/次')

# Sample Dot Distribution
mean_curve, = ax.flat[2].plot([], [], label="样本均值", c=bb)
mean_line, = ax.flat[2].plot([], [], linewidth=1, label=f"总体期望 = {expec}", c=bp)
ax.flat[2].set_title(r"样本均值变化 ($\lim_{N\to\infty} \bar{X} = \mu$)")
ax.flat[2].set_xlabel(r'试验次数N/次')
ax.flat[2].set_ylabel(r'成功事件均值数$\bar{X}$/件')
ax.flat[2].legend()

# Sample Variance Evolution
var_curve, = ax.flat[3].plot([], [], color=bb, label="样本方差")
var_line, = ax.flat[3].plot([], [], linewidth=1, 
                           label=f"总体方差 = {var}", c=bp)
ax.flat[3].set_title(r"样本方差变化 ($\lim_{N\to\infty} s^2 = \sigma^2$)")
ax.flat[3].set_xlabel(r'试验次数N/次')
ax.flat[3].set_ylabel(r'成功事件方差$s^2$')
ax.flat[3].legend()


# Animation Part

x_data = []
y_data = []
mean_data = []
var_data = []

def update(frame: int):
    x_data.append(frame + 1)
    y_data.append(sample[frame])
    if frame % 10 == 0:
        print(f"Render Process: {frame * 100 / trial_number} %")

    # Update Sample Dot Distribution

    dot_dist = ax.flat[0].scatter(x_data, y_data, marker=".",  c=bb, s=1)
    ax.flat[0].set_title("样本点分布")
    ax.flat[0].grid(True, linewidth=0.5, alpha=0.5)
    ax.flat[0].set_yticks(np.arange(0, num_of_coin, 6))
    

    # Update Sample Distribution (Histogram)

    ax.flat[1].clear()
    ax.flat[1].hist(y_data, bins=num_of_coin, range=(0, num_of_coin), color=bb, edgecolor=bp)
    ax.flat[1].set_title("样本分布直方图")
    ax.flat[1].set_xlabel(r'成功事件数Y/件')
    ax.flat[1].set_ylabel(r'出现次数/次')


    # Update Sample Mean Evolution
    mean_data.append(np.mean(y_data))
    mean_curve, = ax.flat[2].plot(x_data, mean_data, label="样本均值", c=bb)
    mean_line, = ax.flat[2].plot(x_data, np.full_like(x_data, expec), linewidth=1, label=f"总体期望 = {expec}", c=bp)
    ax.flat[2].set_title(r"样本均值变化 ($\lim_{N\to\infty} \bar{X} = \mu, $其中$\mu = np$)")


    # Update Sample Variance Evolution
    
    if frame > 0:
        var_data.append(np.var(y_data, ddof=1))
        var_curve, = ax.flat[3].plot(x_data[2:], var_data, color=bb, label="样本方差")
        var_line, = ax.flat[3].plot(x_data, np.full_like(x_data, var), linewidth=1, label=f"总体方差 = {var}", c=bp)
        ax.flat[3].set_title(r"样本方差变化 ($\lim_{N\to\infty} s^2 = \sigma^2, $其中$\sigma^2 = np(1 - p)$)")
        

        return dot_dist, mean_line, mean_curve, var_line, var_curve
    else:
        return dot_dist, mean_line, mean_curve
    
    

fig.tight_layout()
anim = FuncAnimation(fig, update, frames=trial_number, interval=50)
# anim.save("binom_dist.mp4", writer="ffmpeg", fps=30, dpi=400)
plt.show()