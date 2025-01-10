import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from collections import deque

# np.random.seed(19680801) #用于固定路径

def random_walk(num_steps, max_step=0.05):
    """返回一个随机游走3维数组(num_steps, 3)"""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk


def update_lines(num, walks, lines, deques):
    for line, walk, deque_ in zip(lines, walks, deques):
        # 添加当前步的点迹
        deque_.append(walk[num, :])

        # 如果队列长度超过 10，移除最早的点迹
        if len(deque_) > 10:
            deque_.popleft()

        # 将队列中的数据转换为数组
        points = np.array(deque_)

        # 更新路径
        line.set_data_3d(points.T)
    return lines

num_steps = 200  #  “生命周期：200帧 ” 我要给赛博宠物完整的一生😭
walks = [random_walk(num_steps) for _ in range(2)]

# 为每条路径创建一个 deque，用于存储最近的 10 个点迹
deques = [deque(maxlen=10) for _ in walks]

# 初始化图像界面
fig = plt.figure(num="赛博养殖场")
ax = fig.add_subplot(projection="3d")

# 初始化线条
lines = [ax.plot([], [], [], lw=2)[0] for _ in walks]

# 设置坐标轴属性
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')

# 创建动画
ani = animation.FuncAnimation(
    fig, update_lines, num_steps, fargs=(walks, lines, deques), interval=100, blit=True
)

plt.show()