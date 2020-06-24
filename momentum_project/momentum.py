import numpy as np

# 경사 하강법 구체화
class GD:
    def __init__(self, init_x, init_y, alpha, size, eps):
        self.alpha = alpha
        self.i_max = size
        self.eps = eps
        self.w_i = [init_x, init_y] # 초기 매개 변수

    # 학습률 수정
    def setAlpha(self, newAlpha):
        self.alpha = newAlpha

    # EPS 수정
    def setEps(self, newEps):
        self.eps = newEps

    def getAlpha(self):
        return self.alpha

    def getEps(self):
        return self.eps

    def getW(self):
        return self.w_i

    def getSize(self):
        return self.i_max

    # W(t+1) = W(t) - m*g(t)
    def update(self, dmse):
        self.w_i[0] = self.getW()[0] - self.getAlpha() * dmse[0]
        self.w_i[1] = self.getW()[1] - self.getAlpha() * dmse[1]


# 모멘텀 구체화
class Momentum():
    def __init__(self, init_x, init_y, alpha, size, eps, mu):
        self.alpha = alpha  # 학습률
        self.i_max = size  # 반복의 최대 수
        self.eps = eps  # 반복을 종료 기울기의 절대 값의 한계
        self.mu = mu  # 모멘텀 변수
        self.v = np.zeros(2)  # 속도
        self.w_i = [init_x, init_y] # 초기 매개 변수

    # 학습률 수정
    def setAlpha(self, newAlpha):
        self.alpha = newAlpha

    # EPS 수정
    def setEps(self, newEps):
        self.eps = newEps

    # 모멘텀 변수 수정
    def setMu(self, newMu):
        self.mu = newMu

    def getAlpha(self):
        return self.alpha

    def getEps(self):
        return self.eps

    def getMu(self):
        return self.mu

    def getW(self):
        return self.w_i

    def getV(self):
        return self.v

    def getSize(self):
        return self.i_max

    # V(t) = m*V(t-1) - a*g(x)
    def updateV(self, dmse):
        self.v[0] = (self.getMu() * self.getV()[0]) - (self.getAlpha() * dmse[0])
        self.v[1] = (self.getMu() * self.getV()[1]) - (self.getAlpha() * dmse[1])

    # W(t+1) = W(t) + V(t)
    def updateW(self):
        self.w_i[0] = self.getW()[0] + self.getV()[0]
        self.w_i[1] = self.getW()[1] + self.getV()[1]