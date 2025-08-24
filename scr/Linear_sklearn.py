import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Đọc dữ liệu
df = pd.read_csv('C:\\Users\\ASUS\Desktop\\LinearRegression\\Data\\height_weight.csv')

X = df[['Height(cm)']]   # phải để dạng 2D
y = df['Weight(kg)']


model = linear_model.LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R² score: %.2f" % r2_score(y_test, y_pred)) # mức độ giải thích
print("MSE: %.2f" % mean_squared_error(y_test, y_pred)) #Sai số mô hình

plt.scatter(X_test, y_test, color="red", label="Thực tế")
plt.plot(X_test, y_pred, color="blue", linewidth=2, label="Dự đoán")
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Cân nặng (kg)")
plt.legend()
plt.show()