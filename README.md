# Đồ án môn học - Thuật toán A-Star và Dijkstra 
> **Giảng viên hướng dẫn:** TS. Nguyễn An Tế  
> **Nhóm thực hiện:** *Nhóm 10*  
> **Ngôn ngữ:** Python (Jupyter Notebook, OOP)  
> **Học phần:** Lập trình phân tích dữ liệu
>
> ## 🤖 2. Thuật toán A\* – Robot hút bụi

**Mục tiêu:**  
Cài đặt và mô phỏng **thuật toán A\*** để điều khiển robot hút bụi trong **ma trận Aₘ,ₙ**, tối ưu hóa tổng chi phí khi làm sạch toàn bộ ô **dirty (D)**:contentReference[oaicite:3]{index=3}.
>
> **Mô tả bài toán:**
- Ma trận gồm các ô: **F (free)**, **D (dirty)**, **C (clean)**.  
- Robot có thể:
- **Move** đến 1 trong **8 ô lân cận** (chi phí = 1).  
- **Suck** để làm sạch ô hiện tại.  
- Sau mỗi hành động, **mọi ô dirty còn lại** sẽ tăng thêm **1 đơn vị chi phí hút bụi**.

**Yêu cầu chương trình:**
- Cho phép người dùng:
- Nhập kích thước ma trận \(A_{m,n}\).  
- Chọn số lượng và vị trí ngẫu nhiên của các ô **dirty**.  
- Áp dụng **thuật toán A\*** để tìm lộ trình tối ưu cho robot.  
- Hiển thị:
- **Đường đi của robot** (Move/Suck).  
- **Tổng chi phí thực hiện**.  

