from momentum import *
import numpy as np
import matplotlib.pyplot as plt

# 2차원 로젠브록 함수
def f(x, y):
    return (1 - x)**2 + 100.0 * (y - x**2)**2

# 2차원 로젠브록 함수의 도함수
def g(x, y):
    return np.array((2.0 * (x - 1) - 400.0 * x * (y - x**2), 200.0 * (y - x**2)))

# -------------------------------------------------------------------------
# 메인 - (1)
xx = np.linspace(-4, 4, 800)
yy = np.linspace(-3, 3, 600)
X, Y = np.meshgrid(xx, yy)
Z = f(X, Y)
s = 0.95  # 화살표 크기

levels = np.logspace(-1, 3, 10)

plt.figure(figsize=(12, 5))

ax = plt.subplot(1, 2, 1)
ax.contourf(X, Y, Z, alpha=0.2, levels=levels)
ax.contour(X, Y, Z, colors="gray", levels=levels, zorder=0)
ax.plot(1, 1, 'ro', markersize=5)

# 모멘텀 객체 생성
m = Momentum(-1, -1, 0.001, 100000, 0.05, 0.8)

for i in range(1, m.getSize()):
    gx = g(m.getW()[0], m.getW()[1])
    m.updateV(gx)
    ax.arrow(m.getW()[0], m.getW()[1],
             s * m.getV()[0], s * m.getV()[1],
             head_width=0.01, head_length=0.01, fc='k', ec='k', lw=2)
    if max(np.absolute(gx)) < m.getEps():
        break
    m.updateW()

print("< Momentum >")
print("반복 수 : {0}".format(i))
print("W = [{0:.6f}, {1:.6f}]".format(m.getW()[0], m.getW()[1]))
print("dMSE = [{0:.6f}, {1:.6f}]".format(gx[0], gx[1]))
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xticks(np.linspace(-3, 3, 7))
plt.yticks(np.linspace(-3, 3 ,7))
plt.xlabel("x")
plt.ylabel("y")
# -------------------------------------------------------------------------

bx = plt.subplot(1, 2, 2)
bx.contourf(X, Y, Z, alpha=0.2, levels=levels)
bx.contour(X, Y, Z, colors="green", levels=levels, zorder=0)
bx.plot(1, 1, 'ro', markersize=5)

# 경사하강법 객체 생성
gd = GD(-1, -1, 0.001, 100000, 0.05)

for i in range(1, gd.getSize()):
    gx = g(gd.getW()[0], gd.getW()[1])
    bx.arrow(gd.getW()[0], gd.getW()[1], -s * gd.getAlpha() * gx[0], -s * gd.getAlpha() * gx[1],
             head_width=0.01, head_length=0.01, fc='k', ec='k', lw=2)
    if max(np.absolute(gx)) < gd.getEps():
        break
    gd.update(gx)

print('- ' * 30)
print("< GD >")
print("반복 수 : {0}".format(i))
print("W : [{0:.6f}, {1:.6f}]".format(gd.getW()[0], gd.getW()[1]))
print("dMSE : [{0:.6f}, {1:.6f}]".format(gx[0], gx[1]))
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.xticks(np.linspace(-3, 3, 7))
plt.yticks(np.linspace(-3, 3 ,7))
plt.xlabel("x")
plt.ylabel("y")
plt.show()