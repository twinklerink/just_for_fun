# Existence & Uniqueness

- [ ] md notes
- [ ] matplotlib vector field

简谐运动的微分方程：

$$ m\ddot{x} + kx = 0 $$

考虑阻力(阻尼振动，阻力常数$\mu$与速率成正比)：

$$ m\ddot{x} - \mu\dot{x}+ kx = 0 $$

单摆的运动方程：

$$ l\ddot{\theta} + g\sin(\theta) = 0$$

考虑阻力(阻尼振动，阻力常数$\mu$与速率成正比)：

$$ l\ddot{\theta} - \mu\dot{\theta}+ g\sin(\theta) = 0 $$

## 思路

- 纵轴为一阶导
- 横轴为原函数

## 简谐运动(无阻力)

$m\ddot{x} + kx = 0$用角频率 $\omega = \sqrt{\frac{k}{m}}$ 表示为：

$$
\ddot{x} + \omega^2x = 0
$$

又有

$$
\ddot{x} = \frac{\mathrm{d}}{\mathrm{d}t}\dot{x}
$$

这是一个

$
\begin{pmatrix}
    \ddot{x} \\
    \dot{x}
\end{pmatrix}
=
\begin{pmatrix}
    \ddot{x} \\
    \dot{x}
\end{pmatrix}$
$
