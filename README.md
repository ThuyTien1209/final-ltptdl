# Đồ án môn học - Thuật toán A-Star và Dijkstra 
> **Giảng viên hướng dẫn:** TS. Nguyễn An Tế  
> **Nhóm thực hiện:** *Nhóm 10*  
> **Ngôn ngữ:** Python (Jupyter Notebook, OOP)  
> **Học phần:** Lập trình phân tích dữ liệu

---

## Giới thiệu

Đồ án này được thực hiện nhằm **ứng dụng hai thuật toán kinh điển** là **A\*** và **Dijkstra** – để **giải quyết bài toán tìm đường tối ưu** trong hai bối cảnh khác nhau:  
1. **Robot hút bụi di chuyển trong ma trận (A\*)**.  
2. **Tìm đường ngắn nhất trên đồ thị có trọng số (Dijkstra)**.

---

## 1. Thuật toán A\* – Robot hút bụi

### Mục tiêu:
Cài đặt và mô phỏng **thuật toán A\*** để điều khiển robot hút bụi trong **ma trận Aₘ,ₙ**, tối ưu hóa tổng chi phí khi làm sạch toàn bộ ô **dirty (D)**:

### Mô tả bài toán:
- Ma trận gồm các ô:  
  - **F (free)** – ô trống.  
  - **D (dirty)** – ô bẩn.  
  - **C (clean)** – ô sạch.  
- Robot có thể:  
  - **Move** đến một trong **8 ô lân cận** (chi phí = 1).  
  - **Suck** để làm sạch ô hiện tại.  
- Sau mỗi hành động, **tất cả các ô dirty còn lại** tăng thêm **1 đơn vị chi phí hút bụi**.

### Yêu cầu:
- Cho phép người dùng:  
  - Nhập kích thước ma trận \( A_{m,n} \).  
  - Chọn số lượng và vị trí ngẫu nhiên của các ô **dirty**.  
- Áp dụng **thuật toán A\*** để tìm lộ trình tối ưu cho robot.  
- Hiển thị kết quả trực quan:  
  - **Lộ trình di chuyển** (Move/Suck).  
  - **Tổng chi phí thực hiện**.  

---

## 2. Thuật toán Dijkstra

### Mục tiêu:
Xây dựng chương trình minh họa **thuật toán Dijkstra** để tìm đường đi ngắn nhất giữa hai đỉnh bất kỳ trong **đồ thị vô hướng có trọng số dương**.

### Yêu cầu:
- Đọc dữ liệu đồ thị từ file `Graph.csv`, định dạng: (v_from, v_to, weight)
- Viết chương trình Python hướng đối tượng để:
  - Biểu diễn đồ thị bằng **danh sách cạnh liên thuộc**.  
  - Áp dụng **thuật toán Dijkstra** để tìm **đường đi ngắn nhất** và **độ dài đường đi**.
  - Hiển thị kết quả trực quan (đường đi và tổng trọng số).  

---

## Lời cảm ơn
Nhóm xin gửi lời cảm ơn chân thành đến **TS. Nguyễn An Tế** – giảng viên hướng dẫn môn *Lập trình phân tích dữ liệu*, đã tận tình hướng dẫn và hỗ trợ trong suốt quá trình học tập và thực hiện đồ án.  
