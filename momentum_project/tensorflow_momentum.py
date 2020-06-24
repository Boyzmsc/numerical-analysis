import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

class TensorflowMomentum:
    def __init__(self, lr, m):
        self.lr = lr
        self.m = m

    # 학습률 수정
    def setLr(self, newLr):
        self.lr = newLr

    # 모멘텀 변수 수정
    def setM(self, newM):
        self.m = newM

    def getLr(self):
        return self.lr

    def getM(self):
        return self.m

    def train(self, loss):
        optimizer = tf.train.MomentumOptimizer(learning_rate=self.lr, momentum=self.m)
        train = optimizer.minimize(loss)
        return train