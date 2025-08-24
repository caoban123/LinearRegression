# 📊 Hồi quy tuyến tính (Linear Regression)

Dự án này triển khai **hồi quy tuyến tính** theo chương 7 trong tài liệu học máy, bao gồm:
- Mô hình hồi quy tuyến tính
- Hàm mất mát (Mean Squared Error)
- Thêm số hạng regularization (Ridge, Lasso)
- Kỹ thuật đánh giá mô hình bằng K-Fold Cross Validation

---

## 📖 1. Giới thiệu

Hồi quy tuyến tính được dùng để mô hình hóa mối quan hệ tuyến tính giữa:
- Biến độc lập (features) `X`
- Biến phụ thuộc (target) `y`

Mô hình:

y ≈ ŷ = w1x1 + w2x2 + ... + wd*xd + b


---

## ⚖️ 2. Hàm mất mát

Hàm mất mát được sử dụng là **Mean Squared Error (MSE):**

J(w, b) = (1/N) * Σ (y_i - ŷ_i)^


---

## 🛠️ 3. Regularization

Để tránh overfitting, thêm số hạng phạt:

- **Ridge Regression (L2):**

J(w, b) = (1/N) * Σ (y_i - ŷ_i)^2 + λ * Σ (w_j^2)


- **Lasso Regression (L1):**


---

## 🔁 4. Đánh giá mô hình

Sử dụng **K-Fold Cross Validation**:
- Chia dữ liệu thành `K` phần
- Lặp `K` lần, mỗi lần dùng 1 phần để kiểm tra, `K-1` phần còn lại để huấn luyện
- Trung bình hóa sai số → đánh giá mô hình ổn định hơn

---

pip install -r requirements.txt


