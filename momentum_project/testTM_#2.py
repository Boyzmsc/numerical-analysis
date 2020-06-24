from tensorflow_momentum import TensorflowMomentum
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# tensorflow로 구현한 momentum이 잘 동작되는지 테스트

t_m = TensorflowMomentum(0.001,0.7)

num_points = 50
vectors_set = []
for i in np.arange(num_points):
    x = np.random.normal(2, 2) + 10
    y = x * 5 + (np.random.normal(0, 3)) * 2
    vectors_set.append([x, y])
x_data = np.array([v[0] for v in vectors_set])
y_data = np.array([v[1] for v in vectors_set])

plt.plot(x_data, y_data,'ro')
plt.ylim([0,100])
plt.xlim([0,25])
plt.xlabel('x')
plt.ylabel('y')

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b
loss = tf.reduce_mean(tf.square(y - y_data))

# TensorflowMomentum 클래스의 momentum 함수 호출
train = t_m.train(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

train_set = []
for step in np.arange(25):
    sess.run(train)
    train_set.append([sess.run(W), sess.run(b), sess.run(loss)])
    # print(step, sess.run(W), sess.run(b))
    # print(step, sess.run(loss))

    # plt.plot(x_data, y_data, 'ro')
    # plt.ylim([0, 100])
    # plt.xlim([0, 25])
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
    # plt.show()

W_data = np.array([t[0] for t in train_set])
v_data = np.array([t[1] for t in train_set])
Loss_data= np.array([t[2] for t in train_set])

# print('W_data = ', W_data)
# print('v_data = ', v_data)
print('Loss_data = ', Loss_data)

plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
plt.show()