from momentum import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 2차원 로젠브록 함수
def f(x, y):
    return (1 - x)**2 + 100.0 * (y - x**2)**2

# 2차원 로젠브록 함수의 도함수
def g(x, y):
    return np.array((2.0 * (x - 1) - 400.0 * x * (y - x**2), 200.0 * (y - x**2)))

# -------------------------------------------------------------------------

fig = plt.figure()
fig.clf()
ax = fig.add_subplot(1, 2, 1, projection='3d')

s = 0.05
xx = np.arange(-2.0, 2.0 + s, s)
yy = np.arange(-1.0, 3.0 + s, s)
X, Y = np.meshgrid(xx, yy)
Z = f(X, Y)

ax.plot_surface(X,Y,Z,rstride = 5, cstride = 5, cmap = 'jet', alpha = .5, edgecolor = 'none' )

# 모멘텀 객체 생성
m = Momentum(-1, -1, 0.001, 100000, 0.05, 0.8)
m_w0 = [] # w0를 담을 list
m_w1 = [] # w1를 담을 list
m_z = []  # z를 담을 list

for i in range(1, m.getSize()):
    gx = g(m.getW()[0], m.getW()[1])
    m.updateV(gx)
    m_w0.append(m.getW()[0])
    m_w1.append(m.getW()[1])
    m_z.append(f(m.getW()[0],m.getW()[1]))
    if max(np.absolute(gx)) < m.getEps():
        break
    m.updateW()

print("< Momentum >")
print("반복 수 : {0}".format(i))
print("W = [{0:.6f}, {1:.6f}]".format(m.getW()[0], m.getW()[1]))
print("dMSE = [{0:.6f}, {1:.6f}]".format(gx[0], gx[1]))

ax.plot(m_w0,m_w1,m_z,color = 'k', marker = '.', alpha = .9, linewidth= 1, markersize = 3)
ax.set_xlim([-2, 2])
ax.set_ylim([-1, 3])
ax.set_zlim([0, 2500])
ax.set_xlabel("x")
ax.set_ylabel("y")

# -------------------------------------------------------------------------

bx = fig.add_subplot(1, 2, 2, projection='3d')

s = 0.05
xx = np.arange(-2.0, 2.0 + s, s)
yy = np.arange(-1.0, 3.0 + s, s)
X, Y = np.meshgrid(xx, yy)
Z = f(X, Y)

bx.plot_surface(X,Y,Z,rstride = 5, cstride = 5, cmap = 'jet', alpha = .5, edgecolor = 'none' )

# 경사하강법 객체 생성
gd = GD(-1, -1, 0.001, 100000, 0.05)
gd_w0 = [] # w0를 담을 list
gd_w1 = [] # w1를 담을 list
gd_z = []  # z를 담을 list

for i in range(1, gd.getSize()):
    gx = g(gd.getW()[0], gd.getW()[1])
    gd_w0.append(gd.getW()[0])
    gd_w1.append(gd.getW()[1])
    gd_z.append(f(gd.getW()[0], gd.getW()[1]))
    if max(np.absolute(gx)) < gd.getEps():
        break
    gd.update(gx)

print('- ' * 30)
print("< GD >")
print("반복 수 : {0}".format(i))
print("W : [{0:.6f}, {1:.6f}]".format(gd.getW()[0], gd.getW()[1]))
print("dMSE : [{0:.6f}, {1:.6f}]".format(gx[0], gx[1]))

bx.plot(gd_w0,gd_w1,gd_z,color = 'k', marker = '.', alpha = .9, linewidth= 1, markersize = 3)
bx.set_xlim([-2, 2])
bx.set_ylim([-1, 3])
bx.set_zlim([0, 2500])
bx.set_xlabel("x")
bx.set_ylabel("y")
plt.show()