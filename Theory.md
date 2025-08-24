# Lý thuyết Hồi quy Tuyến tính

## 1. Hồi quy tuyến tính là gì?
Hồi quy tuyến tính là một phương pháp trong học máy dùng để mô hình hóa mối quan hệ giữa **biến độc lập** (input) và **biến phụ thuộc** (output).

Ví dụ: dự đoán cân nặng (kg) dựa trên chiều cao (cm).

## 2. Công thức mô hình
Mô hình hồi quy tuyến tính có dạng:

![alt text](image.png)

- \( w_0 \): hệ số chặn (bias / intercept)  
- \( w_1 \): hệ số góc (slope / weight)  
- \( x \): biến đầu vào  
- \( y^\): giá trị dự đoán  

## 3. Hàm mất mát (Loss function)
Để huấn luyện mô hình, ta tối thiểu hóa hàm mất mát:

![alt text](image-2.png)

Trong đó:
- \( y_i \): giá trị thực tế  
- \( y^ \): giá trị dự đoán  
- \( N \): số lượng mẫu  

## 4. Chính quy hóa (Regularization)
Để tránh overfitting, thêm số hạng ràng buộc:

- **L1 (Lasso):**
![alt text](image-3.png)

- **L2 (Ridge):**
![alt text](image-4.png)

## 5. Đánh giá mô hình
Một số chỉ số:
- **MSE (Mean Squared Error):** sai số trung bình bình phương.  
- **R² score:** mức độ mô hình giải thích được biến đầu ra.  

## 6. Trực quan hóa
Vẽ dữ liệu thực tế (scatter plot) và đường hồi quy để trực quan mô hình.