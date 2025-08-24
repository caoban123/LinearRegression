import numpy as np
import matplotlib.pyplot as plt
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180,
183]]).T # height (cm), input data, each row is a data point
# weight (kg)
y = np.array([ 49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

ones = np.ones_like(X)

Xbar = np.concatenate((ones, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)

w = np.dot(np.linalg.pinv(A), b)
w_0, w_1 = w[0], w[1]

y1 = w_1*155 + w_0
y2 = w_1*160 + w_0

print('Input 155cm, true output 52kg, predicted output %.2fkg, accuracy %.2f%%.' %(y1, 100 - (abs(52 - y1) / 52 * 100)))
print('Input 160cm, true output 56kg, predicted output %.2fkg, accuracy %.2f%%.' %(y2, 100 - (abs(56 - y2) / 56 * 100)))

plt.scatter(X, y, c='r', label='Dữ liệu thực tế')
plt.plot(X, w_1*X + w_0, c='y', label='Đường hồi quy (dự đoán)')
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Cân nặng (kg)")
plt.legend()
plt.show()